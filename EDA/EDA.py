import numpy as np
import pandas as pd

# 하나의 cell에서 multiple output을 출력을 가능하게 하는 코드
pd.set_option("display.float_format", lambda x: "%.3f" % x)
pd.set_option("max_columns", None)

df = pd.read_csv("naver_finance/2015_12.csv")
print(df.head)

""" Metadata """
df.shape
print(df.info())
print(df["ticker"].dtype)
df = df.rename(columns={"ticker": "종목명"})
print(df.head)

""" describe() """
print(df.describe())
a = df.describe()
print(a.T)  # 행 열 일시적으로 변환

df.describe(include=[np.number]).T  # df. describe()
print(df.describe(percentiles=[0.01, 0.03, 0.99]).T.head(2))

print(
    df.describe(include=[np.object_, pd.Categorical]).T.head()
)  # 'top' "가장 많이 나오는 단어"를 의미함

df.describe(exclude=[np.number]).T.head()

print(df["PER(배)"].quantile(0.2))
print(df["PER(배)"].quantile([0.1, 0.2, 0.3]))