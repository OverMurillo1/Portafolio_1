import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from st_pages import Page,add_page_title, show_pages



show_pages(
    [
        Page('app.py','Inicio'),
        Page('app_device.py','Modulo Dispositivos'),
        Page('app_internet.py','Modulo Conexion')
    ]
)

data = pd.read_csv('Modulo_TIC.csv', low_memory=False)

st.header("Encuesta de Micronegocios - 2022", divider="rainbow")
st.subheader("Modulo TIC")

st.markdown('''
            1. ¿Para su negocio o actividad utiliza alguno de los siguientes dispositivos electrónicos? Computador(es) o Tableta(s) portátil(es)
            2. ¿Cuántos computadores de escritorio tiene en uso el negocio o actividad?
            3. ¿Cuántos computadores portátiles tiene en uso el negocio o actividad?
            4. ¿Cuántas tabletas tiene en uso el negocio o actividad?
            4a. ¿Para su negocio o actividad utiliza el teléfono celular?
            5. ¿Cuántos teléfonos celulares inteligentes (Smartphone) tiene en uso el negocio o actividad?
            5a. ¿Cuántos teléfonos celular convencional tiene en uso el negocio o actividad?
            6. ¿Cuál es la principal razón por la cual el negocio o actividad no tiene en uso computador (PC, portátil), tableta, Smartphone?
            7. El negocio o actividad tiene página web o presencia en un sitio web?
            8. ¿El negocio o actividad tiene presencia en redes sociales (Facebook,Twitter, etc.)?
            9. ¿Este negocio o actividad tiene acceso o utiliza el servicio de internet?
            10. ¿Utiliza internet con conexión dentro del negocio o donde desarrolla su actividad? 
            11. ¿Qué tipo de conexión utiliza principalmente el negocio o actividad para acceder a internet?
            12. ¿Cuál es la principal razón por la cual el negocio o actividad no utiliza internet?
            13. Del total del personal ocupado del negocio o actividad,¿cuántos utilizan internet para el desarrollo de sus actividades?
            ''')

st.write('Raw Data')
st.dataframe(data)