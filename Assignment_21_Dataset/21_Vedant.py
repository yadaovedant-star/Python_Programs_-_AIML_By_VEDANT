# Question 1: Import Required Libraries

import streamlit as st
import pandas as pd
import joblib


# Question 2: Load Model and Preprocessing Objects

model = joblib.load("LR_ford_car.pkl")
scaler = joblib.load("scaler.pkl")
encoded_columns = joblib.load("columns.pkl")


# Question 3: Configure Streamlit Page

st.set_page_config(
    page_title="Ford Car Price Prediction",
    layout="centered"
)


# Question 4: Title and Description

st.title("Ford Car Price Prediction")

st.write("Enter the details below to predict the car price.")


# Question 5: Numerical Input Fields

year = st.number_input("Manufacturing Year", 1996, 2025, 2018)

mileage = st.number_input("Mileage", min_value=0, value=10000)

tax = st.number_input("Road Tax", min_value=0, value=150)

mpg = st.number_input("MPG", min_value=0.0, value=55.0)

engineSize = st.number_input("Engine Size", min_value=0.0, value=1.5)


# Question 6: Categorical Input Fields

model_name = st.selectbox(
    "Model",
    [
        " B-MAX",
        " C-MAX",
        " EcoSport",
        " Edge",
        " Escort",
        " Fiesta",
        " Focus",
        " Fusion",
        " Galaxy",
        " Grand C-MAX",
        " Grand Tourneo Connect",
        " KA",
        " Ka+",
        " Kuga",
        " Mondeo",
        " Mustang",
        " Puma",
        " Ranger",
        " S-MAX",
        " Streetka",
        " Tourneo Connect",
        " Tourneo Custom",
        " Transit Tourneo",
        "Focus"
    ]
)

transmission = st.selectbox(
    "Transmission",
    [
        "Automatic",
        "Manual",
        "Semi-Auto"
    ]
)

fuelType = st.selectbox(
    "Fuel Type",
    [
        "Petrol",
        "Diesel",
        "Hybrid",
        "Electric",
        "Other"
    ]
)


# Question 7: Predict Button

predict = st.button("Predict Price")


# Question 8: Create Input DataFrame and One-Hot Encoding

if predict:

    input_df = pd.DataFrame({

        "model": [model_name],
        "year": [year],
        "transmission": [transmission],
        "mileage": [mileage],
        "fuelType": [fuelType],
        "tax": [tax],
        "mpg": [mpg],
        "engineSize": [engineSize]

    })

    input_encoded = pd.get_dummies(input_df)

    input_encoded = input_encoded.reindex(
        columns=encoded_columns,
        fill_value=0
    )


# Question 9: Feature Scaling and Prediction

    numeric_columns = [
        "year",
        "mileage",
        "tax",
        "mpg",
        "engineSize"
    ]

    input_encoded[numeric_columns] = scaler.transform(
        input_encoded[numeric_columns]
    )

    prediction = model.predict(input_encoded)


# Question 10: Display Prediction

    st.success(f"Predicted Car Price : £ {prediction[0]:,.2f}")