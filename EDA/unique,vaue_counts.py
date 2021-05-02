import numpy as np
import pandas as pd

pd.set_option("display.float_format", lambda x: "%.3f" % x)
pd.set_option("max_columns", None)

df = pd.read_csv("my_data/naver_finance/2015_12.csv")

# For DataFrame => nunique()
print(df.nunique())

# For Series => unique(), nunique(), value_counts()
print(df["ticker"].unique)
print(df["ticker"].nunique)
print(df["ticker"].value_counts())
print(df["ticker"].value_counts(normalize=True))

# value_counts() ignore np.nan
a = pd.DataFrame({"a": [np.nan, 1, 2]})["a"]
print(a)
print(a.value_counts())

a = pd.read_csv("my_data/symbol_sector.csv")
print(a.head)
print(a["Sector"].nunique())
print(a["Sector"].value_counts())
