
# Importing Libraries

import streamlit as st
import pandas as pd
import joblib


# Page Configuration


st.set_page_config(
    page_title="AIML Model Predictor",
    page_icon="🤖",
    layout="centered"
)


# Load Models


linear_model = joblib.load("linear_regression_model.pkl")

logistic_model = joblib.load("logistic_regression_model.pkl")

knn_model = joblib.load("knn_classifier_model.pkl")

naive_bayes_model = joblib.load("naive_bayes_classifier_model.pkl")



# Load Preprocessors


linear_columns = joblib.load("linear_columns.pkl")

logistic_columns = joblib.load("logistic_columns.pkl")

knn_columns = joblib.load("knn_columns.pkl")

naive_bayes_columns = joblib.load("naive_bayes_columns.pkl")

knn_scaler = joblib.load("knn_scaler.pkl")




# Load Datasets


car_df = pd.read_csv("CarDetails.csv")

heart_df = pd.read_csv("heart.csv")



# Application Title


st.title("🤖 AIML Model Predictor")
st.write("Predict Car Price or Heart Disease using Machine Learning Models")



# Select Prediction Type

prediction_type = st.selectbox(
    "Select Prediction Type",
    (
        "Car Price Prediction",
        "Heart Disease Prediction"
    )
)



# Car Price Prediction


if prediction_type == "Car Price Prediction":

    st.subheader("Car Price Prediction")

    company = st.selectbox(
        "Company",
        sorted(car_df["Company"].unique())
    )

    model = st.selectbox(
        "Car Model",
        sorted(
            car_df[car_df["Company"] == company]["Name"].unique()
        )
    )

    year = st.number_input(
        "Manufacturing Year",
        min_value=int(car_df["Year"].min()),
        max_value=int(car_df["Year"].max()),
        value=int(car_df["Year"].median())
    )

    kms = st.number_input(
        "Kilometers Driven",
        min_value=0,
        value=50000
    )

    fuel = st.selectbox(
        "Fuel Type",
        sorted(car_df["Fuel"].unique())
    )

    predict_car = st.button("Predict Car Price")



# Heart Disease Prediction


else:

    st.subheader("Heart Disease Prediction")

    algorithm = st.selectbox(
        "Select Algorithm",
        (
            "Logistic Regression",
            "K-Nearest Neighbors",
            "Naive Bayes"
        )
    )

    age = st.number_input("Age", 1, 120, 40)

    sex = st.selectbox(
        "Sex",
        sorted(heart_df["Sex"].unique())
    )

    chest_pain = st.selectbox(
        "Chest Pain Type",
        sorted(heart_df["ChestPainType"].unique())
    )

    resting_bp = st.number_input(
        "Resting Blood Pressure",
        50,
        250,
        120
    )

    cholesterol = st.number_input(
        "Cholesterol",
        0,
        700,
        200
    )

    fasting_bs = st.selectbox(
        "Fasting Blood Sugar",
        sorted(heart_df["FastingBS"].unique())
    )

    resting_ecg = st.selectbox(
        "Resting ECG",
        sorted(heart_df["RestingECG"].unique())
    )

    max_hr = st.number_input(
        "Maximum Heart Rate",
        50,
        250,
        150
    )

    exercise_angina = st.selectbox(
        "Exercise Angina",
        sorted(heart_df["ExerciseAngina"].unique())
    )

    oldpeak = st.number_input(
        "Old Peak",
        value=1.0
    )

    st_slope = st.selectbox(
        "ST Slope",
        sorted(heart_df["ST_Slope"].unique())
    )

    predict_heart = st.button("Predict Heart Disease")



  
# Car Price Prediction


if prediction_type == "Car Price Prediction" and predict_car:

    input_data = pd.DataFrame({
        "Name": [model],
        "Company": [company],
        "Year": [year],
        "Kms_driven": [kms],
        "Fuel": [fuel]
    })

    input_data = pd.get_dummies(input_data)

    input_data = input_data.reindex(
        columns=linear_columns,
        fill_value=0
    )

    predicted_price = linear_model.predict(input_data)[0]

    st.success(f"Predicted Car Price : ₹ {predicted_price:,.2f}")



# Heart Disease Prediction


if prediction_type == "Heart Disease Prediction" and predict_heart:

    input_data = pd.DataFrame({
        "Age": [age],
        "Sex": [sex],
        "ChestPainType": [chest_pain],
        "RestingBP": [resting_bp],
        "Cholesterol": [cholesterol],
        "FastingBS": [fasting_bs],
        "RestingECG": [resting_ecg],
        "MaxHR": [max_hr],
        "ExerciseAngina": [exercise_angina],
        "Oldpeak": [oldpeak],
        "ST_Slope": [st_slope]
    })

    input_data = pd.get_dummies(input_data)
    print("Current Columns:")
    print(input_data.columns.tolist())

    print("\nSaved Columns:")
    print(logistic_columns)

    if algorithm == "Logistic Regression":

        input_data = input_data.reindex(
            columns=logistic_columns,
            fill_value=0
        )

        prediction = logistic_model.predict(input_data)[0]
        print("Input Data Columns:")
        print(input_data.columns.tolist())

        print("\nModel Expected Features:")
        print(logistic_model.feature_names_in_)

    elif algorithm == "K-Nearest Neighbors":

        input_data = input_data.reindex(
            columns=knn_columns,
            fill_value=0
        )

        input_data = knn_scaler.transform(input_data)

        prediction = knn_model.predict(input_data)[0]


    else:

        input_data = input_data.reindex(
            columns=naive_bayes_columns,
            fill_value=0
        )

        prediction = naive_bayes_model.predict(input_data)[0]


    if prediction == 1:
        st.error("Heart Disease Detected")
    else:
        st.success("No Heart Disease Detected")