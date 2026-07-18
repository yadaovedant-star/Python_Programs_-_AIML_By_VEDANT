# Question 1: Import Required Libraries

import streamlit as st
import pandas as pd
import joblib


# Question 2: Load Model and Preprocessing Objects

model = joblib.load("LR_mobile.pkl")
scaler = joblib.load("scaler_mobile.pkl")
encoded_columns = joblib.load("columns_mobile.pkl")


# Question 3: Configure Streamlit Page

st.set_page_config(
    page_title="Mobile Price Prediction",
    layout="centered"
)


# Question 4: Title and Description

st.title("Mobile Price Prediction")

st.write("Enter the mobile details below to predict its selling price.")


# Question 5: Numerical Input Fields

rating = st.number_input(
    "Rating",
    min_value=0.0,
    max_value=5.0,
    value=4.2,
    step=0.1
)

no_of_ratings = st.number_input(
    "Number of Ratings",
    min_value=0,
    value=1000
)

total_reviews = st.number_input(
    "Total Reviews",
    min_value=0,
    value=100
)


# Question 6: Categorical Input Fields

company = st.selectbox(
    "Company",
    [
        "APPLE",
        "SAMSUNG",
        "realme",
        "OnePlus",
        "POCO",
        "vivo",
        "Nothing",
        "Google",
        "MOTOROLA",
        "OPPO",
        "IQOO",
        "Xiaomi",
        "REDMI"
    ]
)

ram = st.selectbox(
    "RAM Size",
    [
        "2 GB",
        "4 GB",
        "6 GB",
        "8 GB",
        "12 GB",
        "16 GB"
    ]
)

rom = st.selectbox(
    "Storage",
    [
        "32 GB",
        "64 GB",
        "128 GB",
        "256 GB",
        "512 GB",
        "1 TB"
    ]
)


# Question 7: Predict Button

predict = st.button("Predict Price")


# Question 8: Create Input DataFrame and Perform One-Hot Encoding

if predict:

    try:

        input_df = pd.DataFrame({
            "Company": [company],
            "Rating": [rating],
            "No_of_ratings": [no_of_ratings],
            "TotalReviwes": [total_reviews],
            "RamSize": [ram],
            "RomSize": [rom]
        })

        input_encoded = pd.get_dummies(input_df)

        input_encoded = input_encoded.reindex(
            columns=encoded_columns,
            fill_value=0
        )


# Question 9: Feature Scaling and Prediction

        input_scaled = scaler.transform(input_encoded)

        prediction = model.predict(input_scaled)

        st.success(
            f"Predicted Mobile Price : ₹ {prediction[0]:,.2f}"
        )

    except Exception as e:

        st.error(f"Error : {e}")


# Question 10: Complete Streamlit Application
   #  Local URL: http://localhost:8501
  # Network URL: http://10.97.1.55:8501