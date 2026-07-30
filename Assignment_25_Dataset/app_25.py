import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# Base Directory
BASE_DIR = Path(__file__).resolve().parent

# Load Model and Files
model = joblib.load(BASE_DIR / "bank_churn_model.pkl")

country_encoder = joblib.load(BASE_DIR / "country_encoder.pkl")
gender_encoder = joblib.load(BASE_DIR / "gender_encoder.pkl")

# Title
st.title("🏦 Bank Customer Churn Prediction")

st.write("Enter the customer details below.")

# Inputs
credit_score = st.number_input(
    "Credit Score",
    min_value=300,
    max_value=900,
    value=600
)

country = st.selectbox(
    "Country",
    country_encoder.classes_
)

gender = st.selectbox(
    "Gender",
    gender_encoder.classes_
)

age = st.number_input(
    "Age",
    min_value=18,
    max_value=100,
    value=35
)

tenure = st.number_input(
    "Tenure",
    min_value=0,
    max_value=10,
    value=5
)

balance = st.number_input(
    "Balance",
    min_value=0.0,
    value=50000.0
)

products_number = st.number_input(
    "Number of Products",
    min_value=1,
    max_value=4,
    value=1
)

credit_card = st.selectbox(
    "Has Credit Card",
    [0, 1]
)

active_member = st.selectbox(
    "Active Member",
    [0, 1]
)

estimated_salary = st.number_input(
    "Estimated Salary",
    min_value=0.0,
    value=50000.0
)

if st.button("Predict"):

    country = country_encoder.transform([country])[0]
    gender = gender_encoder.transform([gender])[0]

    input_data = pd.DataFrame({
        "credit_score": [credit_score],
        "country": [country],
        "gender": [gender],
        "age": [age],
        "tenure": [tenure],
        "balance": [balance],
        "products_number": [products_number],
        "credit_card": [credit_card],
        "active_member": [active_member],
        "estimated_salary": [estimated_salary]
    })

   

    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)

    stay_prob = probability[0][0] * 100
    churn_prob = probability[0][1] * 100

    st.write(f"**Stay Probability:** {stay_prob:.2f}%")
    st.write(f"**Churn Probability:** {churn_prob:.2f}%")

    if prediction[0] == 1:
        st.error("🔴 Customer is likely to Churn.")
    else:
        st.success("🟢 Customer is likely to Stay.")