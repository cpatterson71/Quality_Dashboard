#streamlit-app.py
import streamlit as st
import pandas as pd
import plotly.express as px
from st_aggrid import AgGrid

st.set_page_config(layout='wide')
st.title('Quality Managment System Dashboard')
st.subheader('Quality Dashboard that collects data from the various spreadsheets and puts ' 
             'it in a condensed version that can be reviewed.')

#load the data
file = 'temp.csv'
data = pd.read_csv(file, index_col=False)
first = pd.DataFrame(data)

#create table of Deviations and OOS
file2 = 'temp2.csv'
data2 = pd.read_csv(file2)
first2 = pd.DataFrame(data2)

file3 = 'temp3.csv'
data3= pd.read_csv(file3)
first3 = pd.DataFrame(data3)

#set up tabs
tab1, tab2, tab3 = st.tabs(['Change Controls and Documents', 'Deviations and OOS', 'CAPAs and Complaints'])

with tab1:
    col1, col2 = st.columns([20, 400]) 
    with col1:
        second = pd.read_csv('Year.csv', index_col=False)
        #group by year
        x_axis = second['Year']
        y_axis = second['Average Days Open']
        fig = px.bar(second, x=x_axis, y=y_axis)
    st.write(fig)

    with col2:
        AgGrid(data2, height=400)

        #need to get number of change controls per month then year
        #use a chart similar to what was done above. 
    with tab2:
         col3, col4 = st.columns([300, 20])
         with col3:
            AgGrid(first3, height=300)
        
    # with tab3:st

            