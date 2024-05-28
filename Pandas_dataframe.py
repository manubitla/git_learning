import pandas as pd

d1 = dict(weather=["clima"], earth="terra", rain="chuva")
d1["weather"] += ["climate"]
print(d1)
my_df = pd.DataFrame(d1)

print("dictionary is %s pandas data frame is \n %s" % (d1, my_df))

data = {
    "calories": [420, 380, 390, 674, 673, 590],
    "duration": [50, 40, 45, 56, 32, 77]
}
print("data frame")
# we can name the indexes or default index numbers can be given
df = pd.DataFrame(data, index=["day1", "day2", "day3", "day4", "day5", "day7"])
print(df)
# below statement returns a panda series
print(df.loc["day1"])
# printing multiple rows which returns data frame
print(df.loc[["day1", "day2"]])

# loading csv file into pandas dataframe and printing its contents

csv_df = pd.read_csv("data_panda.csv")
print(csv_df)



