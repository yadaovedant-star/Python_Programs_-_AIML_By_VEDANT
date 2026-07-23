# Import Libraries
import streamlit as st
import pandas as pd
import joblib

# Load dataset (only for dropdowns)
df = pd.read_csv("CarDetails.csv")

# Load trained model
model = joblib.load("car_price_model.pkl")

st.title("Car Price Prediction App")

# User inputs
year = st.number_input("Car Year", min_value=1990, max_value=2026, step=1)
kms = st.number_input("Kms Driven", min_value=0, step=100)

company = st.selectbox("Company", df["Company"].unique())
fuel = st.selectbox("Fuel Type", df["Fuel"].unique())
name = st.selectbox("Car Name", df["Name"].unique())

# Create input dataframe
input_df = pd.DataFrame([[year, kms, name, company, fuel]],
                        columns=["Year", "Kms_driven", "Name", "Company", "Fuel"])

# Dummy encode same as training
input_df = pd.get_dummies(input_df, columns=["Name", "Company", "Fuel"], drop_first=True)

# Align columns with training data
# IMPORTANT: load the column structure you saved earlier
columns = joblib.load("car_columns.pkl")
input_df = input_df.reindex(columns=columns, fill_value=0)

# Predict
if st.button("Predict Price"):
    prediction = model.predict(input_df)[0]
    st.success(f"Predicted Price: ₹ {int(prediction)}")
