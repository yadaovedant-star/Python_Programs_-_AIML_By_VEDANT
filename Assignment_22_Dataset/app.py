import streamlit as st

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
    st.write("Prediction")