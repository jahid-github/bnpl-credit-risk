# BNPL Credit Risk Scoring

An end-to-end machine learning project that predicts Buy Now, Pay Later customer default risk and packages the result into a deployable Streamlit application for fintech-style decision support.

**Live Demo:** [bnpl-credit.streamlit.app](https://bnpl-credit.streamlit.app/)

**Dataset:** [Kaggle - Buy Now and Pay Later Fintech ML Dataset](https://www.kaggle.com/datasets/shree0910/buy-now-and-pay-later-fintech-ml-dataset)

## Project Snapshot

- Built a binary classification workflow on **10,345 customer records**.
- Compared **Logistic Regression** and **Random Forest** models using a scikit-learn pipeline.
- Selected **Random Forest** as the final model with **ROC-AUC 0.7696** and **71% accuracy** on the holdout set.
- Deployed an interactive **Streamlit app** for real-time risk prediction.

## Business Context

This project simulates a BNPL underwriting use case: estimate the probability that a customer will default before approving a purchase. The output can support faster credit decisions, better risk segmentation, and clearer communication between data science and business teams.

## Notebook Workflow

- Removed non-predictive or leakage-prone columns such as `user_id`, `risk_score`, and `transaction_date`
- Split the data with an **80/20 stratified train-test split**
- Encoded categorical features using `OneHotEncoder(handle_unknown="ignore")`
- Built reusable scikit-learn pipelines for **Logistic Regression** and **Random Forest**
- Compared models using **classification metrics** and **ROC-AUC**
- Converted predicted default probabilities into fintech-style risk bands: `Low Risk (<0.30)`, `Medium Risk (0.30-0.70)`, `High Risk (>0.70)`

## Key Outputs

- Dataset balance: **61% non-default** and **39% default**
- Logistic Regression: **69% accuracy**, **0.7592 ROC-AUC**
- Random Forest: **71% accuracy**, **0.7696 ROC-AUC**
- Top Random Forest drivers from the notebook: `credit_score`, `repayment_delay_days`, `monthly_income`, `debt_to_income_ratio`, `app_usage_frequency`

## What This Project Demonstrates

- Data preparation for mixed numerical and categorical credit-risk features
- Feature encoding with a reusable scikit-learn preprocessing pipeline
- Model comparison and evaluation for imbalanced credit-risk classification
- Translation of model probabilities into decision-ready risk segments
- Model serialization with `joblib`
- Lightweight ML product deployment with Streamlit

## Tech Stack

`Python` `pandas` `scikit-learn` `Streamlit` `joblib` `Jupyter Notebook`

## Repository Structure

```text
bnpl-credit-risk/
|-- app/                 # Streamlit application
|-- data/                # Source dataset
|-- models/              # Saved trained model
|-- notebooks/           # Analysis and model development
|-- reports/             # Project outputs and reporting assets
|-- requirements.txt
`-- README.md
```

## Key Files

- `notebooks/01_eda.ipynb` - exploratory analysis, preprocessing, model comparison, feature importance, confusion matrix, and model export
- `models/bnpl_model.pkl` - trained Random Forest pipeline
- `app/app.py` - Streamlit interface for live prediction
- `data/bnpl_dataset.csv` - BNPL customer dataset used for modeling

## Run Locally

```bash
pip install -r requirements.txt
streamlit run app/app.py
```

## Deployment

The project is deployed on Streamlit Community Cloud:

[Open the live app](https://bnpl-credit.streamlit.app/)
