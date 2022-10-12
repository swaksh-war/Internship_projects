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
print("libraries Imported Successfully")
SEED = 42
np.random.seed(SEED)
tf.random.set_seed(SEED)


def preprocess_image(image_path, desired_size=224):
    img = Image.open(image_path)
    img = img.resize((desired_size,) * 2, resample=Image.LANCZOS)

    return img

def build_model():

    densenet = DenseNet121(
        weights="models/pretrained/DenseNet.h5",
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
    model.load_weights("models/pretrained/model.h5")
    x_val = np.empty((1, 224, 224, 3), dtype=np.uint8)
    x_val[0, :, :, :] = preprocess_image(img)
    y_val_pred = model.predict(x_val)
    return np.argmax(np.squeeze(y_val_pred[0]))
