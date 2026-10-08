# Week 8 Capstone — Customer Churn Business Analysis

## Business Problem
Identify churn drivers, validate them statistically, predict customer risk, and create a measurable retention plan.

## Dataset
500 rows, 9 original columns, 0 missing values, 0 duplicate rows. Target: `Churn`.

## Key Results
- Overall churn: **10.6%**
- Month-to-month churn: **20.6%**
- Contract chi-square p-value: **9.59e-07**
- Tenure Welch t-test p-value: **8.98e-130**
- Monthly Charges Welch t-test p-value: **0.01008**
- Logistic Regression Accuracy: **95.0%**
- ROC-AUC: **0.981**

## Techniques
EDA, segmentation, chi-square test, Welch t-tests, logistic regression, and five model metrics.

## Recommendations
1. Convert month-to-month customers to longer contracts.
2. Strengthen first-year onboarding/support.
3. Test billing/payment assistance.
4. Prioritize retention outreach using risk scores.
5. A/B test every intervention against a control group.

## 90-Day Plan
0–30 days: baseline + pilot.  
31–60 days: controlled experiments.  
61–90 days: scale winners + validate model.

## Structure
`data/` raw + cleaned data | `notebooks/` 3 notebooks | `reports/` executive + technical reports and 6 figures | `presentation/` 12-slide deck | `screenshots/` dashboard | `src/` reusable pipeline | `capstone_analysis.ipynb` | `requirements.txt`.

## Setup & Installation

### Requirements
- Python 3.10+
- Visual Studio Code
- VS Code Python extension (Microsoft)
- VS Code Jupyter extension (Microsoft)

### Installation
1. Open the project folder in VS Code.
2. Create a virtual environment:
   `python -m venv .venv`
3. Activate the environment:
   `.venv\Scripts\activate`
4. Install required libraries:
   `pip install -r requirements.txt`

### How to Run
Open the notebooks in VS Code and select the `.venv` Python kernel.

Run the notebooks in this order:

1. `notebooks/1_data_cleaning.ipynb`
2. `notebooks/2_eda.ipynb`
3. `notebooks/3_analysis.ipynb`

The notebooks perform data cleaning, exploratory analysis, statistical testing, segmentation, and predictive modeling.