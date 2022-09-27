from pyparsing import col
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

numerical_cols = df.select_dtypes(include=np.number).columns.tolist()
pd.Categorical_cols = df.select_dtypes(include='object').columns.tolist()
#st.write(numerical_cols)
#st.write(pd.Categorical_cols)
colx = st.sidebar.selectbox("select a numerical column x",numerical_cols)
coly = st.sidebar.selectbox("select a numerical column y",numerical_cols)

graph_types = ['line','area','bar','scatter']
gtype = st.sidebar.radio("select a grapg type", graph_types)

if gtype == graph_types[0]:
    fig = px.line(df, x=colx, y=coly)
if gtype == graph_types[1]:
    fig = px.area(df, x=colx, y=coly)

if gtype == graph_types[2]:
    fig = px.bar(df, x=colx, y=coly)


if gtype == graph_types[3]:
    fig = px.scatter(df, x=colx, y=coly)

if fig:
    st.plotly_chart(fig, use_container_width=True)