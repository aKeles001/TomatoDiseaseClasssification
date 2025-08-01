import streamlit as st
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.resnet import preprocess_input

st.title("Bell Pepper Leaf Disease Classification")

# Define class names and image size
class_names = [
    'Bacterial Spot',
    'Healthy'
]
image_size = (224, 224)

# Load the model
model = load_model('model/model_BellPepper.h5')

# Prediction function
def predict_image(img: Image.Image, model, class_names, image_size):
    """Preprocesses and predicts class of image using model"""
    image_resized = img.resize(image_size) # Use img instead of image1
    image_array = np.array(image_resized)
    image_array = preprocess_input(image_array)
    image_array = np.expand_dims(image_array, axis=0)

    prediction = model.predict(image_array)[0][0] # Get the single output value

    # For binary classification with sigmoid output
    if prediction >= 0.5:
        predicted_label = class_names[1] # Bacterial Spot
        confidence = prediction * 100
    else:
        predicted_label = class_names[0] # Healthy
        confidence = (1 - prediction) * 100 # Confidence for the Healthy class

    return predicted_label, confidence

# Streamlit interface
image = st.file_uploader(":arrow_up_small: Upload a bell pepper leaf image", type=["jpg"])
col1, col2 = st.columns(2)

if st.button("Predict") and image is not None:
    image1 = Image.open(image).convert('RGB')
    col1.image(image1, caption="Uploaded Image", use_container_width=True)

    label, conf = predict_image(image1, model, class_names, image_size)

    col2.subheader("Prediction:")
    col2.write(f"**Class:** {label}")
    col2.write(f"**Confidence:** {conf:.2f}%")