import sys
import math
import os
import random
import shutil

from flask import (Flask, flash, redirect, render_template, request,
                   send_from_directory, url_for)
from werkzeug.utils import secure_filename

if str("yolov5") not in sys.path:
    sys.path.append(str("yolov5"))  # add ROOT to PATH

from crop_roi import detect
from image_regression import load_model, predict_image
from patient_regression import FR_score

UPLOAD_FOLDER = './uploaded'


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def idle():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def predict():
    submission_id = random.randint(100000, 999999)
    destination = os.path.join(app.config['UPLOAD_FOLDER'], str(submission_id))
    os.mkdir(destination)
    
    files = request.files.getlist("file")
    
    for i, file in enumerate(files):
        filename = file.filename
        file.save(os.path.join(destination, filename))
    
    detect(destination)
    
    age = float(request.form["Age"])
    ast = float(request.form["AST"])
    alt = float(request.form["ALT"])
    plt = float(request.form["PLT"])

    if age is not None:
        fib4 = (age * ast) / (math.sqrt(alt) * plt)
    else:
        fib4 = 0
    fib4 = round(fib4, 2)
    apri = (ast / 34) / plt
    apri = round(apri, 2)

    model = load_model()
    v1, v2 = predict_image(destination + "/crops", model)

    fr_score = FR_score(v1, v2, ast, alt, plt)
    
    # remove data files
    shutil.rmtree(destination)
    
    return render_template('index.html',
                           session_id=f"Session ID: {submission_id}",
                           prediction_text=f'FR score: {round(fr_score, 4)}',
                           fib4_metric=f'FIB4: {fib4}',
                           apri_metric=f'APRI: {apri}')

if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True)