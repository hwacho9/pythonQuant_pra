import pandas as pd

"""
다수의 Series를 하나의 변수로 관리할 수 있도록 만든 자료형
Series의 dict 형태라고 보면됨
{'컬럼명1': Series1, '컬럼명2': Series2}
각 Series는 DataFrame의 column을 이룸
당연히 DataFrame을 이루는 Series간의 index는 서로 다 같음! => 동일 index 사용
"""

a = pd.Series([1, 2, 3, 4])
print(a)
print(type(a))
# 첫번째 방법
s2 = pd.Series([1, 2, 3, 4], index=["a", "b", "c", "d"])
print(s2)
print(s2.head(3))  # 최상위 5개만 보여줌
# 두번째 방법
s3 = pd.Series({"a": 1, "b": 2, "c": 3, "d": 4, "e": 5})