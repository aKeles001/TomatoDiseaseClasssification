import streamlit as st
from PIL import Image
from tensorflow.keras.models import load_model

st.title("Disease Classification")

model = load_model('/model.h5')

image = st.file_uploader(":arrow_up_small:  ", type=["png", "jpg", "jpeg"])
col1, col2 = st.columns(2)


if st.button("Predict"):
    image1 = Image.open(image)
    col1.image(image)