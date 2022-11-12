import streamlit as st
import joblib

st.title("Lets check whether your issue will be resolved or not")

resar = st.number_input('Residential area:')
bltfr = st.number_input("Built FAR: ")
residfr = st.number_input("Resid FAR: ")
numflr = st.number_input("Number of floors: ")
bldgdpth = st.number_input("Building Depth: ")
bldgarea = st.number_input("Building Area")
faclfr = st.number_input("Facilitate so far: ")
lostar = st.number_input("Lot Area: ")
yral1 = st.number_input("Year alter 1: ")
predict = st.button("predict")

model = joblib.load('xgb.joblib')

if predict:
    res = model.predict([[resar, bltfr, residfr, numflr, bldgdpth, bldgarea, faclfr, lostar, yral1]])
    if res[0] == 1:
        st.write('can be resolved')
    else:
        st.write("cant be resolved")
