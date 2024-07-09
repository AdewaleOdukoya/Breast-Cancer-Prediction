import streamlit as st
import sklearn
import joblib
import numpy as np

# Set page configuration
st.set_page_config(
    page_title="BCP APP",
    page_icon="😇",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Load the model
model = joblib.load(r"/Users/adewaleodukoya/Personal YT Projects/Aptech final Project/BreastCancerProjectapt.pkl")

# Custom CSS for styling
st.markdown(
    """
    <style>
    .main-title {
        font-size: 50px;
        color: #2c3e50;
        text-align: center;
        font-weight: bold;
        margin-bottom: 50px;
    }
    .input-label {
        font-size: 20px;
        font-weight: bold;
        color: #34495e;
        margin-top: 10px;
    }
    .predict-button {
        background-color: #3498db;
        color: white;
        font-size: 20px;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        margin-top: 20px;
    }
    .predict-button:hover {
        background-color: #2980b9;
    }
    .result-container {
        margin-top: 30px;
        text-align: center;
        font-size: 25px;
        font-weight: bold;
        color: #16a085;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Page title
st.markdown('<div class="main-title">Breast Cancer Prediction</div>', unsafe_allow_html=True)

# Input containers
inputs = {
    "mean_radius": "Mean Radius",
    "mean_perimeter": "Mean Perimeter",
    "mean_area": "Mean Area",
    "mean_compactness": "Mean Compactness",
    "mean_concavity": "Mean Concavity",
    "mean_concave_points": "Mean Concave Points",
    "radius_se": "Radius SE",
    "perimeter_se": "Perimeter SE",
    "area_se": "Area SE",
    "worst_radius": "Worst Radius",
    "worst_perimeter": "Worst Perimeter",
    "worst_area": "Worst Area",
    "worst_compactness": "Worst Compactness",
    "worst_concavity": "Worst Concavity",
    "worst_concave_points": "Worst Concave Points"
}

input_values = {}

for key, label in inputs.items():
    st.markdown(f"<div class='input-label'>{label}</div>", unsafe_allow_html=True)
    input_values[key] = st.number_input(
        "", 
        min_value=0.1, max_value=1000.0, value=10.0, 
        key=key, 
        format="%.2f"
    )

# Predict button
if st.button("Predict", key="predict"):
    input_data = np.array([[input_values[key] for key in inputs]])

    prediction = model.predict(input_data)

    # Map prediction back to original labels
    predicted_label = 'M' if prediction[0] == 1 else 'B'
   
    st.markdown(
        f"<div class='result-container'>Predicted Breast Cancer Status: {predicted_label}</div>", 
        unsafe_allow_html=True
    )

