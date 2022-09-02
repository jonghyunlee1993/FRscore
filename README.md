# FR score

Fibrosis risk score calculator web module

To compute the FR score, you need AST, ALT, PLT, and more than two images of abdominal ultrasound image (more is the better)



![image-20220902231426136](/Users/jonghyun/Library/Application Support/typora-user-images/image-20220902231426136.png)



## User guide

1. Download python 3.8
2. Install requiring packages using `pip install -r requirements.txt`
3. Download the image-level regression file (there are two options)
    - Download the weight file using [Google Drive](https://drive.google.com/drive/folders/1VZSJUk7acyuOyJO1CjOpA843OivXdTN0?usp=sharing)
    - Download the weight file using Git LFS
4. Type `python ./app.py`
5. GO to `127.0.0.1:5000` on your web browser
6. Fill up AST, ALT, PLT, and age (optional). With choose files button, you can upload a series of ultrasound images. The image should png or jpg file format. 



## FAQ

- Are uploaded images could be opened to others?
    - No, this web module is running on your local PC, therefore, the data is free from the outflow. 
- For the deep learning model, should I need any GPUs?
    - No, we designed this web module as a CPU inference module.
- Can I use this for mass prediction?
    - No, I'm not a web developer, so this web module is just for demo. Please use a python script rather than a web module for mass prediction. In that case, you need knowledge about python code and PyTorch.



## References

The yolov5 packages were forked from [original yolov5 repository](https://github.com/ultralytics/yolov5)

