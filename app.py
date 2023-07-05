# Our Code Here

import streamlit as st
import pandas as pd

import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import json

from urllib.request import urlopen
df = pd.read_csv("mpg.csv")

st.title('Intro streamlit app')
st.header("MPG Date expploration")
if st.sidebar.checkbox("Show Dataframe"):
    st.subheader("My dataset")
    st.dataframe(data=df)


left_column, mid_column, right_column = st.columns([3,1,1])

years = ['All'] + sorted(pd.unique(df['year']))
year = st.sidebar.selectbox("Choose a year", years)

if year == "All":
    reduced_df = df
else:
    reduced_df = df[df["year"]==year]

m_fig, ax = plt.subplots(figsize = (10,8))
ax.scatter(reduced_df['displ'], reduced_df['hwy'])
ax.set_title("Engine size vs milage")

st.pyplot(m_fig)

