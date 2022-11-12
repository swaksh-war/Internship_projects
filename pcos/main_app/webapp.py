import streamlit as st
import joblib
from PIL import Image

image = Image.open('doc.jpg')

st.title("PCOS DETECTION USING MACHINE LEARNING")
st.image(image)
st.write("We will ask you few questions answer them properly.")
fr = st.number_input("What is your Right Follicle Number?")
fl = st.number_input("What is your Left Follicle Number?")
sd = st.radio("Do you have skin darkening issue?", ("Yes","No"))
hg = st.radio("Is your Hair Growth Normal?", ("Yes", "No"))
wg = st.radio("Are you gaining Weight?", ("Yes", "No"))
cy = st.radio("No of Cycle(R/I)?", ("2","4","5"))

submit = st.button("Predict")

model = joblib.load('Decision_Tree.joblib')
page_bg_img = '''
<style>
body {
background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
background-size: cover;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

if submit:
    fr = fr
    fl = fl
    if sd == "Yes":
        sd = 1
    else:
        sd = 0
    
    if hg =="Yes":
        hg = 1
    else:
        hg = 0
    
    if wg == "Yes":
        wg = 1
    else:
        wg = 0
    
    if cy == "2":
        cy = 2
    elif cy == "4":
        cy = 4
    else:
        cy = 5
    
    result = model.predict([[fr,fl,sd,hg,wg,cy]])
    if result[0] == 1:
        st.write("You are suspected with PCOS, Please go and visit a doctor")
    else:
        st.write("You are totally fine!")


