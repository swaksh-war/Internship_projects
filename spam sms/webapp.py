import streamlit as st
from model_predict import predict_spam

st.title("Spam or Not spam that is the question!")
st.write("enter the message below to know whether its a spam or nor")

sample_message = st.text_input("enter your message here")
submit = st.button("Predict")

if submit:
    if predict_spam(sample_message):
        st.write('This is a SPAM message.')
    else:
        st.write('This is a (normal) message.')