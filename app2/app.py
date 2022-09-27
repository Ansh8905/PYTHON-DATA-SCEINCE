import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

# Step 1 - load the data

@st.cache
def load_data():
    weatherdf = pd.read_csv('weather.csv', parse_dates=['Date.Full'], dayfirst=True)
    weatherdf.columns = ['precipation','date','month','week','year','city','code','location',
    'state','avg_temp','max_temp','min_temp','wind_direction','wind_speed']
    #dropped cols
    weatherdf.drop(columns=['code','location'], inplace=True) 
    return weatherdf

#step2 - setup initial  ui elements
st.set_page_config(
    page_title="weather analysis",
    page_icon='☁️',
    layout='wide'
)

st.title("WEATHER ANALYSIS APP☁️")
df = load_data()

st.sidebar.header("OPTIONS")

view_data = st.sidebar.checkbox("see raw data")
if view_data:
    st.write(df)