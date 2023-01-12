import streamlit as st
from tensorflow import keras
from PIL import Image
import numpy as np

def predict_model(img, model):
    x_val = np.empty((1, 128, 128, 3), dtype=np.uint8)
    img = img.resize((128,)*2, resample=Image.LANCZOS)
    x_val[0, :, :, :] = img
    preds = model.predict(x_val)
    return preds
model = keras.models.load_model('plantgrowthmodel.h5')
# img = Image.open('00b6eee9f.png')
# print(predict_model(img, model))

st.title("Plant Growth Tracker")
st.write("With this app you can identify different stages of wheat plant of different type")
img = st.file_uploader('Upload Your Image here: ')
img = Image.open(img)
predict = st.button('Predict')
if predict:
    pred = predict_model(img, model)
    num = np.where(pred == 1)
    if num[1] == 1:
        st.write("This is a common chick wheat and it is in pre matured state means it has just got out of soil known as sprout")
    if num[1] == 2:
        st.write("This is common wheat with Loose silky bent stage known as sapling.")
    if num[1] == 0:
        st.write("This is wheat with black grass level its known as seedling stage.")
    
    st.write(num[1])

