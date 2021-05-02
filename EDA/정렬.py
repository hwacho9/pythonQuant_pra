import numpy as np
import pandas as pd

pd.set_option("display.float_format", lambda x: "%.3f" % x)
pd.set_option("max_columns", None)
df = pd.read_csv("my_data/naver_finance/2015_12.csv")

"""top n """
print(df.nsmallest(5, "PER(배)"))
# PER이 가장작은 100개 중에서 , 그 중에서 당기순이익이 가장 큰 5개 종목의 데이터
print(df.nsmallest(100, "PER(배)").nlargest(5, "당기순이익(억원)"))

""" Sort """
print(df.sort_values("EPS(원)", ascending=False).head())  # ascending = False 는 내림차순
print(df.sort_values(["순이익률(%)", "EPS(원)"], ascending=[True, False]))
