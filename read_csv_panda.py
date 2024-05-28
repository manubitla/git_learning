import pandas as pd

df = pd.read_csv("data_w3schools.csv")
# printing dataframe without to_string, which outputs only first and last five rows
print(df)

# printing dataframe  to_string, which outputs all rows
print(df.to_string())

# to check systems maximum rows
print(pd.options.display.max_rows)

# we can change the maximum rows a system can return using following statement

pd.options.display.max_rows = 999

# viewing the data using head-can specify first n number of rows or returns first 5 by default
print(df.head())

# returns heading
print(df.head(0))

# returns first 10 rows

print(df.head(10))

# to view last n rows use tail()
print(df.tail(1))

# to print data frames information use info()
print(df.info())
