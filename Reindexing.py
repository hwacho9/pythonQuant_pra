import numpy as np
import pandas as pd

# 하나의 cell에서 multiple output을 출력을 가능하게 하는 코드
pd.set_option("display.float_format", lambda x: "%.3f" % x)
pd.set_option("max_columns", None)

s = pd.Series([1, 2, 3, 4, 5])
print(s)
s.index = ["a", "b", "c", "d", "e"]
print(s)

s1 = pd.Series(np.arange(1, 6, 1))
s2 = pd.Series(np.arange(6, 11, 1))
s3 = pd.Series(
    np.arange(12, 15), index=[1, 2, 10]
)  # this one has index values unlike s1,s2
df = pd.DataFrame({"c1": s1, "c2": s2, "c3": s3})
df["c4"] = pd.Series([1, 2, 3, 4], index=[0, 1, 2, 10])
df["c5"] = pd.Series([1, 2, 3, 4, 5, 6], index=[0, 1, 2, 3, 4, 10])
print(df)

print(df.set_index("c5"))

""" Reindex : 기존의 index-value mapping은 유지한채 재배열하는 것"""
s2 = s.reindex(["a", "c", "e", "g"])
print(s2)
s2["a"] = 0
print(s2)


s1 = pd.Series([0, 1, 2], index=[0, 1, 2])
s2 = pd.Series([0, 1, 2], index=["0", "1", "2"])
print(s2.index)
s2.index = s2.index.astype(int)
print(s2.index)

s2 = s.copy()
s2 = s2.reindex(["a", "f"])
print(s2)
s2 = s2.reindex(["a", "f"], fill_value=0)  # fill 0 instead of Nan
print(s2)

s3 = pd.Series(["red", "green", "blue"], index=[0, 3, 5])
print(s3)
s3 = s3.reindex(np.arange(0, 7))
print(s3)
s4 = s3.reindex(np.arange(0, 7), method="ffill")
print(s4)
