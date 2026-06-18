import joblib
import pandas as pd


# Load model

model = joblib.load(
    "../models/churn_model.pkl"
)


print("Model loaded successfully")


# Create customer data
# Must contain ALL training features

customer = pd.DataFrame({

    "gender": ["Male"],

    "SeniorCitizen": [0],

    "Partner": ["Yes"],

    "Dependents": ["No"],

    "tenure": [12],

    "PhoneService": ["Yes"],

    "MultipleLines": ["No"],

    "InternetService": ["Fiber optic"],

    "OnlineSecurity": ["No"],

    "OnlineBackup": ["Yes"],

    "DeviceProtection": ["No"],

    "TechSupport": ["No"],

    "StreamingTV": ["Yes"],

    "StreamingMovies": ["Yes"],

    "Contract": ["Month-to-month"],

    "PaperlessBilling": ["Yes"],

    "PaymentMethod": [
        "Electronic check"
    ],

    "MonthlyCharges": [70],

    "TotalCharges": [840],

    "CustomerValue": [840],

    "CustomerType": [
        "Medium"
    ]

})


# Prediction

prediction = model.predict(customer)


# Result

if prediction[0] == 1:

    print(
        "⚠ Customer is likely to churn"
    )

else:

    print(
        "✅ Customer is likely to stay"
    )