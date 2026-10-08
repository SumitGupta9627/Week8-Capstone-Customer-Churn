import pandas as pd
from scipy import stats
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
df=pd.read_csv("data/raw_data.csv")
print(df.shape, df.isna().sum().sum(), df.duplicated().sum())
print(stats.chi2_contingency(pd.crosstab(df.Contract,df.Churn))[1])
