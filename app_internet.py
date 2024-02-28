import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from st_pages import Page,add_page_title, show_pages


data = pd.read_csv('Modulo_TIC.csv', low_memory=False)

st.header("Encuesta de Micronegocios - 2022", divider="rainbow")
st.subheader("Conexion")

data_internet = data.groupby(['P2532']).agg({
    'P2532' : 'count'
})

fig = px.pie(
    data_internet,
    values='P2532',
    names=['Si','No'],
    template='plotly_white'
    
)

fig.update_traces(hoverinfo='text+percent')
fig.update_layout(
    title=dict(
        text='7. El negocio o actividad tiene página web o presencia en un sitio web?',
        font=dict( size = 15, family='Arial' ),
        automargin=False,
        yref='paper'
    )
)
st.plotly_chart(fig)
st.divider()

data_internet2 = data.groupby(['P1559']).agg({
    'P1559' : 'count'
})

fig = px.bar(
    data_internet2,
    y='P1559',
    x=['Si','No'],
    template='plotly'
)

fig.update_layout(
    title=dict(
        text='8. ¿El negocio o actividad tiene presencia en redes sociales (Facebook,Twitter, etc.)?',
        font=dict( size = 15, family='Arial' ),
        automargin=False,
        yref='paper'
    )
)

st.plotly_chart(fig)
st.divider()

data_internet3 = data.groupby(['P2524']).agg({
    'P2524' : 'count'
})

fig = px.bar(
    data_internet3,
    y='P2524',
    x=['Si','No'],
    template='plotly'
)

fig.update_layout(
    title=dict(
        text='9. ¿Este negocio o actividad tiene acceso o utiliza el servicio de internet?',
        font=dict( size = 15, family='Arial' ),
        automargin=False,
        yref='paper'
    )
)

st.plotly_chart(fig)
st.divider()

data_internet4 = data.groupby(['P1093']).agg({
    'P1093' : 'count'
})

fig = px.bar(
    data_internet4,
    y='P1093',
    x=['Si','No'],
    template='plotly'
)

fig.update_layout(
    title=dict(
        text='10. ¿Utiliza internet con conexión dentro del negocio o donde desarrolla su actividad? ',
        font=dict( size = 15, family='Arial' ),
        automargin=False,
        yref='paper'
    )
)

st.plotly_chart(fig)
st.divider()

data_internet5 = data.groupby(['P2528']).agg({
    'P2528' : 'count'
})

fig = px.bar(
    data_internet5,
    y='P2528',
    x=['Si','No'],
    template='plotly'
)

fig.update_layout(
    title=dict(
        text='11. ¿Qué tipo de conexión utiliza principalmente el negocio o actividad para acceder a internet?',
        font=dict( size = 15, family='Arial' ),
        automargin=False,
        yref='paper'
    )
)

st.plotly_chart(fig)
st.divider()

data_internet6 = data.groupby(['P1095']).agg({
    'P1095' : 'count'
})

fig = px.bar(
    data_internet6,
    y='P1095',
    x=['Es muy costoso','No lo necesita','El personal no sabe usarlo','No tiene dispositivo para conectarse',
        'El servicio no es de buena calidad','No hay cobertura del servicio en la zona'],
    template='plotly'
)

fig.update_layout(
    title=dict(
        text='12. ¿Cuál es la principal razón por la cual el negocio o actividad no utiliza internet?',
        font=dict( size = 15, family='Arial' ),
        automargin=False,
        yref='paper'
    )
)

st.plotly_chart(fig)
st.divider()

st.write(' 13. Del total del personal ocupado del negocio o actividad,¿cuántos utilizan internet para el desarrollo de sus actividades?')

data_internet7 = data.groupby(['P980']).agg({
    'P980' : 'count'
})
data_internet7 = data_internet7.iloc[~data_internet7.index.isin([0])]

st.dataframe(
    data_internet7,
    column_config = {
        "P980":"Cantida de Personas"
    })

st.header('',divider="blue")