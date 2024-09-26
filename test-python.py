import pandas as pd 
import plotly.express as px
import streamlit as st

st.title("Esto es un titulo")

st.subheader("Esto es un subtitutlo")

df = pd.read_csv('empleados.csv')

fig = px.bar(df, x='Ciudad', y='Salario')

st.plotly_chart(fig)