import streamlit as st
import tensorflow as tf
import cv2
import numpy as np
from PIL import Image

model_to_predict = tf.keras.models.load_model('covid_classification .h5')
def predict_covid(test_image):
  img = cv2.imread(test_image)
  img = img / 255.0
  img = cv2.resize(img, (50, 50))
  img = img.reshape(1,50,50,3)
  prediction = model_to_predict.predict(img)
  pred_class = np.argmax(prediction, axis = -1)
  return pred_class

def load_image(image_file):
    img = Image.open(image_file)
    return img


st.write("Covid-19 classification using CNN")



pic = st.file_uploader("Upload a X-ray picture!")
submit = st.button('submit')



if submit:
    pic_details = {"filename":pic.name, 'filetype':pic.type, 'filesize':pic.size}
    st.write(pic_details)

    st.image(load_image(pic), width=250)

    with open('test.jpg', 'wb') as f:
        f.write(pic.getbuffer())
    pred_class = predict_covid('test.jpg')
    if pred_class == 1:
        st.write('You have covid and its severe level!')
    
    if pred_class == 2:
        st.write('We found Lung Opacital damage, its a Sign of mild severety of Covid!')
    
    if pred_class == 3:
        st.write('We found Viral Pneumonial signs if your lungs, You may have a low severe Covid')
    
    if pred_class == 0:
        st.write('Chill Bro! You are fine as red wine!')