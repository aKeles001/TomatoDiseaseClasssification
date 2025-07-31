import streamlit as st
from PIL import Image

st.set_page_config(page_title="Home Page", page_icon="🌿")


st.title("🌿 Plant Leaf Disease Classifier")
st.subheader("Detect and identify plant leaf diseases using deep learning.")


st.markdown("""
Welcome to the **Plant Leaf Disease Classifier** app! This tool uses a trained deep learning model to help identify potential diseases in plant leaves based on image analysis. Whether you're a farmer, botanist, or hobby gardener, this app can help you quickly detect leaf issues and take action early.

---

### 🌱 Features:
- Upload a clear image of a **plant leaf**
- Classify between **healthy leaves** and various **common plant diseases**
- Instant results with confidence scores
- Visual preview of your uploaded image

---

### 📸 How to Use:
1. Go to the **"Disease Detector"** page using the sidebar.
2. Upload a plant leaf image (JPG/PNG).
3. Click **"Classify"** to see the result.
4. Review the prediction and suggested label.

---

### ⚠️ Note:
- For best results, use well-lit, focused leaf images.
- This tool is for **informational purposes only** and not a replacement for expert agricultural advice.

---

### 🔬 About the Model:
The model is based on a fine-tuned deep convolutional neural network trained on a dataset of various plant species and disease types. It has been tested on thousands of images to ensure reliable performance.

---
""")
