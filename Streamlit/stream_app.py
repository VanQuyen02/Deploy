import streamlit as st
from PIL import Image
from models.catdog_predictor import Predictor
from config.catdog_cfg import ModelConfig
import sys
from pathlib import Path
import webbrowser
import threading
import os
sys.path.append(str(Path(__file__).parent))

# Initialize predictor
predictor = Predictor(
    model_name=ModelConfig.MODEL_NAME,
    model_weight=ModelConfig.MODEL_WEIGHT,
    device=ModelConfig.DEVICE
)


st.title("Cat vs Dog Classifier")

uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Classifying...")

    # Make prediction
    response = predictor.predict(uploaded_file)
    st.write(response)

