import streamlit as st
import requests

#fastAPI endpoint
API_URL=""

st.set_page_config(
    page_title="House Price Prediction",
    layout="centered"
)

st.title("House Price Prediction")
st.write("predict house price using a Linear Regression model")

#user input
area=st.number_input("Area ( sqft)", min_value=300,max_value=5000, value=1200)
bedrooms=st.number_input("Bedrooms", min_value=1, max_value=10, value=2)

if st.button("Predict Price"):
    payload={
        "area":area,
        "bedrooms":bedrooms
    }
    try:
        response=requests.post(f"{API_URL}/predict", json=payload)
        
        if response.status_code==200:
            result=response.json()
            price=result.get("predicted_price")
            st.success(f"Estimated Price:Rs.{price:,.2f}")
        else:
            st.error("Prediction Failed .check API.")

    except requests.exceptions.ConnectionError:
        st.error("Cannot connect to FastAPI backend.Is it running?")