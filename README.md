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

## Performance
### FR score threshold based on transient elastography (TE)
| TE target threshold | FR score threshold | AUROC  | Accuracy | Sensitivity | Specificity | PPV   | NPV   |
|---------------------|--------------------|--------|----------|-------------|-------------|-------|-------|
|          6          |        1.855       | 0.7615 |   69.55  |    65.62    |    70.00    | 65.12 | 70.47 |
|          7          |        1.869       | 0.7557 |   69.06  |    66.34    |    70.62    | 56.30 | 78.62 |
|          8          |        1.873       | 0.7958 |   71.22  |    71.43    |    71.13    | 51.72 | 85.19 |
|          9          |        1.873       | 0.8083 |   71.94  |    76.39    |    70.39    | 47.41 | 89.51 |
|          10         |        1.908       | 0.8326 |   75.90  |    79.03    |    75.00    | 47.57 | 92.57 |
|          11         |        1.932       | 0.8411 |   76.62  |    80.39    |    75.77    | 42.71 | 94.51 |
|          12         |        1.932       | 0.8813 |   77.34  |    88.37    |    75.32    | 39.58 | 97.25 |
|          13         |        1.932       | 0.8825 |   76.26  |    89.47    |    74.17    | 35.42 | 97.80 |
|          14         |        1.932       | 0.8825 |   76.26  |    89.47    |    74.17    | 35.42 | 97.80 |
|          15         |        1.932       | 0.9198 |   75.18  |    93.55    |    72.87    | 30.21 | 98.90 |
|          16         |        1.932       | 0.9198 |   75.18  |    93.55    |    72.87    | 30.21 | 98.90 |
|          17         |        1.932       | 0.9241 |   74.82  |    93.33    |    72.58    | 29.17 | 98.90 |
|          18         |        1.932       | 0.9371 |   74.10  |    96.15    |    71.83    | 26.04 | 99.45 |
|          19         |        1.984       | 0.9425 |   81.29  |    95.83    |    79.92    | 31.08 | 99.51 |
|          20         |        1.984       | 0.9429 |   80.58  |    95.45    |    79.30    | 28.38 | 99.51 |

### FR score threshold based on magnetic resonance elastography (MRE)
| TE target threshold | FR score threshold | AUROC  | Accuracy | Sensitivity | Specificity | PPV   | NPV   |
|---------------------|--------------------|--------|----------|-------------|-------------|-------|-------|
|         2.0         |         1.8        | 0.7167 |   65.17  |    63.75    |    70.39    | 88.81 | 34.52 |
|         2.5         |        1.851       | 0.7722 |   69.80  |    67.91    |    71.89    | 72.78 | 66.94 |
|         3.0         |        1.872       | 0.8121 |   72.75  |    77.33    |    70.32    | 58.05 | 85.38 |
|         3.5         |        1.904       | 0.8378 |   73.60  |    81.67    |    70.86    | 48.68 | 91.95 |
|         4.0         |        1.913       | 0.8513 |   72.89  |    83.69    |    70.23    | 40.97 | 94.58 |
|         4.5         |        1.936       | 0.8587 |   73.60  |    86.73    |    71.12    | 36.16 | 96.60 |
|         5.0         |        1.939       | 0.8763 |   72.47  |    90.59    |    70.02    | 29.06 | 98.21 |
|         5.5         |        2.005       | 0.8836 |   75.00  |    84.75    |    74.12    | 22.83 | 98.17 |
|         6.0         |        2.005       | 0.8863 |   74.44  |    89.36    |    73.38    | 19.18 | 98.99 |
|         6.5         |        2.015       | 0.9067 |   74.86  |    92.11    |    73.89    | 16.59 | 99.40 |
|         7.0         |        2.015       | 0.8966 |   73.74  |    90.00    |    73.02    | 12.80 | 99.40 |

## FAQ
- Are uploaded images could be opened to others?
    - No, this web module is running on your local PC, therefore, the data is free from the outflow. 
- For the deep learning model, should I need any GPUs?
    - No, we designed this web module as a CPU inference module.
- Can I use this for mass prediction?
    - No, I'm not a web developer, so this web module is just for demo. Please use a python script rather than a web module for mass prediction. In that case, you need knowledge about python code and PyTorch.

## References
The yolov5 packages were forked from [original yolov5 repository](https://github.com/ultralytics/yolov5)

