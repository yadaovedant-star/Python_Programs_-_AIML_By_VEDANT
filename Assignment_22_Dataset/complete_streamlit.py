import streamlit as st
import pandas as pd
import joblib

model = joblib.load("heart_model.pkl")
columns = joblib.load("columns.pkl")

st.title("Heart Disease Prediction")

age = st.number_input("Age")
sex = st.selectbox("Sex", ["M", "F"])
cp = st.selectbox("Chest Pain", ["ATA", "NAP", "ASY", "TA"])
bp = st.number_input("Resting BP")
chol = st.number_input("Cholesterol")
fbs = st.selectbox("Fasting BS", [0, 1])
ecg = st.selectbox("ECG", ["Normal", "ST", "LVH"])
hr = st.number_input("Max HR")
angina = st.selectbox("Exercise Angina", ["Y", "N"])
oldpeak = st.number_input("Oldpeak")
slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"])

if st.button("Predict"):
    data = {
        "Age": age,
        "Sex": sex,
        "ChestPainType": cp,
        "RestingBP": bp,
        "Cholesterol": chol,
        "FastingBS": fbs,
        "RestingECG": ecg,
        "MaxHR": hr,
        "ExerciseAngina": angina,
        "Oldpeak": oldpeak,
        "ST_Slope": slope
    }

    df = pd.DataFrame([data])

    df = pd.get_dummies(df)

    df = df.reindex(columns=columns, fill_value=0)

    ans = model.predict(df)

    if ans[0] == 1:
        st.error("Heart Disease : Yes")
    else:
        st.success("Heart Disease : No")