# Customer Churn Prediction

## Project Overview
This project predicts whether a telecommunications customer is likely to leave the company.

## Objectives
- Predict customer churn using machine learning.
- Estimate churn probability.
- Classify customers into Low, Medium, and High risk levels.
- Provide predictions through a Flask web application.

## Technologies Used
- Python
- Pandas
- Scikit-learn
- Flask
- Joblib
- Jupyter Notebook
- HTML and CSS

## Machine Learning
The project uses a trained machine-learning pipeline to predict customer churn and estimate churn probability.

## Model Evaluation

The model was evaluated using different classification thresholds to understand the trade-off between accuracy, recall, and precision.

| Threshold | Accuracy | Recall | Precision |
|   ---     |    ---:  |   ---: |    ---:   |
| 0.30      | 74.95%   | 75.40% | 51.93%    |
| 0.40      | 77.71%   | 66.84% | 56.82%    |
| 0.50      | 80.55%   | 55.88% | 65.72%    |
| 0.60      | 79.91%   | 40.11% | 71.77%    |

A lower threshold identifies more customers who may churn, increasing recall but also producing more false positives. A higher threshold improves precision but may miss more customers who actually churn.

## Web Application
The Flask application accepts customer details and displays a churn prediction, probability, and risk level.

## How to Run
1. Install the required packages:
   `pip install -r requirements.txt`
2. Start the application:
   `python app.py`
3. Open `http://127.0.0.1:5000` in your browser.

## Author
Supriya Zadge
