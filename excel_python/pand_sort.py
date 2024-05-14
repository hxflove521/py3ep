import pandas as pd

df = pd.read_excel(io="t.xlsx",index_col="id")

# print(df.sort_values("age"))
print(df.sort_values(["isok","name"],ascending=False))

