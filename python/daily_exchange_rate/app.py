import streamlit as st
import requests
import pandas as pd
import numpy as np

url = "https://gee.bccr.fi.cr/IndicadoresEconomicos/Cuadros/frmConsultaTCVentanilla.aspx"

tables = pd.read_html(url, encoding='utf-8')
df = tables[2]

# Igualar el nombre de las columnas con el primer row de la tabla
df.columns = df.iloc[0]

# Eliminar el primer row para que sea remplazado por los nombres de las columnas
df = df.drop(0)

""""Function that format Entity Types"""
def format_entity_types(data):
    entity_types = []
    current_entity = ''

    for entity in data['Tipo de Entidad']:
        
        if not pd.isna(entity):
            current_entity = entity
            entity_types.append(entity)
        else:
            entity_types.append(current_entity)
    
    return entity_types

def format_buy(data):
    return data['Compra'].astype(float) / 100

def format_sell(data):
    return data['Venta'].astype(float) / 100

def format_exchange_rate_differential(data):
    return data['Diferencial Cambiario'].astype(float) / 100

def format_last_update(data):
    return pd.to_datetime(data['Última Actualización'], infer_datetime_format=True, dayfirst=True, errors='coerce').dt.strftime('%d-%m-%Y %I:%M %p')

df['Tipo de Entidad'] = format_entity_types(df)
df['Compra'] = format_buy(df)
df['Venta'] = format_sell(df)
df['Diferencial Cambiario'] = format_exchange_rate_differential(df)
df['Última Actualización'] = format_last_update(df)

df = df.dropna()
print(df)

st.dataframe(df)