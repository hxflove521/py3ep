import pandas as pd

# data = pd.Series([1,2,3],[1,2,3],name='data')

# print(data)

s1 = pd.Series([1,2,3],index=[1,2,3],name="A")
s2 = pd.Series([4,5,6],index=[1,2,3],name="B")
s3 = pd.Series([7,8,9],index=[1,2,3],name="C")

df = pd.DataFrame([s1,s2,s3])
print(df)