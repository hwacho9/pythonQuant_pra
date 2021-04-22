import numpy as np
import pandas as pd

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
s1 = pd.Series(np.arange(1, 6, 1))
s2 = pd.Series(np.arange(6, 11, 1))
df4 = pd.DataFrame({"c1": s1, "c2": s2})
print(df4)