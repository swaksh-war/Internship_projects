import os
import sys
from flask import Flask, redirect, url_for, request, render_template, Response, redirect,jsonify
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.applications.imagenet_utils import preprocess_input, decode_predictions
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from keras import layers
from tensorflow.keras.optimizers import Adam
from keras.models import Sequential
from tensorflow.keras.applications import DenseNet121
from keras.callbacks import Callback, ModelCheckpoint
from PIL import Image
from models.model import build_model, preprocess_image
import numpy as np
from utils import base64_to_pil
print("All Libraries Loaded in application file")
app = Flask(__name__)

MODEL_PATH = './models/pretrained/model.h5'

# Loading trained model
model = build_model()
model.load_weights(MODEL_PATH)
print('Open the chrome and type localhost:5000')


def model_predict(img, model):
    """
    0 - No DR
    1 - Mild
    2 - Moderate
    3 - Severe
    4 - Proliferative DR
    """
    
    ## Preprocessing the image
    x_val = np.empty((1, 224, 224, 3), dtype=np.uint8)
    img = img.resize((224,) * 2, resample=Image.LANCZOS)
    x_val[0, :, :, :] = img

    preds = model.predict(x_val)
    return preds


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        img = base64_to_pil(request.json)
        preds = model_predict(img, model)

        # Process result to find probability and class of prediction
        pred_proba = "{:.3f}".format(np.amax(preds))    # Max probability
        pred_class = np.argmax(np.squeeze(preds))
        diagnosis = ["No DR", "Mild", "Moderate", "Severe", "Proliferative DR"]

        result = diagnosis[pred_class]
        return jsonify(result=result, probability=pred_proba)

    return None


if __name__ == '__main__':
    http_server = WSGIServer(('0.0.0.0', 5000), app)
    http_server.serve_forever()

