#ResArea, NumFloors, BuiltFar, BldgArea, BldgDepth, LotArea, ResidFar, FacilFar, Yearalter1
import pickle
import streamlit as st
with open('model.pickle', 'rb') as f:
    model = pickle.load(f)

st.title('Complaint type Detection based on 311 service request and PLUTO dataset')
st.write()

ResArea = st.number_input("Insert Residential Area(sqft): ")
NumFloors = st.number_input("Insert the number of floors: ")
BuiltFar = st.number_input("Insert the Area that has built so far: ")
BldgFar = st.number_input("Insert the Bldg Area: ")
BldgDepth = st.number_input("Insert the Building depth: ")
LotArea = st.number_input("Insert the LOT area(sqft): ")
ResidFar = st.number_input("Insert Residential so far: ")
FacilFar = st.number_input("Insert the area facilitate so far(sqft): ")
Yearalter1 = st.number_input("Insert the Year Alter 1: ")
submit = st.button('Submit')

if submit:
    pred = model.predict([[ResArea, NumFloors, BuiltFar, BldgFar, BldgDepth, LotArea, ResidFar, FacilFar, Yearalter1]])[0]
    if pred == 2:
        st.write('Unsanitary Condition')
    elif pred == 1:
        st.write('Hot water problem')
    else:
        st.write('Plumbing Issue')