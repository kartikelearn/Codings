import pandas as pd
coffee=pd.read_csv("D:\Codings\Python Codes\Pandas\Coffee.csv")
# print(coffee.head())
print(coffee)
print(coffee.sample(10))
print(coffee.loc[0]) # .loc[rows,columns]
print(coffee.loc[[0,1,5]]) # We can locate what's on the index/row
print(coffee.loc[1:3,"Day"])
