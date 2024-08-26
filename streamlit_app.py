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
file = 'Open_Docs.csv'
data = pd.read_csv(file, index_col=False)
first = pd.DataFrame(data)

#create table of Deviations and OOS
file2 = 'Open_Dev.csv'
data2 = pd.read_csv(file2)
first2 = pd.DataFrame(data2)

#file of Open OOS
file3 = 'OOS_Open.csv'
data3= pd.read_csv(file3)
first3 = pd.DataFrame(data3)

#file of Open CAPA
file4 = 'Open_CAPA.csv'
data4= pd.read_csv(file4)
first4 = pd.DataFrame(data4)

#file of Open complaints
file5 = 'Open_comp.csv'
data5= pd.read_csv(file5)
first5 = pd.DataFrame(data5)

#set up tabs
tab1, tab2, tab3 = st.tabs(['Change Controls and Documents', 'Deviations and OOS', 'CAPAs and Complaints'])

with tab1:
    col1, col2, col3 = st.columns([1, 1, 120]) 
    with col3:
        second = pd.read_csv('Avg Days Open.csv')
        #group by year
        x_axis = second['Year']
        y_axis = second['Average Days Open']
        fig = px.bar(second, x=x_axis, y=y_axis)
    st.write(fig)

    with col2:
        third = pd.read_csv('Number per Year.csv')
        xp_axis = third['Year']
        yp_axis = third['Count']
        fig = px.bar(third,x=xp_axis, y=yp_axis )
    st.write(fig)

    with col1:
        first = pd.read_csv('Open_Docs.csv')
        AgGrid(first, height=400)

        #need to get number of change controls per month then year
        #use a chart similar to what was done above. 
with tab2:
    col4, col5, col8 = st.columns([120, 120, 120])
    with col4:
        AgGrid(first2, height=300)

    with col5:
        AgGrid(first3, height=300)

    with col8:
        third = pd.read_csv('Average_Devation_per_Year.csv')
        d_axis = third['Year']
        f_axis = third['Average Days Open']
        fig = px.bar(third,x=d_axis, y=f_axis ) 

    with tab3:
        col6, col7 = st.columns([100, 100])
        with col6:
            AgGrid(first4, height=300)
        
        with col7:
            AgGrid(first5, height=300)


            