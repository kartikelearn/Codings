import pandas as pd
df= pd.DataFrame([[1,2,3],[4,5,6],[6,7,8]],columns=["A","B","C"],index=["X","Y","Z"])
print(df.head(2))   # Shows the 1st two rows.
print(df.tail(2))   # Shows the last two rows.
print(df.columns)   # Returns the names of columns
print(df)   # Prints the DataFrame
print(df.index) # Shows the Rows
print(df.index.tolist()) # Shows the rows in List
print(df.info()) # Shows all the information of the DataFrame
print(df.describe()) # Shows Count, Mean, STD, MIN, 25%...75% & MAX
print(df.nunique()) # Returns No.. of Unique datas in a column..
print(df["A"].unique()) # Shows Unique Data in a column..
print(df.shape) # The shape(dimension) of DataFrame
print(df.size) # No.. of elements in DataFrame
print(df.ndim) # Dimension of DataFrame