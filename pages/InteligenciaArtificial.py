import streamlit as st
import cv2
import numpy as np
#from PIL import Image
from PIL import Image as Image, ImageOps as ImagOps
from keras.models import load_model

model = load_model('keras_model.h5')
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

st.title("Reconocimiento de Imágenes")

img_file_buffer = st.camera_input("Toma una Foto")

if img_file_buffer is not None:
    # To read image file buffer with OpenCV:
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
   #To read image file buffer as a PIL Image:
    img = Image.open(img_file_buffer)

    newsize = (224, 224)
    img = img.resize(newsize)
    # To convert PIL Image to numpy array:
    img_array = np.array(img)

    # Normalize the image
    normalized_image_array = (img_array.astype(np.float32) / 127.0) - 1
    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference
    prediction = model.predict(data)
    print(prediction)
    if prediction[0][0]>0.4:
      st.header('Asco, con Probabilidad: '+str( prediction[0][0]) )
    if prediction[0][1]>0.4:
      st.header('Tristeza, con Probabilidad: '+str( prediction[0][1]))
    if prediction[0][2]>0.4:
      st.header('Felicidad, con Probabilidad: '+str( prediction[0][2]))
    if prediction[0][3]>0.4:
      st.header('Seriedad, con Probabilidad: '+str( prediction[0][3]))
    if prediction[0][4]>0.4:
      st.header('Confianza, con Probabilidad: '+str( prediction[0][4]))
    if prediction[0][5]>0.4:
      st.header('Enojo, con Probabilidad: '+str( prediction[0][5]))

