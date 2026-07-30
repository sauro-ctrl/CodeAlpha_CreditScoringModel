import joblib
import pandas as pd
import streamlit as st


model = joblib.load("D:/intern/Model/Decision_tree_Pipeline.pkl")

st.title("Credit Eligibility Predictor")

st.sidebar.title("About")

st.sidebar.info("""
This application predicts an applicant's creditworthiness
using a Decision Tree machine learning model.

Author~
Saurodeep De
""")

age = st.number_input(
    "Age(years)",
    min_value=15,
    max_value=100,
    value=35,
    step=1
)

annual_income = st.number_input(
    "Annual Income (INR)",
    value=26000
)

experience = st.number_input(
    "Employment Years",
    value=6
)

monthly_debt = st.number_input(
    "Monthly Debt",
    value=2100
)

debt_to_income = st.number_input(
    "Debt to Income",
    value=0.25
)

credit_utilisation = st.number_input(
    "Credit Utilisation",
    value=45
)

late_payments = st.number_input(
    "Late Payments",
    value=1
)

credit_history = st.number_input(
    "Credit History (Years)",
    value=8
)

credit_accounts = st.number_input(
    "Credit Accounts",
    value=45
)

loan_amount = st.number_input(
    "Loan Amount",
    value=50000
)

mapping = {
    "No": 0,
    "Yes": 1
}

previous_defaults = st.selectbox(
    "Has the applicant defaulted on a loan before?",
    list(mapping.keys())
)
previous_defaults = mapping[previous_defaults]

payment_history_score = st.number_input(
    "Payment History Score (%)",
    min_value=0,
    max_value=100,
    value= 85
)

home_ownership = st.selectbox(
    "Home Ownership",
    ["Own","Rent","Mortgage"]
)

marital_status = st.selectbox(
    "Marital Status",
    ["Married","Single"]
)

education_level = st.selectbox(
    "Education Level",
    ["HighSchool","Bachelor","Master","PhD"]
)

if st.button("Predict Creditworthiness"):

    pred = pd.DataFrame({
    "Age": [age],
    "Annual_Income": [annual_income],
    "Employment_Years": [experience],
    "Monthly_Debt": [monthly_debt],
    "Debt_to_Income": [debt_to_income],
    "Credit_Utilization": [credit_utilisation],
    "Late_Payments": [late_payments],
    "Credit_History_Years": [credit_history],
    "Credit_Accounts": [credit_accounts],
    "Loan_Amount": [loan_amount],
    "Previous_Defaults": [previous_defaults],
    "Payment_History_Score": [payment_history_score],
    "Home_Ownership": [home_ownership],
    "Marital_Status": [marital_status],
    "Education_Level": [education_level]})

    predicted = model.predict(pred)[0]
    co = "demo"

    if predicted == 0:
        st.error("Prediction: The applicant is **Not Creditworthy**.")

    else:
        st.success("Prediction: The applicant is **Creditworthy**.")

#st.success(f"Prediction: The applicant is **{co}**.")