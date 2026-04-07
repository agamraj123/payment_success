import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("payment_success_model.pkl")

# App Title
st.title("💳 Payment Success Analyzer")

st.write("Enter transaction amount to predict payment success")

# Input from user
amount = st.number_input("Transaction Amount (INR)", min_value=0.0)

# Prediction
if st.button("Predict Payment Status"):

    input_data = pd.DataFrame([[amount]], columns=["Amount (INR)"])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("✅ Payment will likely SUCCESS")
    else:
        st.error("❌ Payment may FAIL")
