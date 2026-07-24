import streamlit as st
import pandas as pd
import joblib

model = joblib.load("LR_model.pkl")
scaler = joblib.load("scaler.pkl")
encoded_columns = joblib.load("columns.pkl")

st.set_page_config(
    page_title="Diamond Price Predictor",
    layout="centered"
)

st.title("Diamond Price Predictor")
st.write("Enter the diamond details below to predict its price.")

carat = st.number_input("Carat", min_value=0.0, value=1.0)
depth = st.number_input("Depth", min_value=0.0, value=61.0)
table = st.number_input("Table", min_value=0.0, value=55.0)
x = st.number_input("Length (x)", min_value=0.0, value=5.0)
y = st.number_input("Width (y)", min_value=0.0, value=5.0)
z = st.number_input("Height (z)", min_value=0.0, value=3.0)

cut = st.selectbox(
    "Cut",
    ["Fair", "Good", "Very Good", "Premium", "Ideal"]
)
color = st.selectbox(
    "Color",
    ["D", "E", "F", "G", "H", "I", "J"]
)
clarity = st.selectbox(
    "Clarity",
    ["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"]
)

predict = st.button("Predict Price")
if predict:
    input_data = pd.DataFrame({
        "carat": [carat],
        "cut": [cut],
        "color": [color],
        "clarity": [clarity],
        "depth": [depth],
        "table": [table],
        "x": [x],
        "y": [y],
        "z": [z]
    })
    input_encoded = pd.get_dummies(input_data)
    input_encoded = input_encoded.reindex(
        columns=encoded_columns,
        fill_value=0
    )
    numerical_columns = [
        "carat",
        "depth",
        "table",
        "x",
        "y",
        "z"
    ]
    input_encoded[numerical_columns] = scaler.transform(
        input_encoded[numerical_columns]
    )
    prediction = model.predict(input_encoded)   
    prediction = model.predict(input_encoded)
    st.success(f"Predicted Diamond Price: ₹{prediction[0]:,.2f}")