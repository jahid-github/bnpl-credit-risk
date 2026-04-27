import streamlit as st
import pandas as pd
import joblib

model = joblib.load("models/bnpl_model.pkl")

st.set_page_config(page_title="BNPL Credit Risk App", layout="wide")

st.title("BNPL Credit Risk Prediction")
st.write("Predict customer default risk for Buy Now Pay Later fintech decisions.")

age = st.number_input("Age", min_value=18, max_value=100, value=30)
employment_type = st.selectbox("Employment Type", ["Salaried", "Self-employed", "Student", "Unemployed"])
monthly_income = st.number_input("Monthly Income", min_value=0.0, value=3000.0)
credit_score = st.number_input("Credit Score", min_value=300, max_value=900, value=650)
purchase_amount = st.number_input("Purchase Amount", min_value=0.0, value=500.0)
product_category = st.selectbox("Product Category", ["Electronics", "Fashion", "Furniture", "Grocery", "Travel"])
bnpl_installments = st.number_input("BNPL Installments", min_value=1, max_value=24, value=4)
repayment_delay_days = st.number_input("Repayment Delay Days", min_value=0, value=0)
missed_payments = st.number_input("Missed Payments", min_value=0, value=0)
app_usage_frequency = st.number_input("App Usage Frequency", min_value=0, value=10)
location = st.selectbox("Location", ["Urban", "Semi-Urban", "Rural"])
debt_to_income_ratio = st.number_input("Debt to Income Ratio", min_value=0.0, max_value=1.0, value=0.3)
customer_segment = st.selectbox("Customer Segment", ["Low", "Medium", "High"])

input_data = pd.DataFrame([{
    "age": age,
    "employment_type": employment_type,
    "monthly_income": monthly_income,
    "credit_score": credit_score,
    "purchase_amount": purchase_amount,
    "product_category": product_category,
    "bnpl_installments": bnpl_installments,
    "repayment_delay_days": repayment_delay_days,
    "missed_payments": missed_payments,
    "app_usage_frequency": app_usage_frequency,
    "location": location,
    "debt_to_income_ratio": debt_to_income_ratio,
    "customer_segment": customer_segment
}])

if st.button("Predict Risk"):
    probability = model.predict_proba(input_data)[0][1]

    if probability < 0.3:
        risk_level = "Low Risk"
    elif probability < 0.7:
        risk_level = "Medium Risk"
    else:
        risk_level = "High Risk"

    st.subheader("Prediction Result")
    st.write(f"Default Probability: **{probability:.2%}**")
    st.write(f"Risk Level: **{risk_level}**")
