import cv2
import glob

import timm
import torch

import albumentations as A
from albumentations.pytorch.transforms import ToTensorV2

def load_model():
    weight_path = "./weights/image_regression.pt"
    model = timm.create_model("resnet152", num_classes=1, pretrained=False)
    model.load_state_dict(torch.load(weight_path))
    model.eval()
    
    return model


def predict_image(fpath, model):
    images = glob.glob(fpath + "/*")
    results = []
    
    transform = A.Compose([
        A.Resize(width=224, height=224, p=1.0),
        A.Normalize(p=1.0),
        ToTensorV2()
    ])
    
    for image in images:
        image = cv2.imread(image)
        transformed_image = transform(image=image)
        image = transformed_image['image'].unsqueeze(0)
        
        result = model(image)
        result = result.detach().numpy()[0][0]
        results.append(result)
    
    results.sort(reverse=True)
    
    return results[0], results[2]
    