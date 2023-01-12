import streamlit as st
import joblib
airline_dict = {
    'IndiGo':0,
    'Air India':1,
    'Jet Airways':2,
    'SpiceJet':3,
    'Multiple carriers':4,
    'GoAir':5,
    'Vistara':6,
    'Air Asia': 7,
    'Vistara Premium economy': 8,
    'Jet Airways Business' : 9,
    'Multiple carriers Premium economy' : 10,
    'Trujet': 11
    }

stops = {
    'non-stop':0,
    '2 stops': 1,   
    '1 stop': 2,
    '3 stops': 3,
    '4 stops': 4
}
model = joblib.load("model.joblib")

st.title('Flight Price Predictor using Airline, number of stop and flight duration')

airlline = st.selectbox("What is your airlines ?", ("IndiGo", "Air India", "Jet Airways", "SpiceJet", "GoAir", "Vistara", "Air Asia", "TruJet", "Vistara Premium economy", "Jet Airways Business", "Multiple carriers", "Multiple carriers Premium economy"))

airline_inp = airline_dict[airlline]

stop_num = st.selectbox("Number of Stops", ('non-stop', '2 stops', '1 stop', '3 stops', '4 stops'))
stop_inp = stops[stop_num]

duration = st.number_input('Duration of flight in minutes: ')
submit = st.button('Predict')
if submit:
    val = model.predict([[airline_inp, stop_inp, duration]])
    val = val[0]
    st.write(f'{round(val)} rs approximately')
