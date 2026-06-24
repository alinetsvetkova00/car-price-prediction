import streamlit as st
import requests

st.title("Car Price Prediction")

brand = st.text_input("Brand", "Ford")
model = st.text_input("Model", "F-150")
model_year = st.number_input("Model year", min_value=1970, max_value=2024, value=2020)
milage = st.number_input("Mileage", min_value=0, value=30000)
fuel_type = st.text_input("Fuel type", "Gasoline")
engine = st.text_input("Engine", "300.0HP 3.5L V6 Cylinder Engine Gasoline Fuel")
transmission = st.text_input("Transmission", "A/T")
ext_col = st.text_input("Exterior color", "Black")
int_col = st.text_input("Interior color", "Black")
accident = st.text_input("Accident", "None reported")
clean_title = st.text_input("Clean title", "Yes")

if st.button("Predict price"):
    data = {
        "brand": brand,
        "model": model,
        "model_year": model_year,
        "milage": milage,
        "fuel_type": fuel_type,
        "engine": engine,
        "transmission": transmission,
        "ext_col": ext_col,
        "int_col": int_col,
        "accident": accident,
        "clean_title": clean_title
    }

    response = requests.post("http://127.0.0.1:8000/predict", json=data)

    if response.status_code == 200:
        price = response.json()["price"]
        st.success(f"Predicted price: ${price:,.0f}")
    else:
        st.error("Prediction error")