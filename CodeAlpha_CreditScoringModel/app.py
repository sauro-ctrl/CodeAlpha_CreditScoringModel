import joblib
import pandas as pd
import streamlit as st


# Page setup
st.set_page_config(
    page_title="Credit Eligibility Predictor",
    page_icon="💳",
    layout="centered"
)


# Load trained model
model = joblib.load("Model/Decision_tree_Pipeline.pkl")


# Title
st.title("💳 Credit Eligibility Predictor")

st.write(
    "Enter the applicant's details below to predict "
    "whether they are creditworthy."
)

st.divider()


# Sidebar
st.sidebar.title("ℹ️ About")

st.sidebar.info("""
This application predicts an applicant's creditworthiness
using a Decision Tree machine learning model.

**Author:** Saurodeep De
""")


# ---------------- PERSONAL DETAILS ----------------

st.subheader("👤 Personal Details")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input(
        "Age (Years)",
        min_value=18,
        max_value=100,
        value=35
    )

    experience = st.number_input(
        "Employment Years",
        min_value=0,
        value=6
    )

    marital_status = st.selectbox(
        "Marital Status",
        ["Married", "Single"]
    )

with col2:
    education_level = st.selectbox(
        "Education Level",
        ["HighSchool", "Bachelor", "Master", "PhD"]
    )

    home_ownership = st.selectbox(
        "Home Ownership",
        ["Own", "Rent", "Mortgage"]
    )


st.divider()


# ---------------- FINANCIAL DETAILS ----------------

st.subheader("💰 Financial Details")

col1, col2 = st.columns(2)

with col1:
    annual_income = st.number_input(
        "Annual Income (INR)",
        min_value=0,
        value=26000
    )

    monthly_debt = st.number_input(
        "Monthly Debt (INR)",
        min_value=0,
        value=2100
    )

    debt_to_income = st.number_input(
        "Debt to Income Ratio",
        min_value=0.0,
        value=0.25
    )

with col2:
    loan_amount = st.number_input(
        "Loan Amount (INR)",
        min_value=0,
        value=50000
    )

    credit_utilisation = st.number_input(
        "Credit Utilisation (%)",
        min_value=0,
        max_value=100,
        value=45
    )


st.divider()


# ---------------- CREDIT HISTORY ----------------

st.subheader("📊 Credit History")

col1, col2 = st.columns(2)

with col1:
    late_payments = st.number_input(
        "Late Payments",
        min_value=0,
        value=1
    )

    credit_history = st.number_input(
        "Credit History (Years)",
        min_value=0,
        value=8
    )

    credit_accounts = st.number_input(
        "Credit Accounts",
        min_value=0,
        value=5
    )

with col2:
    previous_defaults = st.selectbox(
        "Previous Default",
        ["No", "Yes"]
    )

    payment_history_score = st.number_input(
        "Payment History Score (%)",
        min_value=0,
        max_value=100,
        value=85
    )


# Convert Yes/No into 1/0
if previous_defaults == "Yes":
    previous_defaults = 1
else:
    previous_defaults = 0


st.divider()


# ---------------- PREDICTION ----------------

if st.button(
    "🔍 Predict Creditworthiness",
    use_container_width=True
):

    # Store user input in a DataFrame
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
        "Education_Level": [education_level]
    })


    # Make prediction
    predicted = model.predict(pred)[0]


    # Display result
    if predicted == 0:

        st.error(
            "❌ Prediction: The applicant is **Not Creditworthy**."
        )

    else:

        st.success(
            "✅ Prediction: The applicant is **Creditworthy**."
        )
