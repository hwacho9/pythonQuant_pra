import numpy as np
import pandas as pd

a = np.array([1, 2, 3])
print(a)
b = np.array([4, 5, 6])
print(a + b)

c = np.array([[1, 2], [3, 4]])
print(c[1][0])

# NAN
s = pd.Series([10, 0, 1, 1, 2, 3, 4, 5, 6, np.nan])
print(s)  # float로 변환
print(s.count())  # not count 'NAN'

print(s.value_counts())

# Series연산에서 Data의 순서가 아니라 index label이 자동으로 정렬되어 연산이 진행됨
s3 = pd.Series([1, 2, 3, 4], index=["a", "b", "c", "d"])
s4 = pd.Series([4, 3, 2, 1], index=["d", "c", "b", "a"])
print(s3, s4)
print(s3 + s4)