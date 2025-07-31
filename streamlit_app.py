import streamlit as st
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.resnet import preprocess_input

st.title("Tomato Leaf Disease Classification")

# Define class names and image size
class_names = [
    'Bacterial Spot', 'Early Blight', 'Healthy',
    'Late Blight', 'Septoria Leaf Spot', 'Yellow Leaf Curl Virus'
]
image_size = (224, 224)

# Load the model
model = load_model('/workspaces/TomatoDiseaseClasssification/model/model.h5')

# Prediction function
def predict_image(img: Image.Image, model, class_names, image_size):
    """Preprocesses and predicts class of image using model"""
    image_resized = image1.resize(image_size)
    image_array = np.array(image_resized)
    image_array = preprocess_input(image_array)
    image_array = np.expand_dims(image_array, axis=0)

    prediction = model.predict(image_array)[0]
    predicted_index = np.argmax(prediction)
    predicted_label = class_names[predicted_index]
    confidence = prediction[predicted_index] * 100

    return predicted_label, confidence

# Streamlit interface
image = st.file_uploader(":arrow_up_small: Upload a tomato leaf image", type=["jpg"])
col1, col2 = st.columns(2)

if st.button("Predict") and image is not None:
    image1 = Image.open(image).convert('RGB')
    col1.image(image1, caption="Uploaded Image", use_container_width=True)

    label, conf = predict_image(image1, model, class_names, image_size)

    col2.subheader("Prediction:")
    col2.write(f"**Class:** {label}")
    col2.write(f"**Confidence:** {conf:.2f}%")
