import streamlit as st
from tensorflow.keras.models import load_model

model = load_model('model.h5')

flag_dict = {'SF':0, 'S0': 1, 'REJ': 2, 'RSTR': 3, 'SH': 4, 'RSTO': 5, 'S1': 6, 'RSTOS0': 7, 'S3': 8, 'S2':9, 'OTH':10}

st.title('Security Attack checker')
st.write('Check whether your network is safe or not by entering certain parameter of your network at any instace and check whether you network is safe.')
dur = st.number_input('Enter the duration of of request(http): ')
proto_type = st.selectbox('Mention Protocol type: ', ('tcp', 'udp', 'icmp'))
if proto_type == 'tcp':
    proto_type = 2
elif proto_type == 'udp':
    proto_type = 1
else:
    proto_type = 0

flag_inp = st.selectbox('Enter the flag type: ',('SF', 'S0', 'REJ', 'RSTR', 'SH', 'RSTO', 'S1', 'RSTOS0', 'S3', 'S2', 'OTH'))
flag = flag_dict[flag_inp]
src_bytes = st.number_input('Incoming bytes: ')
dst_type = st.number_input('DST Bytes: ')
count = st.number_input('Count of request: ')

submit = st.button('submit')

if submit:
    val = model.predict([[dur, proto_type, flag, src_bytes, dst_type, count]])
    print(val)
    if val == 1:
        st.write('Normal')
    elif val != 0:
        st.write('Malicious')
