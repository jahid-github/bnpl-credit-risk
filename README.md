# BNPL Credit Risk Scoring

An end-to-end machine learning project that predicts Buy Now, Pay Later customer default risk and packages the result into a deployable Streamlit application for fintech-style decision support.

**Live Demo:** [bnpl-credit.streamlit.app](https://bnpl-credit.streamlit.app/)

## Project Snapshot

- Built a binary classification workflow on **10,345 customer records**.
- Compared **Logistic Regression** and **Random Forest** models using a scikit-learn pipeline.
- Selected **Random Forest** as the final model with **ROC-AUC 0.7696** and **71% accuracy** on the holdout set.
- Deployed an interactive **Streamlit app** for real-time risk prediction.

## Business Context

This project simulates a BNPL underwriting use case: estimate the probability that a customer will default before approving a purchase. The output can support faster credit decisions, better risk segmentation, and clearer communication between data science and business teams.

## What This Project Demonstrates

- Data preparation for mixed numerical and categorical credit-risk features
- Feature encoding with a reusable scikit-learn preprocessing pipeline
- Model comparison and evaluation using classification metrics and ROC-AUC
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

- `notebooks/01_eda.ipynb` - exploratory analysis, preprocessing, model comparison, evaluation, and model export
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
