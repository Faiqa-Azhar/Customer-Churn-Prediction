import streamlit as st
import pandas as pd
import joblib


# -----------------------------
# Load Model
# -----------------------------

model = joblib.load(
    "../models/churn_model.pkl"
)


# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="Customer Churn AI",
    page_icon="📊",
    layout="wide"
)



# -----------------------------
# Professional Theme
# -----------------------------

st.markdown(
"""
<style>


.main {

background-color:#f8fafc;

}


h1 {

font-size:42px !important;
color:#0f172a;

}


h2 {

font-size:28px !important;

}


h3 {

font-size:22px !important;

}


p,label {

font-size:17px !important;

}



.stButton button {

width:100%;

height:50px;

font-size:18px;

font-weight:600;

border-radius:10px;

}


</style>

""",
unsafe_allow_html=True
)




# -----------------------------
# Title
# -----------------------------


st.title(
"📊 Customer Churn Intelligence System"
)


st.caption(
"AI-powered customer retention analytics using Machine Learning"
)


st.write(
"""
This system predicts customers who are likely to leave 
and provides business retention recommendations.
"""
)


st.divider()



# -----------------------------
# Customer Information
# -----------------------------


st.subheader(
"👤 Customer Information"
)


col1,col2,col3 = st.columns(3)



with col1:


    gender = st.selectbox(
        "Gender",
        ["Male","Female"]
    )


    senior = st.selectbox(
        "Senior Citizen",
        [0,1]
    )


    partner = st.selectbox(
        "Partner",
        ["Yes","No"]
    )



with col2:


    dependents = st.selectbox(
        "Dependents",
        ["Yes","No"]
    )


    tenure = st.number_input(
        "Tenure (Months)",
        0,
        100,
        12
    )


    phone = st.selectbox(
        "Phone Service",
        ["Yes","No"]
    )



with col3:


    multiple_lines = st.selectbox(
        "Multiple Lines",
        ["Yes","No"]
    )


    internet = st.selectbox(
        "Internet Service",
        [
        "DSL",
        "Fiber optic",
        "No"
        ]
    )


    contract = st.selectbox(
        "Contract",
        [
        "Month-to-month",
        "One year",
        "Two year"
        ]
    )



st.divider()



# -----------------------------
# Services
# -----------------------------


st.subheader(
"⚙️ Services"
)



col4,col5,col6 = st.columns(3)



with col4:


    online_security = st.selectbox(
        "Online Security",
        ["Yes","No"]
    )


    online_backup = st.selectbox(
        "Online Backup",
        ["Yes","No"]
    )


    device_protection = st.selectbox(
        "Device Protection",
        ["Yes","No"]
    )



with col5:


    tech_support = st.selectbox(
        "Tech Support",
        ["Yes","No"]
    )


    streaming_tv = st.selectbox(
        "Streaming TV",
        ["Yes","No"]
    )


    streaming_movies = st.selectbox(
        "Streaming Movies",
        ["Yes","No"]
    )



with col6:


    paperless = st.selectbox(
        "Paperless Billing",
        ["Yes","No"]
    )


    payment = st.selectbox(
        "Payment Method",
        [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
        ]
    )



st.divider()



# -----------------------------
# Financial Information
# -----------------------------


st.subheader(
"💰 Financial Information"
)



col7,col8 = st.columns(2)



with col7:


    monthly = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        value=70.0
    )



with col8:


    total = st.number_input(
        "Total Charges",
        min_value=0.0,
        value=800.0
    )



# -----------------------------
# Feature Engineering
# -----------------------------


customer_value = tenure * monthly



if tenure < 12:

    customer_type = "New Customer"


elif tenure < 36:

    customer_type = "Medium"


else:

    customer_type = "Loyal"



st.info(
f"Customer Segment: {customer_type}"
)



st.divider()



# -----------------------------
# Prediction
# -----------------------------


if st.button(
    "🔍 Predict Churn"
):


    customer = pd.DataFrame({


        "gender":[gender],

        "SeniorCitizen":[senior],

        "Partner":[partner],

        "Dependents":[dependents],

        "tenure":[tenure],

        "PhoneService":[phone],

        "MultipleLines":[multiple_lines],

        "InternetService":[internet],

        "OnlineSecurity":[online_security],

        "OnlineBackup":[online_backup],

        "DeviceProtection":[device_protection],

        "TechSupport":[tech_support],

        "StreamingTV":[streaming_tv],

        "StreamingMovies":[streaming_movies],

        "Contract":[contract],

        "PaperlessBilling":[paperless],

        "PaymentMethod":[payment],

        "MonthlyCharges":[monthly],

        "TotalCharges":[total],

        "CustomerValue":[customer_value],

        "CustomerType":[customer_type]

    })



    prediction = model.predict(customer)



    probability = model.predict_proba(customer)



    churn_probability = probability[0][1]



    st.subheader(
    "📌 Prediction Result"
    )



    if prediction[0] == 1:


        st.error(
        """
        🚨 HIGH CHURN RISK

        Customer is likely to leave.
        """
        )



        st.metric(
        "Churn Probability",
        f"{churn_probability*100:.2f}%"
        )



        st.warning(
        """
        Recommended Actions:

        • Offer retention discount

        • Provide better support

        • Encourage long-term contract

        """
        )



    else:


        st.success(
        """
        ✅ CUSTOMER RETAINED

        Customer is likely to stay.
        """
        )


        st.metric(
        "Churn Probability",
        f"{churn_probability*100:.2f}%"
        )



# -----------------------------
# Business Metrics
# -----------------------------


st.divider()


st.subheader(
"📈 Business Insights"
)


c1,c2,c3 = st.columns(3)


c1.metric(
"Customer Type",
customer_type
)


c2.metric(
"Monthly Revenue",
f"${monthly}"
)


c3.metric(
"Customer Value",
f"${customer_value}"
)

