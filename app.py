import streamlit as st
import pandas as pd
import joblib

model = joblib.load("payment_success_model.pkl")

st.title("Payment Success Analyzer")

amount = st.number_input("Transaction Amount (INR)", min_value=0.0)

if st.button("Predict"):

    input_data = pd.DataFrame([[amount]], columns=["Amount (INR)"])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("Payment will likely SUCCESS")
    else:
        st.error("Payment may FAIL")
