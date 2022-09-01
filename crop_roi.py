from genericpath import exists
import os
from pathlib import Path

import torch
import torch.backends.cudnn as cudnn

from yolov5.models.common import DetectMultiBackend
from yolov5.utils.dataloaders import IMG_FORMATS, VID_FORMATS, LoadImages, LoadStreams
from yolov5.utils.general import (LOGGER, check_file, check_img_size, check_imshow, check_requirements, colorstr, cv2,
                           increment_path, non_max_suppression, print_args, scale_coords, strip_optimizer, xyxy2xywh)
from yolov5.utils.plots import Annotator, colors, save_one_box
from yolov5.utils.torch_utils import select_device, time_sync


def detect(fpath):
    imgsz = (640, 640)
    device = select_device('')
    save_dir = os.path.join(fpath)
    
    model = DetectMultiBackend("./yolov5/roi_detector.pt", device=device, dnn=False, data=None, fp16=False)
    stride, names, pt = model.stride, model.names, model.pt
    imgsz = check_img_size(imgsz, s=stride)

    dataset = LoadImages(fpath, img_size=imgsz, stride=stride, auto=pt)
    bs = 1  # batch_size

    model.warmup(imgsz=(1 if pt else bs, 3, *imgsz))  # warmup

    for path, im, im0s, vid_cap, s in dataset:
        im = torch.from_numpy(im).to(device)
        im = im.float()  # uint8 to fp16/32
        im /= 255  # 0 - 255 to 0.0 - 1.0
        if len(im.shape) == 3:
            im = im[None]  # expand for batch dim

        # Inference
        pred = model(im, augment=False, visualize=False)

        # NMS
        pred = non_max_suppression(pred, conf_thres=0.3, iou_thres=0.1, classes=None, agnostic=False, max_det=1000)

        # Process predictions
        for i, det in enumerate(pred):  # per image
            p, im0, frame = path, im0s.copy(), getattr(dataset, 'frame', 0)
            p = Path(p)  # to Path
            
            save_path = os.path.join(save_dir, p.name)  # im.jpg
            
            gn = torch.tensor(im0.shape)[[1, 0, 1, 0]]  # normalization gain whwh
            imc = im0.copy()
            
            if len(det):
                # Rescale boxes from img_size to im0 size
                det[:, :4] = scale_coords(im.shape[2:], det[:, :4], im0.shape).round()

                # Write results
                os.makedirs(os.path.join(save_dir, 'crops'), exist_ok=True)
                for *xyxy, conf, cls in reversed(det):
                    save_one_box(xyxy, imc, file=os.path.join(save_dir, 'crops', f'{p.stem}.jpg'), BGR=True)