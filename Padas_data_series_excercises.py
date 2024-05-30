import coerce
import numpy
import pandas as pd

# Write a Pandas program to create and display a one-dimensional array-like object
# containing an array of data using Pandas module.
li = [1, 2, 3, 4]

# creating a pandas series by passing the list
ds = pd.Series(li)
print(ds.to_string())

# 2. Write a Pandas program to convert a Panda module Series to  Python list, and it's type.

print("type of pandas series is : ", type(ds))
li1 = ds.tolist()
print("list from series : ", li1)
print("its data type is : ", type(li1))

# 3. Write a Pandas program to add, subtract, multiple and divide two Pandas Series.
# Sample Series: [2, 4, 6, 8, 10], [1, 3, 5, 7, 9]
list1 = [2, 4, 6, 8, 10]
list2 = [1, 3, 5, 7, 9]
ds1 = pd.Series(list1)
ds2 = pd.Series(list2)
print("first list is \n", list1)
print("second list is \n", list2)
print("addition of two lists: \n", ds1 + ds2)
print("subtraction of two lists: \n", ds1 - ds2)
print("multiplication of two lists: \n", ds1 * ds2)
print("division of two lists: \n", ds1 / ds2)


# 4. Write a Pandas program to compare the elements of the two Pandas Series.
print("above lists are equal? :", ds1 == ds2)
print("ds1 < ds2 ? :", ds1 < ds2)
print("ds1 > ds2 ? :", ds1 > ds2)

# 5. Write a Pandas program to convert a dictionary to a Pandas series.
orig_dict = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}
ds_dict = pd.Series(orig_dict)
print("original dictionary is : \n", orig_dict)
print("pandas series dictionary is : \n", ds_dict)

# 6. Write a Pandas program to convert a NumPy array to a Pandas series.
numpy_list = numpy.array(li)
print("numpy array is : ", numpy_list)
numpy_ds = pd.Series(numpy_list)
print("numpy array after converting to panda series:\n", numpy_ds)

# 7.Write a Pandas program to change the data type of given a column or a Series.
sample_series = pd.Series(['100', '200', 'python', '300.12', '400', ])
print("original series: ]\n", sample_series)
print(pd.to_numeric(sample_series, errors='coerce'))
# errors = coerce will make the value to Nan if it is not convertible
# 8. Write a Pandas program to convert the first column of a DataFrame as a Series.
d = {'col1': [1, 2, 3, 4, 7, 11], 'col2': [4, 5, 6, 9, 5, 0], 'col3': [7, 5, 8, 12, 1, 11]}
df = pd.DataFrame(d)
ds_df = pd.Series(df.loc[0])
print("Data frame is : \n", df)
print("first column of above dataframe as series: \n", ds_df)

# 9. Write a Pandas program to convert a given Series to an array.
# can convert series to array using tolist() or series.values
print("series to list using series.tolist(): \n", sample_series.tolist())
print("series to list using series.values: \n", sample_series.values)
# 10. Write a Pandas program to convert Series of lists to one Series.
series_lists = pd.Series([['Red', 'Green', 'White'], ['Red', 'Black'], ['yellow']])
print(series_lists.apply(pd.Series).stack().reset_index(drop=True))