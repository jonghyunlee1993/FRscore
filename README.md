# FR score
Fibrosis risk score calculator web module

To compute the FR score, you need AST, ALT, PLT, and more than two images of abdominal ultrasound image (more is the better)

![image](https://user-images.githubusercontent.com/37280722/188170182-62ac7d8c-97b3-4c59-9ade-f515aec5796e.png)

## User guide
1. Download python 3.8
2. Install requiring packages using `pip install -r requirements.txt`
3. Download the image-level regression file (there are two options)
    - Download the weight file using [Google Drive](https://drive.google.com/drive/folders/1VZSJUk7acyuOyJO1CjOpA843OivXdTN0?usp=sharing)
    - Download the weight file using Git LFS
4. Type `python ./app.py`
5. GO to `127.0.0.1:5000` on your web browser
6. Fill up AST, ALT, PLT, and age (optional). With choose files button, you can upload a series of ultrasound images. The image should png or jpg file format. 

## Executable file
- Using pyinastaller, you can generate an executable file
`pyinstaller --add-data "weights;weights" --add-data "templates;templates" --add-data "yolov5;yolov5" --add-data "uploaded;uploaded" --hidden-import torch --hidden-import cv2 --hidden-import albumentations --hidden-import flask --hidden-import timm --hidden-import tqdm --hidden-import glob --hidden-import pathlib app.py`
- Or download folder from [Google Drive](https://drive.google.com/drive/folders/1E0sFaVaah_-G55Vb-JGW6e69VNa6zSkX). Download folder and double click the `app.exe` file

## Performance
### FR score threshold based on magnetic resonance elastography (MRE)
| MRE kPa | FR score | AUROC | Accuracy | Sensitivity | Specificity | PPV   | NPV   |
|---------|----------|-------|----------|-------------|-------------|-------|-------|
| 2.0     | 1.043    | 0.725 | 65.24    | 63.38       | 70.47       | 88.92 | 34.43 |
| 2.5     | 1.110    | 0.777 | 69.66    | 69.29       | 70.06       | 71.83 | 67.44 |
| 3.0     | 1.190    | 0.816 | 72.79    | 77.46       | 70.31       | 58.15 | 85.41 |
| 3.5     | 1.250    | 0.844 | 74.22    | 82.68       | 71.32       | 49.66 | 92.33 |
| 4.0     | 1.280    | 0.859 | 73.50    | 85.00       | 70.64       | 41.90 | 94.98 |
| 4.5     | 1.311    | 0.872 | 74.07    | 87.50       | 71.53       | 36.84 | 96.79 |
| 5.0     | 1.394    | 0.891 | 74.93    | 89.41       | 72.93       | 31.28 | 98.04 |
| 5.5     | 1.394    | 0.897 | 72.36    | 91.53       | 70.61       | 22.22 | 98.91 |
| 6.0     | 1.429    | 0.905 | 73.08    | 93.62       | 71.60       | 19.13 | 99.36 |
| 6.5     | 1.429    | 0.924 | 72.36    | 97.37       | 70.93       | 16.09 | 99.79 |
| 7.0     | 1.429    | 0.909 | 71.23    | 96.67       | 70.09       | 12.61 | 99.79 |

## FAQ
- Are uploaded images could be opened to others?
    - No, this web module is running on your local PC, therefore, the data is free from the outflow. 
- For the deep learning model, should I need any GPUs?
    - No, we designed this web module as a CPU inference module.
- Can I use this for mass prediction?
    - No, I'm not a web developer, so this web module is just for demo. Please use a python script rather than a web module for mass prediction. In that case, you need knowledge about python code and PyTorch.

## References
The yolov5 packages were forked from [original yolov5 repository](https://github.com/ultralytics/yolov5)

