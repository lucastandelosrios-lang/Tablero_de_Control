import pandas as pd
import streamlit as st

url = 'https://github.com/lucastandelosrios-lang/Proyecto_BootCamp/raw/refs/heads/main/datos_generales_ficticios.csv'
df=pd.read_csv(url, sep=';', encoding='utf-8')

#Crear lista de los colu,nas de interes
selected_columns = ['FECHA_HECHOS', 'DELITO', 'ETAPA', 'FISCAL_ASIGNADO', 'DEPARTAMENTO', 'MUNICIPIO_HECHOS']
#actualizo el dataframe -df- con las columnas de interes ordenadas por fceha y reseteo el indice
df = df[selected_columns].sort_values(by='FECHA_HECHOS', ascending=True).reset_index(drop=True)

# Convierto la columna FECHA_HECHOS a formato fecha
df['FECHA_HECHOS'] = pd.to_datetime(df['FECHA_HECHOS'], errors='coerce')
# Extraigo solo la fecha sin la hora
df['FECHA_HECHOS'] = df['FECHA_HECHOS'].dt.date

#st.dataframe(df)

#cALCULO EL MUNICIPIO CON MAS DELITOS
max_MUNICIPIO = df['MUNICIPIO_HECHOS'].value_counts().index[0].upper()
max_cantidad_municipio = df['MUNICIPIO_HECHOS'].value_counts().iloc[0]

#st.write(max_MUNICIPIO)
st.write(f"### Municipios con mas delitos: {max_MUNICIPIO} con {max_cantidad_municipio} reportes")

#construir la pagina
st.set_page_config(page_title='Análisis de Datos de Delitos', layout='centered')
st.header('Análisis de Datos de Delitos')
st.dataframe(df)

st.subheader('Tipo de Delito')
delitos = df['DELITO'].value_counts()
st.bar_chart(delitos)






