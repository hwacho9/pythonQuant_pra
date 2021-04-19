import pandas as pd


a = pd.Series([1, 2, 3, 4])
print(a)
print(type(a))
# 첫번째 방법
s2 = pd.Series([1, 2, 3, 4], index=["a", "b", "c", "d"])
print(s2)
print(s2.head(3))  # 최상위 5개만 보여줌
# 두번째 방법
s3 = pd.Series({"a": 1, "b": 2, "c": 3, "d": 4, "e": 5})