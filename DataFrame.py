import numpy as np
import pandas as pd

# 하나의 cell에서 multiple output을 출력을 가능하게 하는 코드
pd.set_option("display.float_format", lambda x: "%.3f" % x)
pd.set_option("max_columns", None)


s1 = np.arange(1, 6, 1)
s2 = np.arange(6, 11, 1)
print(s1, s2)

df = pd.DataFrame({"c1": s1, "c2": s2})
print(df)
# 첫번쨰 방법
pd.DataFrame([[10, 11], [10, 12]])
df2 = pd.DataFrame(np.array([[10, 11], [10, 12]]))
print(df2)
# 세번째 방법
df3 = pd.DataFrame(
    np.array([[10, 11], [20, 21]]), columns=["a", "b"], index=["r1", "r2"]
)
print(df3)
# 네번째 방법
s1 = pd.Series(np.arange(1, 6, 1))  # Series가 아니고 list 여도 됨(iterabl한 object면 다 가능)
s2 = pd.Series(np.arange(6, 11, 1))
df4 = pd.DataFrame({"c1": s1, "c2": s2})
# df4 = pd.DataFrame({"c1": [1,2,3], "c2": [4,5,6]})
print(df4)

"""DataFrame 생성시, Series간에 Index 기준으로 자동정렬 """
s1 = pd.Series(np.arange(1, 6, 1))
s2 = pd.Series(np.arange(6, 11, 1))
s3 = pd.Series(
    np.arange(12, 15), index=[1, 2, 10]
)  # this one has index values unlike s1,s2

df5 = pd.DataFrame({"c1": s1, "c2": s2, "c3": s3})
print(df5)

"""DataFrame에 새로운 column 추가하기"""
df5["c4"] = pd.Series([1, 2, 3, 4], index=[0, 1, 2, 10])
print(df5)