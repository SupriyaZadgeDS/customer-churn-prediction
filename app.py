
from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained machine-learning pipeline
model = joblib.load("customer_churn_model.pkl")


@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None

    if request.method == "POST":
        # Collect all 19 features expected by the model
        customer = {
            "gender": request.form["gender"],
            "SeniorCitizen": int(request.form["SeniorCitizen"]),
            "Partner": request.form["Partner"],
            "Dependents": request.form["Dependents"],
            "tenure": int(request.form["tenure"]),
            "PhoneService": request.form["PhoneService"],
            "MultipleLines": request.form["MultipleLines"],
            "InternetService": request.form["InternetService"],
            "OnlineSecurity": request.form["OnlineSecurity"],
            "OnlineBackup": request.form["OnlineBackup"],
            "DeviceProtection": request.form["DeviceProtection"],
            "TechSupport": request.form["TechSupport"],
            "StreamingTV": request.form["StreamingTV"],
            "StreamingMovies": request.form["StreamingMovies"],
            "Contract": request.form["Contract"],
            "PaperlessBilling": request.form["PaperlessBilling"],
            "PaymentMethod": request.form["PaymentMethod"],
            "MonthlyCharges": float(request.form["MonthlyCharges"]),
            "TotalCharges": float(request.form["TotalCharges"])
        }

        # Keep the same feature order used during training
        input_data = pd.DataFrame([customer], columns=model.feature_names_in_)

        result = int(model.predict(input_data)[0])
        churn_probability = model.predict_proba(input_data)[0][1] * 100
        churn_probability = round(churn_probability, 2)
        if churn_probability < 30:
            risk_level = "Low Risk"
            risk_color = "low-risk"
        elif churn_probability < 60:
            risk_level = "Medium Risk"
            risk_color = "medium-risk"
        else:
            risk_level = "High Risk"
            risk_color = "high-risk"
        if result == 1:
            prediction = "Prediction: Customer is likely to churn."
        else:
            prediction = "Prediction: Customer is likely to stay."

    return render_template(
    "index.html",
    prediction=prediction,
    churn_probability=churn_probability if request.method == "POST" else None,
    risk_level=risk_level if request.method == "POST" else None,
    risk_color=risk_color if request.method == "POST" else None
)



if __name__ == "__main__":
    app.run(debug=True)
