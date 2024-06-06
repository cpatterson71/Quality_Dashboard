#streamlit-app.py
import altair as alt
import streamlit as st
import Quality_Data_Clean_Up 
from st_aggrid import Agrid

st.set_page_config(layout='wide')
st.title('Quality Managment System Dashboard')

#set up tabs
tab1, tab2, tab3 = st.tabs(['Change Controls', 'Deivations and OOS', 'CAPAs and Complaints'])

with tab1:
    x = temp['Date Opened']
    y = temp['Days Open']
    st.line_chart(x, y)

with tab3:
    buffer, col1, col2 = 


