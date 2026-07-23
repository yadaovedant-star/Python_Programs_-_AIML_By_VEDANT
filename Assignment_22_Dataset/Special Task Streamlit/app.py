# Import Libraries
import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# Load dataset
df = pd.read_csv("CarDetails.csv")

# Remove unwanted index column if present
if "Unnamed: 0" in df.columns:
    df = df.drop("Unnamed: 0", axis=1)

# Create input and output
X = df.drop("Price", axis=1)
y = df["Price"]

# Convert categorical columns into numbers
X = pd.get_dummies(X, columns=["Name", "Company", "Fuel"], drop_first=True)

# Train Model
model = LinearRegression()
model.fit(X, y)

st.title("Car Price Prediction App")

# User inputs
year = st.number_input(
    "Car Year",
    min_value=1990,
    max_value=2026,
    step=1
)

kms = st.number_input(
    "Kms Driven",
    min_value=0,
    step=100
)

company = st.selectbox(
    "Company",
    df["Company"].unique()
)

fuel = st.selectbox(
    "Fuel Type",
    df["Fuel"].unique()
)

name = st.selectbox(
    "Car Name",
    df["Name"].unique()
)

# Create input dataframe
input_df = pd.DataFrame(
    [[year, kms, name, company, fuel]],
    columns=["Year", "Kms_driven", "Name", "Company", "Fuel"]
)

# Convert categorical columns into numbers
input_df = pd.get_dummies(
    input_df,
    columns=["Name", "Company", "Fuel"],
    drop_first=True
)

# Make input columns same as training columns
input_df = input_df.reindex(
    columns=X.columns,
    fill_value=0
)

# Predict Price
if st.button("Predict Price"):
    prediction = model.predict(input_df)[0]

    st.success(
        f"Predicted Price: ₹ {int(prediction)}"
    )