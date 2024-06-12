### Instalacion de pandas
# pip install pandas

### Instalacion de matplotlib
# pip install matplotlib


import pandas as pd
import matplotlib.pyplot as plt

#URL del dataset de COVID-19
url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"

# Leer dataset
df = pd.read_csv(url)

# Mostrar las primera lineas del data frame
print(df.head)

# Mostar las columanas del data frame
print(df.columns)

# Resumen estadistico de las columnas numericas
print(df.describe)

# Filtrar datos por Espana
df_spain = df[df['location'] == 'Spain']

# Mostrar las primera lineas del data frame filtrado
print(df_spain)


### Visualizacion de la evulucion de casos

# Seleccionar las columnas de interes
df_spain_cases = df_spain[['date', 'total_cases']]

# Convertir la columna 'date' a tipo datetime
df_spain_cases['date'] = pd.to_datetime(df_spain_cases['date'])

# Converitir la columna 'date' como indice
df_spain_cases.set_index('date', inplace=True)

# Grafica de evolucion de los casos confirmados
plt.figure(figsize=(10,6))
plt.plot(df_spain_cases.index, df_spain_cases['total_cases'], label = 'Total Cases')
plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.title('Evolution of COVID-19 Cases in Spain')
plt.legend()
plt.grid(True)
plt.show()

### Analisis de tendencias

df_spain = df[df['location'] == 'Spain'].copy()
df_spain['date'] = pd.to_datetime(df_spain['date'])

# Calcular casos nuevos diarios
df_spain['new_cases'] = df_spain['total_cases'].diff()

df_spain['new_cases_7d'] = df_spain['new_cases'].rolling(window=7).mean()

# Graficar los casos nuevos diarios y su medi movil
plt.figure(figsize=(10,6))
plt.plot(df_spain['date'], df_spain['new_cases'], label='New Cases')
plt.plot(df_spain['date'], df_spain['new_cases_7d'], label='7-Day Movin Average', color='orange')
plt.xlabel('Date')
plt.ylabel('New Cases')
plt.title('Daily New COVID-19 Cases in Spain')
plt.legend()
plt.grid(True)
plt.show()

df_spain.to_csv('covid19_spain.csv', index=False)




