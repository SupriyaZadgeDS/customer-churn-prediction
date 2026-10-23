# Customer Churn Prediction

## Project Overview
This project predicts whether a telecommunications customer is likely to leave the company.

## Project Workflow

1. **Data Loading:** Loaded the Telco Customer Churn dataset using Pandas.
2. **Data Cleaning:** Handled missing values and prepared the data for analysis.
3. **Data Preprocessing:** Prepared numerical and categorical features for machine learning.
4. **Model Training:** Trained a Logistic Regression model using Scikit-learn.
5. **Model Evaluation:** Evaluated performance using accuracy, precision, recall, F1-score, and a confusion matrix.
6. **Threshold Analysis:** Compared classification thresholds to understand the trade-off between recall and precision.
7. **Deployment:** Built a Flask web application to predict customer churn and display risk levels.

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

## Confusion Matrix and Classification Report

The model was evaluated using a classification threshold of 0.40.

### Model Performance

- **Accuracy:** 77.71%
- **Precision (Churn = Yes):** 57%
- **Recall (Churn = Yes):** 67%
- **F1-score (Churn = Yes):** 61%

### Confusion Matrix

|  | Predicted: No Churn | Predicted: Churn |
|---|---:|---:|
| Actual: No Churn | 845 | 190 |
| Actual: Churn | 124 | 250 |

### Interpretation

- **845** customers who did not churn were correctly identified.
- **190** customers who did not churn were incorrectly predicted to churn.
- **124** customers who churned were incorrectly predicted not to churn.
- **250** customers who churned were correctly identified.

The model identifies approximately 67% of customers who actually churned at this threshold. This makes recall an important metric when evaluating the model's ability to identify potential churners.


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
