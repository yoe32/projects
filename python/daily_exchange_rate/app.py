import streamlit as st
import requests
import pandas as pd

url = "https://gee.bccr.fi.cr/IndicadoresEconomicos/Cuadros/frmConsultaTCVentanilla.aspx"


tables = pd.read_html(url)
df = tables[2]

#st.table(df)

# Igualar el nombre de las columnas con el primer row de la tabla
df.columns = df.iloc[0]

# Cambiar el nombre de la ultima columna por temas de tildes
df = df.rename(columns={df.columns[5] : 'Ultima Actualizacion'})

# Eliminar el primer row para que sea remplazado por los nombres de las columnas
df = df.drop(0)
df = df.reset_index(drop=True)


#print(df.head())
print(df)

