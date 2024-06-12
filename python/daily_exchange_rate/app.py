import streamlit as st
import requests
import pandas as pd

url = "https://gee.bccr.fi.cr/IndicadoresEconomicos/Cuadros/frmConsultaTCVentanilla.aspx"


tables = pd.read_html(url)
df = tables[2]

st.table(df)

print(df)