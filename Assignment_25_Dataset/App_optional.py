from pathlib import Path
import joblib
import pandas as pd

BASE_DIR = Path(__file__).parent

model = joblib.load(BASE_DIR / "best_model.pkl")
feature_columns = joblib.load(BASE_DIR / "columns.pkl")

df = pd.read_csv(BASE_DIR / "Breast_Cure.csv")

# Page Configuration

import streamlit as st

st.set_page_config(
    page_title="Breast Cancer Predictor",
    page_icon="🩺",
    layout="centered"
)

st.title("🩺 Breast Cancer Prediction")
st.write("Predict whether the tumor is Benign or Malignant using XGBoost.")

st.subheader("Enter Tumor Details")

radius_mean = st.number_input(
    "Radius Mean",
    min_value=0.0,
    value=float(df["radius_mean"].mean())
)

texture_mean = st.number_input(
    "Texture Mean",
    min_value=0.0,
    value=float(df["texture_mean"].mean())
)

perimeter_mean = st.number_input(
    "Perimeter Mean",
    min_value=0.0,
    value=float(df["perimeter_mean"].mean())
)

area_mean = st.number_input(
    "Area Mean",
    min_value=0.0,
    value=float(df["area_mean"].mean())
)

concavity_mean = st.number_input(
    "Concavity Mean",
    min_value=0.0,
    value=float(df["concavity_mean"].mean())
)

concave_points_mean = st.number_input(
    "Concave Points Mean",
    min_value=0.0,
    value=float(df["concave points_mean"].mean())
)

predict = st.button("Predict")

if predict:

    input_data = pd.DataFrame({
        "radius_mean": [radius_mean],
        "texture_mean": [texture_mean],
        "perimeter_mean": [perimeter_mean],
        "area_mean": [area_mean],
        "concavity_mean": [concavity_mean],
        "concave points_mean": [concave_points_mean]
    })

    input_data = input_data.reindex(
        columns=feature_columns,
        fill_value=0
    )

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("Prediction : Malignant (Cancerous)")
    else:
        st.success("Prediction : Benign (Non-Cancerous)")

    st.divider()
    st.caption("Made by Vedant Yadao")