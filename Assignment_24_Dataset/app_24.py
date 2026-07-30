import streamlit as st
import pandas as pd
import joblib
 
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
# Page Configuration

st.set_page_config(
    page_title="Unified Model Prediction System",
    page_icon="🤖",
    layout="wide"
)

# Dictionaries Saves Space

classification_models = {
    "Logistic Regression": "best_class_model.pkl",
    "Decision Tree": "modelDT.pkl",
    "Support Vector Machine": "modelSVM.pkl",
    "K-Nearest Neighbors": "modelKNN.pkl",
    "Naive Bayes": "modelNB.pkl"
}



regression_models = {
    "Linear Regression": "best_regi_model.pkl",
    "Decision Tree Regressor": "modelDTR.pkl",
    "Support Vector Regressor": "modelSVR.pkl",
    "K-Nearest Neighbors Regressor": "modelKNNR.pkl"
}




# Project Heading

st.title("🤖 Unified Model Prediction System")
st.caption("One Platform • Multiple Prediction Models")

st.divider()



# Sidebar Navigation

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Choose Prediction",
    [
        "🏠 Home",
        "❤️ Heart Disease Prediction",
        "🚗 Car Price Prediction",
        "ℹ️ About Project"
    ]
)




# Home Page

if page == "🏠 Home":

    st.header("Welcome")

    st.write("""
Welcome to the **Unified Model Prediction System**.

This application combines multiple Machine Learning models into one platform.

You can perform:

- ❤️ Heart Disease Prediction
- 🚗 Car Price Prediction

Select any module from the sidebar to begin.
""")



# About Page


elif page == "ℹ️ About Project":

    st.header("About Project")

    st.write("""
Unified Model Prediction System is a Machine Learning application
developed using Python, Streamlit and Scikit-Learn.

Features:

- Heart Disease Prediction
- Car Price Prediction
- Multiple Machine Learning Algorithms
- User Friendly Interface
- Author - Vedant Yadao
""")


# Navigation--------- Heart Disease Prediction --------- Selectbox  

elif page == "❤️ Heart Disease Prediction":

    st.header("❤️ Heart Disease Prediction")

    algorithm = st.selectbox(
        "Choose Prediction Algorithm",
        [
            "Logistic Regression",
            "Decision Tree",
            "Support Vector Machine",
            "K-Nearest Neighbors",
            "Naive Bayes"
        ]

    )
 
    # Loading Required Files

  

    class_columns = joblib.load(BASE_DIR / "class_columns.pkl")
    class_scaler = joblib.load(BASE_DIR / "class_scaler.pkl")


    # taking input from User 

    age = st.number_input("Age", min_value=15, max_value=100)

    resting_bp = st.number_input("Resting Blood Pressure", min_value=120)

    cholesterol = st.number_input("Cholesterol", min_value=120)

    fasting_bs = st.selectbox(
        "Fasting Blood Sugar",
        [0, 1]
    )

    max_hr = st.number_input("Maximum Heart Rate", min_value=110)

    oldpeak = st.number_input("Old Peak", value=1.0)

    sex = st.selectbox(
        "Sex",
        ["M", "F"]
    )   

    chest_pain = st.selectbox(
        "Chest Pain Type",
        ["ASY", "ATA", "NAP", "TA"]
    )

    resting_ecg = st.selectbox(
        "Resting ECG",
        ["LVH", "Normal", "ST"]
    )

    exercise_angina = st.selectbox(
        "Exercise Angina",
        ["Y", "N"]
    )

    st_slope = st.selectbox(
        "ST Slope",
        ["Down", "Flat", "Up"]
    )


    # Prediction Button

    if st.button("Predict Heart Dataset"):

        model = joblib.load(BASE_DIR / classification_models[algorithm])



        # Create all columns with 0
        input_data = dict.fromkeys(class_columns, 0)

    # Numerical Features
        input_data["Age"] = age
        input_data["RestingBP"] = resting_bp
        input_data["Cholesterol"] = cholesterol
        input_data["FastingBS"] = fasting_bs
        input_data["MaxHR"] = max_hr
        input_data["Oldpeak"] = oldpeak

    # One-Hot Encoding
        input_data[f"Sex_{sex}"] = 1

        input_data[f"ChestPainType_{chest_pain}"] = 1

        input_data[f"RestingECG_{resting_ecg}"] = 1



        if exercise_angina == "Y":

                input_data["ExerciseAngina_Y"] = 1

        else:

                input_data["ExerciseAngina_N"] = 1

        input_data[f"ST_Slope_{st_slope}"] = 1


        # Create DataFrame
        input_df = pd.DataFrame([input_data])


        # Arrange Columns
        input_df = input_df[class_columns]


        # Scale Data
        input_scaled = class_scaler.transform(input_df)


        # Prediction
        prediction = model.predict(input_scaled)


        # Result
        
        if prediction[0] == 1:
            st.error("❤️ Heart Disease Detected")

        else:
            st.success("💚 No Heart Disease Detected")
    
    

# Navigation--------- Car Price Prediction --------- Selectbox  

elif page == "🚗 Car Price Prediction":

    st.header("🚗 Car Price Prediction")

    algorithm = st.selectbox(
        "Choose Prediction Algorithm",
        [
            "Linear Regression",
            "Decision Tree Regressor",
            "Support Vector Regressor",
            "K-Nearest Neighbors Regressor"
        ]
    ) 

   

    regi_columns = joblib.load(BASE_DIR / "regi_columns.pkl")
    regi_scaler = joblib.load(BASE_DIR / "regi_scaler.pkl")

# Taking Input From User
    year = st.number_input("Year", min_value=1990, max_value=2026,value=2018)

    engine_size = st.number_input("Engine Size", min_value=0.5, max_value=10.0,value=2.0,step=0.1)

    mileage = st.number_input("Mileage", min_value=0.0,max_value=500000.0,value=50000.0)
    make = st.selectbox(
            "Make",
            ["Audi", "BMW", "Ford", "Honda", "Toyota"]
        )

    model_name = st.selectbox(
            "Model",
            ["Model A", "Model B", "Model C", "Model D", "Model E"]
        )

    fuel_type = st.selectbox(
            "Fuel Type",
            ["Diesel", "Electric", "Petrol"]
        )

    transmission = st.selectbox(
            "Transmission",
            ["Automatic", "Manual"]
        )       
    
        
    if st.button("Predict Car Price"):



    # Load Selected Model
        model = joblib.load(BASE_DIR / regression_models[algorithm])

    # Create Empty Dictionar
        input_data = dict.fromkeys(regi_columns, 0)

    # Fill Numerical Features
        input_data["Year"] = year
        input_data["Engine Size"] = engine_size
        input_data["Mileage"] = mileage

    # One-Hot Encode Categorical Features
        input_data[f"Make_{make}"] = 1
        input_data[f"Model_{model_name}"] = 1
        input_data[f"Fuel Type_{fuel_type}"] = 1
        input_data[f"Transmission_{transmission}"] = 1

    # Convert Dictionary to DataFrame
        input_df = pd.DataFrame([input_data])

    # Arrange Columns in Correct Order
        input_df = input_df[regi_columns]
# Predict Car Price

        if algorithm in ["Linear Regression", "Decision Tree Regressor"]:

            # These models were trained WITHOUT scaling
            prediction = model.predict(input_df)

        else:

            # SVR and KNN were trained WITH scaling
            input_scaled = regi_scaler.transform(input_df)
            prediction = model.predict(input_scaled)

        # Display Result
        st.success(f"💰 Predicted Car Price: ₹{prediction[0]:,.2f}")