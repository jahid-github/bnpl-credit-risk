from pathlib import Path

import joblib
import pandas as pd
import streamlit as st


st.set_page_config(page_title="BNPL Credit Risk App", layout="wide")

MODEL_PATH = Path(__file__).resolve().parents[1] / "models" / "bnpl_model.pkl"


@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)


def inject_styles():
    st.markdown(
        """
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;700&family=Manrope:wght@400;500;600;700&display=swap');

            :root {
                --bg: #f6f2e9;
                --surface: rgba(255, 251, 245, 0.82);
                --surface-strong: #fffaf2;
                --ink: #15332d;
                --muted: #5e6d68;
                --line: rgba(21, 51, 45, 0.12);
                --teal: #0f766e;
                --teal-deep: #0b5b55;
                --amber: #d97706;
                --rose: #b45309;
                --shadow: 0 20px 50px rgba(31, 41, 55, 0.10);
            }

            .stApp {
                background:
                    radial-gradient(circle at top left, rgba(15, 118, 110, 0.18), transparent 32%),
                    radial-gradient(circle at top right, rgba(217, 119, 6, 0.16), transparent 28%),
                    linear-gradient(180deg, #fbf7ef 0%, #f1ede3 100%);
            }

            html, body, [class*="css"] {
                font-family: "Manrope", sans-serif;
                color: var(--ink);
            }

            h1, h2, h3 {
                font-family: "Space Grotesk", sans-serif;
                letter-spacing: -0.03em;
            }

            .block-container {
                padding-top: 2rem;
                padding-bottom: 2.5rem;
                max-width: 1180px;
            }

            [data-testid="stSidebar"] {
                background: rgba(255, 250, 242, 0.78);
                border-right: 1px solid var(--line);
            }

            [data-testid="stSidebar"] * {
                color: var(--ink);
            }

            [data-testid="stForm"] {
                background: var(--surface);
                border: 1px solid var(--line);
                border-radius: 24px;
                padding: 1.4rem 1.2rem 0.8rem 1.2rem;
                box-shadow: var(--shadow);
                backdrop-filter: blur(12px);
            }

            div[data-testid="stMetric"] {
                background: rgba(255, 250, 242, 0.72);
                border: 1px solid var(--line);
                border-radius: 18px;
                padding: 0.9rem 1rem;
            }

            .hero {
                background:
                    linear-gradient(135deg, rgba(12, 66, 60, 0.96), rgba(15, 118, 110, 0.92)),
                    linear-gradient(135deg, rgba(217, 119, 6, 0.22), rgba(15, 118, 110, 0.06));
                border-radius: 28px;
                padding: 2rem 2rem 1.8rem 2rem;
                color: #f8fbfa;
                box-shadow: 0 24px 60px rgba(15, 118, 110, 0.24);
                animation: rise 0.55s ease-out;
            }

            .hero-kicker {
                font-size: 0.8rem;
                text-transform: uppercase;
                letter-spacing: 0.22em;
                opacity: 0.78;
                margin-bottom: 0.8rem;
            }

            .hero-title {
                font-family: "Space Grotesk", sans-serif;
                font-size: 2.6rem;
                line-height: 1.02;
                margin: 0;
            }

            .hero-copy {
                font-size: 1rem;
                max-width: 760px;
                line-height: 1.7;
                color: rgba(248, 251, 250, 0.88);
                margin: 1rem 0 0 0;
            }

            .stat-card {
                background: rgba(255, 250, 242, 0.78);
                border: 1px solid var(--line);
                border-radius: 22px;
                padding: 1rem 1.1rem;
                box-shadow: var(--shadow);
                min-height: 132px;
                backdrop-filter: blur(12px);
            }

            .stat-label {
                font-size: 0.78rem;
                text-transform: uppercase;
                letter-spacing: 0.16em;
                color: var(--muted);
                margin-bottom: 0.65rem;
            }

            .stat-value {
                font-family: "Space Grotesk", sans-serif;
                font-size: 1.55rem;
                color: var(--ink);
                margin: 0 0 0.35rem 0;
            }

            .stat-note {
                font-size: 0.92rem;
                line-height: 1.6;
                color: var(--muted);
                margin: 0;
            }

            .section-chip {
                display: inline-block;
                background: rgba(15, 118, 110, 0.10);
                color: var(--teal-deep);
                border: 1px solid rgba(15, 118, 110, 0.18);
                border-radius: 999px;
                padding: 0.38rem 0.8rem;
                font-size: 0.78rem;
                font-weight: 700;
                letter-spacing: 0.06em;
                text-transform: uppercase;
                margin-bottom: 0.6rem;
            }

            .section-copy {
                color: var(--muted);
                font-size: 0.95rem;
                line-height: 1.7;
                margin-bottom: 1.15rem;
            }

            .side-panel {
                background: rgba(255, 250, 242, 0.78);
                border: 1px solid var(--line);
                border-radius: 22px;
                padding: 1.1rem 1.1rem 0.95rem 1.1rem;
                box-shadow: var(--shadow);
            }

            .side-panel h3 {
                font-size: 1.05rem;
                margin: 0 0 0.7rem 0;
            }

            .side-panel p,
            .side-panel li {
                color: var(--muted);
                line-height: 1.65;
                font-size: 0.92rem;
            }

            .result-card {
                border-radius: 26px;
                padding: 1.35rem 1.35rem 1.15rem 1.35rem;
                border: 1px solid transparent;
                box-shadow: var(--shadow);
                animation: rise 0.4s ease-out;
                margin-top: 1rem;
            }

            .result-card.low {
                background: linear-gradient(135deg, rgba(15, 118, 110, 0.18), rgba(255, 250, 242, 0.92));
                border-color: rgba(15, 118, 110, 0.20);
            }

            .result-card.medium {
                background: linear-gradient(135deg, rgba(217, 119, 6, 0.17), rgba(255, 250, 242, 0.92));
                border-color: rgba(217, 119, 6, 0.20);
            }

            .result-card.high {
                background: linear-gradient(135deg, rgba(180, 83, 9, 0.18), rgba(255, 250, 242, 0.92));
                border-color: rgba(180, 83, 9, 0.22);
            }

            .result-kicker {
                font-size: 0.78rem;
                text-transform: uppercase;
                letter-spacing: 0.18em;
                color: var(--muted);
                margin-bottom: 0.5rem;
            }

            .result-grid {
                display: flex;
                align-items: center;
                justify-content: space-between;
                gap: 1rem;
                flex-wrap: wrap;
            }

            .result-title {
                font-family: "Space Grotesk", sans-serif;
                font-size: 2rem;
                margin: 0;
                color: var(--ink);
            }

            .result-copy {
                color: var(--muted);
                font-size: 0.96rem;
                line-height: 1.7;
                margin: 0.55rem 0 0 0;
                max-width: 680px;
            }

            .result-pill {
                min-width: 150px;
                text-align: center;
                background: rgba(255, 255, 255, 0.68);
                border: 1px solid var(--line);
                border-radius: 999px;
                padding: 0.9rem 1rem;
            }

            .result-pill strong {
                display: block;
                font-family: "Space Grotesk", sans-serif;
                font-size: 1.55rem;
                color: var(--ink);
            }

            .result-pill span {
                font-size: 0.8rem;
                text-transform: uppercase;
                letter-spacing: 0.16em;
                color: var(--muted);
            }

            .placeholder {
                margin-top: 1rem;
                border-radius: 22px;
                border: 1px dashed rgba(21, 51, 45, 0.18);
                padding: 1rem 1.1rem;
                color: var(--muted);
                background: rgba(255, 250, 242, 0.55);
            }

            div.stButton > button,
            div[data-testid="stFormSubmitButton"] > button {
                width: 100%;
                border: 0;
                border-radius: 999px;
                padding: 0.85rem 1.2rem;
                background: linear-gradient(135deg, #0f766e, #115e59);
                color: #f6fbfa;
                font-family: "Space Grotesk", sans-serif;
                font-size: 1rem;
                font-weight: 700;
                letter-spacing: 0.01em;
                box-shadow: 0 16px 28px rgba(15, 118, 110, 0.22);
            }

            div.stButton > button:hover,
            div[data-testid="stFormSubmitButton"] > button:hover {
                background: linear-gradient(135deg, #115e59, #0b4f4b);
                transform: translateY(-1px);
            }

            div[data-baseweb="input"] > div,
            div[data-baseweb="select"] > div {
                background: rgba(255, 253, 249, 0.95);
                border-radius: 16px;
                border-color: rgba(21, 51, 45, 0.14);
            }

            label,
            .stSelectbox label,
            .stNumberInput label {
                color: var(--ink) !important;
                font-weight: 600 !important;
            }

            @keyframes rise {
                from {
                    opacity: 0;
                    transform: translateY(10px);
                }
                to {
                    opacity: 1;
                    transform: translateY(0);
                }
            }

            @media (max-width: 900px) {
                .hero-title {
                    font-size: 2rem;
                }

                .result-grid {
                    align-items: flex-start;
                }
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


def stat_card(title, value, note):
    return f"""
    <div class="stat-card">
        <div class="stat-label">{title}</div>
        <div class="stat-value">{value}</div>
        <p class="stat-note">{note}</p>
    </div>
    """


def classify_risk(probability):
    if probability < 0.3:
        return (
            "Low Risk",
            "low",
            "The applicant looks relatively stable under the current model. This profile may be suitable for standard approval checks.",
            "Standard approval lane",
        )
    if probability < 0.7:
        return (
            "Medium Risk",
            "medium",
            "The applicant shows a mixed signal profile. This case may benefit from tighter exposure limits or an additional review step.",
            "Review with policy controls",
        )
    return (
        "High Risk",
        "high",
        "The model is flagging elevated default risk. This case may require manual underwriting review or a stricter approval policy.",
        "Escalate for manual review",
    )


model = load_model()
inject_styles()

with st.sidebar:
    st.markdown("### Decision Lens")
    st.caption("A compact scoring prototype for BNPL credit screening.")
    st.markdown("**Model**  \nRandom Forest pipeline")
    st.markdown("**Dataset Size**  \n10,345 customer records")
    st.markdown("**Best ROC-AUC**  \n0.7696")
    st.markdown("---")
    st.markdown("### Risk Bands")
    st.markdown("- Low Risk: below 30%")
    st.markdown("- Medium Risk: 30% to 70%")
    st.markdown("- High Risk: above 70%")

st.markdown(
    """
    <section class="hero">
        <div class="hero-kicker">Fintech Risk Studio</div>
        <h1 class="hero-title">BNPL Credit Risk Prediction</h1>
        <p class="hero-copy">
            Screen a customer profile, estimate default probability, and translate the result
            into a decision-ready risk band. This interface is designed to feel closer to a
            portfolio operations dashboard than a plain model demo.
        </p>
    </section>
    """,
    unsafe_allow_html=True,
)

top_cards = st.columns(3)
with top_cards[0]:
    st.markdown(
        stat_card(
            "Evaluation",
            "71.44% Accuracy",
            "Holdout-set performance of the selected Random Forest model.",
        ),
        unsafe_allow_html=True,
    )
with top_cards[1]:
    st.markdown(
        stat_card(
            "Risk Logic",
            "3 Screening Bands",
            "Probability is translated into low, medium, and high risk buckets.",
        ),
        unsafe_allow_html=True,
    )
with top_cards[2]:
    st.markdown(
        stat_card(
            "Use Case",
            "BNPL Underwriting",
            "Built to support faster pre-approval and review decisions.",
        ),
        unsafe_allow_html=True,
    )

main_col, side_col = st.columns([1.55, 0.95], gap="large")

with main_col:
    st.markdown('<div class="section-chip">Application Input</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-copy">Capture the applicant profile and transaction context below, then run the screening model.</div>',
        unsafe_allow_html=True,
    )

    with st.form("risk_form"):
        left_col, right_col = st.columns(2, gap="large")

        with left_col:
            st.markdown("#### Customer Profile")
            age = st.number_input("Age", min_value=18, max_value=100, value=30)
            employment_type = st.selectbox(
                "Employment Type",
                ["Salaried", "Self-employed", "Student", "Unemployed"],
            )
            monthly_income = st.number_input("Monthly Income", min_value=0.0, value=3000.0)
            credit_score = st.number_input("Credit Score", min_value=300, max_value=900, value=650)
            location = st.selectbox("Location", ["Urban", "Semi-Urban", "Rural"])
            customer_segment = st.selectbox("Customer Segment", ["Low", "Medium", "High"])

        with right_col:
            st.markdown("#### Transaction and Behavior")
            purchase_amount = st.number_input("Purchase Amount", min_value=0.0, value=500.0)
            product_category = st.selectbox(
                "Product Category",
                ["Electronics", "Fashion", "Furniture", "Grocery", "Travel"],
            )
            bnpl_installments = st.number_input("BNPL Installments", min_value=1, max_value=24, value=4)
            repayment_delay_days = st.number_input("Repayment Delay Days", min_value=0, value=0)
            missed_payments = st.number_input("Missed Payments", min_value=0, value=0)
            app_usage_frequency = st.number_input("App Usage Frequency", min_value=0, value=10)
            debt_to_income_ratio = st.number_input(
                "Debt to Income Ratio",
                min_value=0.0,
                max_value=1.0,
                value=0.3,
            )

        submitted = st.form_submit_button("Run Risk Assessment")

    input_data = pd.DataFrame(
        [
            {
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
                "customer_segment": customer_segment,
            }
        ]
    )

    if submitted:
        probability = model.predict_proba(input_data)[0][1]
        risk_level, risk_class, summary, recommendation = classify_risk(probability)

        st.markdown(
            f"""
            <div class="result-card {risk_class}">
                <div class="result-kicker">Assessment Output</div>
                <div class="result-grid">
                    <div>
                        <h2 class="result-title">{risk_level}</h2>
                        <p class="result-copy">{summary}</p>
                    </div>
                    <div class="result-pill">
                        <strong>{probability:.2%}</strong>
                        <span>Default Probability</span>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        metric_cols = st.columns(3)
        metric_cols[0].metric("Default Probability", f"{probability:.2%}")
        metric_cols[1].metric("Risk Level", risk_level)
        metric_cols[2].metric("Suggested Action", recommendation)
        st.progress(float(probability))
    else:
        st.markdown(
            """
            <div class="placeholder">
                Run the model to generate a live risk assessment and decision-style summary.
            </div>
            """,
            unsafe_allow_html=True,
        )

with side_col:
    st.markdown(
        """
        <div class="side-panel">
            <h3>How to Read the Output</h3>
            <p>
                The model estimates the likelihood that a customer may default on a BNPL
                obligation. The percentage is then mapped into a simpler decision band to make
                the result easier to interpret for non-technical users.
            </p>
            <p>
                This is most useful as a decision-support signal alongside policy rules,
                affordability checks, and human review.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("")
    st.markdown(
        """
        <div class="side-panel">
            <h3>Strong Drivers in the Model</h3>
            <p>
                The notebook highlights credit score, repayment delay history, monthly income,
                debt-to-income ratio, app usage frequency, and missed payments as major
                contributors to model behavior.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("")
    st.markdown(
        """
        <div class="side-panel">
            <h3>Screening Intent</h3>
            <p>
                Use this view to simulate frontline underwriting, compare applicant quality,
                and communicate risk in a cleaner format during demos or stakeholder reviews.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
