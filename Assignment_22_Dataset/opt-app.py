import streamlit as st
import pandas as pd
import joblib

model = joblib.load("diabetes_Model.pkl")
columns = joblib.load("columns_Diabetes.pkl")

st.title("Diabetes Prediction App")

gender = st.selectbox("Gender", ["Female", "Male"])
gender = 1 if gender == "Male" else 0

age = st.number_input("Age", 1, 120, 30)

hypertension = st.selectbox("Hypertension", ["No", "Yes"])
hypertension = 1 if hypertension == "Yes" else 0

heart_disease = st.selectbox("Heart Disease", ["No", "Yes"])
heart_disease = 1 if heart_disease == "Yes" else 0

smoking_history = st.selectbox(
    "Smoking History",
    ["never", "former", "current"]
)

smoking_map = {
    "never": 0,
    "former": 1,
    "current": 2
}

smoking = smoking_map[smoking_history]

bmi = st.number_input("BMI", 10.0, 60.0, 25.0)

HbA1c = st.number_input("HbA1c Level", 3.0, 15.0, 5.5)

blood_glucose_level = st.number_input(
    "Blood Glucose Level",
    50,
    300,
    120
)

input_data = pd.DataFrame([[
    gender,
    age,
    hypertension,
    heart_disease,
    smoking,
    bmi,
    HbA1c,
    blood_glucose_level
]], columns=columns)

if st.button("Predict"):

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("Diabetes Detected")
    else:
        st.success("No Diabetes Detected")