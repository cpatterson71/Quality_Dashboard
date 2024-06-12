#streamlit-app.py
import altair as alt
import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')
st.title('Quality Managment System Dashboard')

#set up tabs
tab1, tab2, tab3 = st.tabs(['Change Controls', 'Deivations and OOS', 'CAPAs and Complaints'])

with tab1:
    col1, col2 = st.columns([20, 20]) 
    with col1:
        file = 'temp.csv'
        first = pd.read_csv(file)
        first = pd.DataFrame(first)
        x = first['Date Opened']
        y = first['Change Control'].count()
    st.line_chart(x, y)
    with col2:
        x1 = first['Date Opened']
        y1 = first['Days Open']
    st.bar_chart(x1, y1)

# with tab2:
#     buffer, col1, col2 = 

# with tab3:
