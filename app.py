import pandas as pd
import streamlit as st

url = 'https://github.com/lucastandelosrios-lang/Proyecto_BootCamp/raw/refs/heads/main/datos_generales_ficticios.csv'
df=pd.read_csv(url, sep=';', encoding='utf-8')

selected_columns = ['FECHA_HECHOS', 'DELITO', 'ETAPA', 'FISCAL_ASIGNADO', 'DEPARTAMENTO', 'MUNICIPIO_HECHOS']
df = df[selected_columns].sort_values(by='FECHA_HECHOS', ascending=True).reset_index(drop=True)

df['FECHA_HECHOS'] = pd.to_datetime(df['FECHA_HECHOS'], errors='coerce')

df_serie_tiempo = df.copy()
df_serie_tiempo['FECHA_HECHOS'] = df['FECHA_HECHOS'].dt.date

#construir la pagina
st.set_page_config(page_title='Análisis de Datos de Delitos', layout='wide')
st.header('Análisis de Datos de Delitos')
st.dataframe(df)

st.subheader('Tipo de Delito')
delitos = df['DELITO'].value_counts()
st.bar_chart(delitos)






