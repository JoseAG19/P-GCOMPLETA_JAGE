import streamlit as st
st.title("¿QUE ÉS IOT?")
import pandas as pd
from PIL import Image


st.title('Análisis de datos de Sensores TH')
image = Image.open('Analisis de datos.jpg')
st.image(image)

uploaded_file = st.file_uploader('Choose a file')
if uploaded_file is not None:
   df1=pd.read_csv(uploaded_file)
   st.write(df1)
   st.subheader('Estadísticos básicos de los sensores')
   st.dataframe(df1["humedad ESP32"].describe())
else:
 st.warning('Necesitas cargar un archivo csv excel.')
