import pandas as pd

df = pd.read_csv("data_w3schools.csv")
print("info of original dataframe ", df.info())

# To remove empty cells from data- dropna(). it returns new data frame but doesn't modify the original
#df_no_empty = df.dropna()
#print("info of dataframe after removing empty cells", df_no_empty.info())
print(df.to_string())
#print(df_no_empty.to_string())

# To change the original data frame by removing empty cells use - inplace = true
# df.dropna(inplace=True)

# Filling the empty rows using fillna()
# df.fillna(100, inplace=True)
# print(df.to_string())

# replace empty values in the specified column by mentioning its name
# df["Calories"].fillna(130, inplace=True)
# print(df.to_string())


# instead of replacing the empty values with hardcoded values we can us either mean(average),
# median(middle value after sorting), mode(most frequent)
# mean
# x = df["Calories"].mean()
# df["Calories"].fillna(x, inplace=True)
# print(df.to_string())

# Mode
# x = df["Calories"].mode()[0]
# df["Calories"].fillna(x, inplace=True)
# print(df.to_string())


# Median
x = df["Calories"].median()
df["Calories"].fillna(x, inplace=True)
print(df.to_string())


