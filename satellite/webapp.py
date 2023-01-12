import joblib
import cv2
import streamlit as st
from PIL import Image
model = joblib.load('classifier.joblib')
st.title("Hello There!")
st.write("Enter an image to check whether its a desert or cloudy or greenery or water body satellite image")
img = st.file_uploader('Upload Your Image here: ')
but = st.button('Predict')
if but:
    img = Image.open(img)
    img.save('temp.jpg')
    img = cv2.imread('temp.jpg', 0)
    img = cv2.resize(img, (64,64))
    img = img / 255
    img = img.flatten()
    img = [img]
    pred = model.predict(img)
    print(pred)
    if pred == 0:
        st.write('Cloudy')
    if pred == 1:
        st.write('Desert')
    if pred == 2:
        st.write('Green Area')
    if pred == 3:
        st.write('Water Body')