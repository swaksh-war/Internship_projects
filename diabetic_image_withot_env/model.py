import os
import cv2
import json
import math
import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow.keras import layers
from keras.optimizers import adam_v2
from tensorflow.keras.models import Sequential
from tensorflow.keras.applications import DenseNet121
from tensorflow.keras.callbacks import Callback, ModelCheckpoint
from tensorflow.keras.preprocessing.image import ImageDataGenerator
print("Libraries Imported Successfully model files")
np.random.seed(2020)
tf.set_random_seed(2020)


def preprocess_image(image_path, desired_size=224):
    im = Image.open(image_path)
    im = im.resize((desired_size,) * 2, resample=Image.LANCZOS)
    return im


def build_model():
    densenet = DenseNet121(
        weights="model/DenseNet.h5",
        include_top=False,
        input_shape=(224, 224, 3),
    )


    model = Sequential()
    model.add(densenet)
    model.add(layers.GlobalAveragePooling2D())
    model.add(layers.Dropout(0.5))
    model.add(layers.Dense(5, activation="sigmoid"))



    model.compile(
        loss="binary_crossentropy", optimizer=adam_v2.Adam(lr=0.00005), metrics=["accuracy"]
    )

    return model

def classify_image(img):
    model = build_model()
    model.load_weights("model/model.h5")
    x_val = np.empty((1, 224, 224, 3), dtype=np.uint8)
    x_val[0, :, :, :] = preprocess_image(img)
    y_val_pred = model.predict(x_val)
    return np.argmax(np.squeeze(y_val_pred[0]))
