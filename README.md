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

## Performance
### FR score threshold based on transient elastography (TE)
| TE target | FR score threshold | Accuracy | Sensitivity | Specificity |   PPV  |   NPV  |
|:---------:|:------------------:|:--------:|:-----------:|:-----------:|:------:|:------:|
|     6     |       1.8677       |  0.6957  |    0.6587   |    0.7267   | 0.6694 | 0.7171 |
|     7     |       1.8677       |  0.6993  |    0.7071   |    0.6949   | 0.5645 | 0.8092 |
|     8     |       1.9540       |  0.7717  |    0.6585   |    0.8196   | 0.6067 | 0.8503 |
|     9     |       1.9540       |  0.7826  |    0.7042   |    0.8098   | 0.5618 | 0.8877 |
|     10    |       1.9582       |  0.7971  |    0.7541   |    0.8093   | 0.5287 | 0.9206 |
|     11    |       1.9582       |  0.7935  |    0.8000   |    0.7920   | 0.4598 | 0.9471 |
|     12    |       1.9582       |  0.8007  |    0.8810   |    0.7863   | 0.4253 | 0.9735 |
|     13    |       1.9582       |  0.7899  |    0.8919   |    0.7741   | 0.3793 | 0.9788 |
|     14    |       1.9582       |  0.7899  |    0.8919   |    0.7741   | 0.3793 | 0.9788 |
|     15    |       1.9582       |  0.7790  |    0.9333   |    0.7602   | 0.3218 | 0.9894 |
|     16    |       1.9582       |  0.7790  |    0.9333   |    0.7602   | 0.3218 | 0.9894 |
|     17    |       2.1139       |  0.8768  |    0.8276   |    0.8826   | 0.4528 | 0.9776 |
|     18    |       2.1139       |  0.8804  |    0.8846   |    0.8800   | 0.4340 | 0.9866 |
|     19    |       2.1139       |  0.8804  |    0.9167   |    0.8770   | 0.4151 | 0.9910 |
|     20    |       2.1452       |  0.8986  |    0.9091   |    0.8976   | 0.4348 | 0.9913 |

### FR score threshold based on magnetic resonance elastography (MRE)
| MRE target | FR score threshold | Accuracy | Sensitivity | Specificity |   PPV  |   NPV  |
|:----------:|:------------------:|:--------:|:-----------:|:-----------:|:------:|:------:|
|     2.0    |       1.8074       |  0.6581  |    0.6456   |    0.7047   | 0.8903 | 0.3488 |
|     2.5    |       1.9315       |  0.7108  |    0.6005   |    0.8323   | 0.7978 | 0.6541 |
|     3.0    |       1.9392       |  0.7678  |    0.7213   |    0.7926   | 0.6494 | 0.8422 |
|     3.5    |       1.9392       |  0.7635  |    0.7933   |    0.7533   |  0.524 | 0.9142 |
|     4.0    |       1.9430       |  0.7493  |    0.8286   |    0.7295   | 0.4328 | 0.9447 |
|     4.5    |       1.9430       |  0.7379  |    0.8750   |    0.7119   | 0.3657 | 0.9677 |
|     5.0    |       1.9430       |  0.7194  |    0.9176   |    0.6921   | 0.2910 | 0.9839 |
|     5.5    |       1.9430       |  0.7194  |    0.9176   |    0.6921   | 0.2910 | 0.9839 |
|     6.0    |       2.0168       |  0.7436  |    0.8936   |    0.7328   | 0.1936 | 0.9897 |
|     6.5    |       2.0692       |  0.7877  |    0.8947   |    0.7816   | 0.1899 | 0.9924 |
|     7.0    |       2.1364       |  0.8191  |    0.8667   |    0.8170   | 0.1745 | 0.9928 |

## FAQ
- Are uploaded images could be opened to others?
    - No, this web module is running on your local PC, therefore, the data is free from the outflow. 
- For the deep learning model, should I need any GPUs?
    - No, we designed this web module as a CPU inference module.
- Can I use this for mass prediction?
    - No, I'm not a web developer, so this web module is just for demo. Please use a python script rather than a web module for mass prediction. In that case, you need knowledge about python code and PyTorch.

## References
The yolov5 packages were forked from [original yolov5 repository](https://github.com/ultralytics/yolov5)

