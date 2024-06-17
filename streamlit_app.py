#streamlit-app.py
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')
st.title('Quality Managment System Dashboard')

#set up tabs
tab1, tab2, tab3 = st.tabs(['Change Controls', 'Deivations and OOS', 'CAPAs and Complaints'])

with tab1:
    col1, col2 = st.columns([20, 20]) 
    with col1:
        #load the data
        file = 'temp.csv'
        data = pd.read_csv(file)
        first = pd.DataFrame(data)

    #     #create x axis groupby year
    #     x_axis = first['Date Opened'].groupby(['Date'] )

        
        
    #     #create line chart
    #     fig = px.line_ternary(first, x='Date Opened', y=])

    # with col2:
    #     x1 = first['Date Opened']
    #     y1 = first['Days Open']
    # st.bar_chart(x1, y1)

# with tab2:
#     buffer, col1, col2 = 

# with tab3:
