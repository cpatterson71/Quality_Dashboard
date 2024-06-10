#streamlit-app.py
import altair as alt
import streamlit as st
import pandas as pd
from st_aggrid import Agrid

st.set_page_config(layout='wide')
st.title('Quality Managment System Dashboard')

#set up tabs
tab1, tab2, tab3 = st.tabs(['Change Controls', 'Deivations and OOS', 'CAPAs and Complaints'])

with tab1:
    col1, col2 = st.columns([20, 20]) 
    with col1:
        file = 'temp.csv'
        first = pd.read_csv(file, index=False)
        x = first['Date Opened']
        y = first['Days Open']
    st.line_chart(x, y)
    with col2:
        x = first[]
        y = first[]
    st.altair_chart

with tab2:
    buffer, col1, col2 = 

with tab3:
