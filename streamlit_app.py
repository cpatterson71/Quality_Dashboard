#streamlit-app.py
import streamlit as st
import pandas as pd
import plotly.express as px
from st_aggrid import AgGrid

st.set_page_config(layout='wide')
st.title('Quality Managment System Dashboard')

#load the data
file = 'temp.csv'
data = pd.read_csv(file, index_col=False)
first = pd.DataFrame(data)

second = first.loc[:,['Date Opened', 'Change Control', 'Days Open', 'Year']]
 
#create x axis and strp down to date in Date Opened 
second.to_csv('temp.csv', index=False)

#create table of Deviations and OOS
file2 = 'temp2.csv'
data2 = pd.read_csv(file2)
first2 = pd.DataFrame(data2)

file3 = 'temp3.csv'
data3= pd.read_csv(file3)
first3 = pd.DataFrame(data3)




#set up tabs
tab1, tab2, tab3 = st.tabs(['Change Controls', 'Deivations and OOS', 'CAPAs and Complaints'])

with tab1:
    col1, col2 = st.columns([20, 20]) 
    with col1:
        #group by year
        number_CC = second.groupby(['Year']).mean()['Days Open']
        #need average per year days open

        x_axis = second['Year']
        y_axis = number_CC
        fig = px.bar(second, x=x_axis, y=y_axis)
    st.write(fig)

    # with col2:
        #need to get number of change controls per month then year
        #use a chart similar to what was done above. 
    with tab2:
         col3, col4 = st.columns([20, 20])
         with col3:
            AgGrid(data2, height=300)

         with col4:
            AgGrid(first3, height=300)
        
    # with tab3:
            