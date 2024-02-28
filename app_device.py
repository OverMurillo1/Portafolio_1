import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from st_pages import Page,add_page_title, show_pages


data = pd.read_csv('Modulo_TIC.csv', low_memory=False)

st.header("Encuesta de Micronegocios - 2022", divider="rainbow")
st.subheader("Dispositivos")

data_movil1 = data.copy()

data_device = data_movil1.groupby(['P4001']).agg({
    'P4001' : 'count'
})

fig = px.pie(
    data_device,
    values='P4001',
    names=['Si','No'],
    template='plotly_white'
    
)

fig.update_traces(hoverinfo='text+percent')
fig.update_layout(
    title=dict(
        text='1. ¿Para su negocio o actividad utiliza alguno de los siguientes dispositivos electrónicos? <br>Computador(es) o Tableta(s) portátil(es)',
        font=dict( size = 15, family='Arial' ),
        automargin=False,
        yref='paper'
    )
)
st.plotly_chart(fig)

st.divider()

data_device2 = data.groupby(['P1087']).count()
data_device2 = data_device2.iloc[~data_device2.index.isin([0])]

fig = px.bar(
    data_device2,
    x='P1088',
    orientation='h',
    template='plotly'
)

fig.update_layout(
    title=dict(
        text='2. ¿Cuántos computadores de escritorio tiene en uso el negocio o actividad?',
        font=dict( size = 15, family='Arial' ),
        automargin=False,
        yref='paper'
    )
)

st.plotly_chart(fig)

st.divider()

data_device3 = data.groupby(['P1088']).count()
data_device3 = data_device2.iloc[~data_device2.index.isin([0])]

fig = px.bar(
    data_device3,
    y='P977',
    template='plotly'
)

fig.update_layout(
    title=dict(
        text='3. ¿Cuántos computadores portátiles tiene en uso el negocio o actividad?',
        font=dict( size = 15, family='Arial' ),
        automargin=False,
        yref='paper'
    )
)

st.plotly_chart(fig)

st.divider()

data_device4 = data.groupby(['P977']).count()
data_device4 = data_device2.iloc[~data_device2.index.isin([0])]

fig = px.bar(
    data_device4,
    y='P976',
    template='plotly'
)

fig.update_layout(
    title=dict(
        text='4. ¿Cuántas tabletas tiene en uso el negocio o actividad?',
        font=dict( size = 15, family='Arial' ),
        automargin=False,
        yref='paper'
    )
)

st.plotly_chart(fig)

st.divider()

data_device5 = data.groupby(['P976']).agg({
    'P976' : 'count'
})

fig = px.pie(
    data_device5,
    values='P976',
    names=['Si','No'],
    template='plotly_white'
    
)

fig.update_traces(hoverinfo='text+percent')
fig.update_layout(
    title=dict(
        text='4a. ¿Para su negocio o actividad utiliza el teléfono celular?',
        font=dict( size = 15, family='Arial' ),
        automargin=False,
        yref='paper'
    )
)
st.plotly_chart(fig)

st.divider()

data_device6 = data.groupby(['P978']).count()
data_device6 = data_device2.iloc[~data_device2.index.isin([0])]

fig = px.bar(
    data_device6,
    y='P978',
    template='plotly'
)

fig.update_layout(
    title=dict(
        text='5. ¿Cuántos teléfonos celulares inteligentes (Smartphone) tiene en uso el negocio o actividad?',
        font=dict( size = 15, family='Arial' ),
        automargin=False,
        yref='paper'
    )
)

st.plotly_chart(fig)

st.divider()

data_device7 = data.groupby(['P979']).count()
data_device7 = data_device2.iloc[~data_device2.index.isin([0])]

fig = px.bar(
    data_device6,
    y='P979',
    template='plotly'
)

fig.update_layout(
    title=dict(
        text='5a. ¿Cuántos teléfonos celular convencional tiene en uso el negocio o actividad?',
        font=dict( size = 15, family='Arial' ),
        automargin=False,
        yref='paper'
    )
)

st.plotly_chart(fig)
st.divider()

data_device8 = data.groupby(['P994']).agg({
    'P994' : 'count'
})

fig = px.pie(
    data_device8,
    values='P994',
    names=['Es muy costoso','No se necesita','El personal no sabe usarlo'],
    template='plotly_white'
    
)

fig.update_traces(hoverinfo='text+percent')
fig.update_layout(
    title=dict(
        text='6. ¿Cuál es la principal razón por la cual el negocio o actividad no tiene en uso computador <br>(PC, portátil), tableta, Smartphone?',
        font=dict( size = 15, family='Arial' ),
        automargin=False,
        yref='paper'
    )
)
st.plotly_chart(fig)
st.header('',divider="blue")