import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import torch
import numpy as np

# Set page configuration
st.set_page_config(page_title="Object Detector", layout="centered")

# Load the YOLOv5 model
@st.cache(allow_output_mutation=True)
def load_model():
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
    return model

model = load_model()

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: #1e1e1e;
        color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
    }
    .title {
        text-align: center;
        font-family: Arial, sans-serif;
        color: #f0f2f6;
    }
    .upload-box {
        text-align: center;
        padding: 10px;
        border: 2px dashed #aaa;
        border-radius: 10px;
        background-color: #333;
    }
    .result-box {
        background-color: #333;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
    }
    .detected-label {
        font-weight: bold;
        color: #1f77b4;
    }
    .footer {
        text-align: center;
        padding: 20px;
        color: #888;
    }
    </style>
""", unsafe_allow_html=True)

# Main container
with st.container():
    st.markdown("<h1 class='title'>Object Detector</h1>", unsafe_allow_html=True)

    # Image upload widget
    st.markdown("<div class='upload-box'>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    st.markdown("</div>", unsafe_allow_html=True)

    if st.button('Analyze Image'):
        if uploaded_file is not None:
            # Load and display the image
            image = Image.open(uploaded_file)
            st.image(image, caption='Uploaded Image.', use_column_width=True)

            st.write("Analyzing...")

            # Perform inference
            results = model(image)

            # Extract results
            pred_classes = results.pred[0][:, -1].cpu().numpy()  # Extract class indices
            pred_scores = results.pred[0][:, 4].cpu().numpy()  # Extract confidence scores
            pred_boxes = results.pred[0][:, :4].cpu().numpy()  # Extract bounding boxes

            # Draw annotated image with numbered labels
            annotated_image = image.copy()
            draw = ImageDraw.Draw(annotated_image)
            font = ImageFont.load_default()

            # Display results with labels, confidence scores, and numbering
            st.markdown("<div class='result-box'>", unsafe_allow_html=True)
            st.write("Objects detected in the image:")
            for i, (class_idx, score, box) in enumerate(zip(pred_classes, pred_scores, pred_boxes)):
                label = model.names[int(class_idx)]
                draw.rectangle(((box[0], box[1]), (box[2], box[3])), outline="green", width=2)
                draw.text((box[0], box[1]), text=f"{i+1}. {label} ({score:.2f})", fill="green", font=font)
                st.markdown(f"<span style='color:#f0f2f6'>{i+1}. <span class='detected-label'>{label}</span> (Confidence: {score:.2f})</span>", unsafe_allow_html=True)

            st.markdown("</div>", unsafe_allow_html=True)

            # Display annotated image
            st.image(annotated_image, caption='Annotated Image.', use_column_width=True)


