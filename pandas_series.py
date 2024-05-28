import pandas as pd

print("version of current pandas is : ", pd.__version__)
d1 = dict(weather=["clima"], earth="terra", rain="chuva")
d1["weather"] += ["climate"]
print(d1)
my_df = pd.Series(d1)

print("dictionary is %s pandas Series is \n %s" % (d1, my_df))
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
print("series")
print(pd.Series(data))