import streamlit as st
from PIL import Image
from ultralytics import YOLO
import numpy as np
import cv2
import tempfile
import os


model = YOLO("best.pt")
st.set_page_config(page_title="Trash Detection with YOLOv8", layout="centered")
st.title("Trash Object Detection Using YOLO")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # Read image
    img = Image.open(uploaded_file)

    # Convert to OpenCV format
    img_np = np.array(img.convert("RGB"))
    img_bgr = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)

    # Run prediction
    with st.spinner("Detecting trash..."):
        results = model.predict(img_bgr, conf=0.3)
        result_img = results[0].plot()  # prediction image as numpy array

    # Create two columns
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Uploaded Image")
        st.image(img, use_column_width=True)

    with col2:
        st.subheader("Detection Result")
        st.image(result_img[:, :, ::-1], use_column_width=True)  # BGR to RGB

