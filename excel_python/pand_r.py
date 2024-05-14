import pandas as pd

# df = pd.read_excel("py.xlsx")
# print(df)

data = {'name':['张三','里斯','王武'],'age':[13,44,42],'gender':['M','W','M']}

df = pd.DataFrame(data)

df.to_excel('new.xlsx')