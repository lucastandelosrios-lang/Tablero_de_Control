import pandas as pd
import streamlit as st
import plotly.express as px


url = 'https://github.com/lucastandelosrios-lang/Proyecto_BootCamp/raw/refs/heads/main/datos_generales_ficticios.csv'
df=pd.read_csv(url, sep=';', encoding='utf-8')

#Crear lista de los columnas de interes
selected_columns = ['FECHA_HECHOS', 'DELITO', 'ETAPA', 'FISCAL_ASIGNADO', 'DEPARTAMENTO', 'MUNICIPIO_HECHOS']
#actualizo el dataframe -df- con las columnas de interes ordenadas por fceha y reseteo el indice
df = df[selected_columns].sort_values(by='FECHA_HECHOS', ascending=True).reset_index(drop=True)

# Convierto la columna FECHA_HECHOS a formato fecha
df['FECHA_HECHOS'] = pd.to_datetime(df['FECHA_HECHOS'], errors='coerce')

df_serie_tiempo = df.copy()
df_serie_tiempo['FECHA_HECHOS'] = df['FECHA_HECHOS'].dt.date

max_municipio = df['MUNICIPIO_HECHOS'].value_counts().index[0].upper()
max_cantidad_municipio = df['MUNICIPIO_HECHOS'].value_counts().iloc[0]

# CALCULO DE LA ETAPA QUE MAS VECES SE PRESENTA
# Ya que value_counts() genera un dataframe ORDENADO, traigo solo EL PRIMER INDICE .index[0]
etapa_mas_frecuente = df['ETAPA'].value_counts().index[0].upper()
# Ya que value_counts() genera un dataframe ORDENADO, traigo solo EL PRIMER VALOR .iloc[0]
cant_etapa_mas_frecuente = df['ETAPA'].value_counts().iloc[0]

#construir la pagina
#st.set_page_config(page_title='Análisis de Datos de Delitos', layout='wide')
st.markdown(
    """
    <style>
    .block-container {
    padding: 1rem 2rem 2rem 2rem;
    max-width: 1600px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.image('img/encabezado.png', use_container_width=True)

#Grafico de barras apiladas por departamento y tipo de delito
st.markdown('<h2>Delitos por Departamento</h2>', unsafe_allow_html=True)
df_delitos = df.groupby(['DEPARTAMENTO', 'DELITO']).size().reset_index(name='conteo')
fig = px.bar(df_delitos, x='DEPARTAMENTO', y='conteo', color='DELITO', barmode='stack')
st.plotly_chart(fig, key="bar_departamento")
fig.update_layout(showlegend=False, height=400)

#Crear 4 columnas para las Tatjetas
col1, col2, col3, col4 = st.columns(4)

with col1:
    #Tarjetas 1 - Municipio con mas delitos
    st.markdown(f"""<h3 style=
                    'color:#D9665B;
                    background-color:#F2D98D;
                    border:2px solid #D9665B;
                    border-radius:10px; padding:10px;
                    text-align:center'>
                    Municipio con más delitos: {max_municipio}</h3><br>""",
                    unsafe_allow_html=True)

with col2:
#Tarjetas 2 - 
    st.markdown(f"""<h3 style=
                'color:#F2A88D;
                background-color:#FFF6F5;
                border:2px solid #F2A88D;
                border-radius:10px; 
                padding:10px;
                text-align:center'>
                Delitos reportados<br> {max_cantidad_municipio} </h3><br>""",
                unsafe_allow_html=True)

with col3:
 #Tarjetas 3 - 
    st.markdown(f"""<h3 style=
                'color:#F2A88D;
                background-color:#FFF6F5;
                border:2px solid #F2A88D;
                border-radius:10px; 
                padding:10px;
                text-align:center'>
                Etapa mas recurrente<br> {etapa_mas_frecuente} </h3><br>""",
                unsafe_allow_html=True) 
      
with col4:
#Tarjetas 4 - 
    st.markdown(f"""<h3 style=
                'color:#F2A88D;
                background-color:#FFF6F5;
                border:2px solid #F2A88D;
                border-radius:10px; 
                padding:10px;
                text-align:center'>
                Procesos en esta etapa<br> {cant_etapa_mas_frecuente} </h3><br>""",
                unsafe_allow_html=True) 

col5, col6 = st.columns(2)

with col5:
    st.subheader('Tipo de Delito')
    tipo_delitos = df['DELITO'].value_counts()
    st.bar_chart(tipo_delitos)

with col6:
    st.subheader('Distribución por Departamentos')
    departamento = df['DEPARTAMENTO'].value_counts()
    fig = px.pie(
        names=departamento.index, #para los nombres de la torta
        values=departamento.values #para los valores de la torta
    )
    fig.update_traces(textposition='outside', textinfo='percent+label')
    fig.update_layout(showlegend=False, height=350)
    st.plotly_chart(fig, key="torta_departamento")


# Seleccion dato para visualizar
cols_grafico = ['DELITO', 'ETAPA', 'FISCAL_ASIGNADO', 'DEPARTAMENTO', 'MUNICIPIO_HECHOS']
df_grafico = df[cols_grafico]

st.subheader('Seleccione Dato a Visualizar')
variable = st.selectbox(
    'Seleccione la variable para el análisis',
    options= df_grafico.columns
)

#st.subheader('Tipo de Delito')
grafico = df_grafico[variable].value_counts() 
st.bar_chart(grafico)

if st.checkbox('Mostrar matriz de Datos'):
    st.subheader('Matriz de Datos')
    st.dataframe(df_grafico)

st.header('Consulta por Fiscal Asignado')
fiscal_consulta = st.selectbox(
    'Seleccione El Fiscal Asignado:',
    options = df['FISCAL_ASIGNADO'].unique()
)

df_fiscal = df[df['FISCAL_ASIGNADO'] == fiscal_consulta]
st.dataframe(df_fiscal)


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




st.write(df_delitos)

st.subheader("Tipo de Delito")
delitos = df['DELITO'].value_counts()
st.bar_chart(delitos)







