# create a script that let the user type in a search term and opens and searches on the browser for
# that term
import webbrowser

import pandas
import requests

# search_term = input("enter your search term : ")
# webbrowser.open("https://www.google.com/search?q=%s" %search_term)


# Create a script that reads https://pythonhow.com/media/data/sampledata.txt file,
# multiplies its values by two, and saves the output in a new text file.

sample_data = pandas.read_csv("https://pythonhow.com/media/data/sampledata.txt")
sample_data = sample_data * 2
df = pandas.DataFrame(sample_data)
df.to_csv("multiplier.csv")

# Question: Please concatenate "https://pythonhow.com/media/data/sampledata.txt" file with
# "https://pythonhow.com/media/data/sampledata_x_2.txt" one to a single text file.

df1 = pandas.read_csv("https://pythonhow.com/media/data/sampledata.txt")
df2 = pandas.read_csv("https://pythonhow.com/media/data/sampledata_x_2.txt")
merged_df = pandas.concat([df1, df2], ignore_index=True)
merged_df.to_csv("merged_data.txt")
















