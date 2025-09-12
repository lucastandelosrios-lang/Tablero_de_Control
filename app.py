import pandas as pd
import streamlit as st
import plotly.express as px


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

etapa_mas_frecuente = df['ETAPA'].value_counts().index[0].upper()
cant_etapa_mas_frecuente = df['ETAPA'].value_counts().iloc[0]

#st.write(max_MUNICIPIO)
st.write(f"### Municipios con mas delitos: {max_MUNICIPIO} con {max_cantidad_municipio} reportes")
st.write(f'{etapa_mas_frecuente} tiene {cant_etapa_mas_frecuente} registros')



#construir la pagina
st.set_page_config(page_title='Análisis de Datos de Delitos', layout='centered')
st.title('Análisis de Datos de Delitos')

st.header('Análisis de Datos de Delitos')
st.dataframe(df)

st.subheader('Tipo de Delito')
delitos = df['DELITO'].value_counts()
st.bar_chart(delitos)

#ejercicio 2 Departamento con más delitos
max_DEPARTAMENTO = df['DEPARTAMENTO'].value_counts().index[0].upper()
max_cantidad_departamento = df['DEPARTAMENTO'].value_counts().iloc[0]
st.write(f"### Departamento con mas delitos: {max_DEPARTAMENTO} con {max_cantidad_departamento} reportes")
st.subheader('Departamento con más delitos')
departamentos = df['DEPARTAMENTO'].value_counts()
st.bar_chart(departamentos)

st.subheader('Distribución por Departamentos')
fig = px.pie(
    values=departamentos.values,
    names=departamentos.index
    )
fig.update_traces(textposition='outside', textinfo='percent+label')
fig.update_layout(showlegend=False, height=400)
st.plotly_chart(fig)

df_delitos = df.groupby(['DEPARTAMENTO', 'DELITO']).size().reset_index(name='conteo')
fig = px.bar(df_delitos, x='DEPARTAMENTO', y='conteo', color='DELITO', barmode='stack')
st.plotly_chart(fig)
st.write(df_delitos)







