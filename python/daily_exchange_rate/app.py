"""Module for loading and cleaning economic indicators data from a URL, 
then displaying it in a Streamlit app."""

import streamlit as st
import pandas as pd

# Data source URL
URL = "https://gee.bccr.fi.cr/IndicadoresEconomicos/Cuadros/frmConsultaTCVentanilla.aspx"

def load_data(url):
    """Loads table from the provided URL."""
    tables = pd.read_html(url, encoding='utf-8')
    df = tables[2]
    return df

def clean_dataframe(df):
    """"Cleans and formats the DateFrame."""
    # Set the column names to the first row of the table
    df.columns = df.iloc[0]

    # Drop the first row as it has been replaced by the column names
    df = df.drop(0)
    return df

def format_entity_types(data):
    """Formats entity types to fill null values."""
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
    """Converts and formats the 'Compra' column to float."""
    return data['Compra'].astype(float) / 100

def format_sell(data):
    """Converts and formats the 'Venta' column to float."""
    return data['Venta'].astype(float) / 100

def format_exchange_rate_differential(data):
    """Converts and formats the 'Diferencial Cambiario' column to float."""
    return data['Diferencial Cambiario'].astype(float) / 100

def format_last_update(data):
    """Converts and formats the 'Última Actualización' column to datetime."""
    return pd.to_datetime(
        data['Última Actualización'],
        infer_datetime_format=True,
        dayfirst=True,
        errors='coerce'
        ).dt.strftime('%d-%m-%Y %I:%M %p')


def main():
    """Main function to load, clean, and display data in a Streamlit app."""
    df = load_data(URL)
    df = clean_dataframe(df)
    df['Tipo de Entidad'] = format_entity_types(df)
    df['Compra'] = format_buy(df)
    df['Venta'] = format_sell(df)
    df['Diferencial Cambiario'] = format_exchange_rate_differential(df)
    df['Última Actualización'] = format_last_update(df)
    df = df.dropna()


    st.metric(df.loc[4][1], df.loc[4][3], df.loc[4][5])

    #print(df.loc[4][1])

    st.dataframe(df)
    #print(df)

if __name__ == "__main__":
    main()
