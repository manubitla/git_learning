# creating a number list using range
import collections
import string
from pprint import pprint

my_list = range(1, 21)
# range 1 to 20, upper bound excluded. range creates python range object.must use list() to prit

print(list(my_list))

# Question: Complete the script so that it produces the expected output.
# Please use my_range  as input data.

# Expected output:

# [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200] \
my_range = range(1,21)
print([10*x for x in my_range])

# Question: Complete the script, so it generates the expected output using my_range  as input data.
# Please note that the items of the expected list output are all strings.
my_list = range(1,21)
# solution 1
print([str(x) for x in my_list])
# solution 2
print(list(map(str,my_list)))
# Question: Complete the script so that it removes duplicate items from the list a .

dup_list = ["1", 1, "1", 2]
# using set
print("original list : ", list(dup_list))
print("using set() : ",list(set(dup_list)))
# using list comprehension
res = []
[res.append(x) for x in dup_list if x not in res]
print("using list comprehension : ", res)
# using collections.OrderedDict.fromkeys()
print("using collections.OrderedDict.fromkeys() : ", list(collections.OrderedDict.fromkeys(dup_list)))
# using “in”, “not in” operators
res = []
for i in dup_list:
    if i not in res:
        res.append(i)

print("using “in”, “not in” operators : ", res)

# Question: Create a dictionary that contains the keys a  and b  and their respective values 1  and 2 .
dict1 = {'a': 1, 'b': 2}
dict2 = dict(a=1, b=2)
print("dict1: ",dict1, "  dict2: ",dict2)
# Question: Please complete the script so that it prints out the value of key b .
print("value of b is : ", dict1.get("b"))
print("value of b is : ", dict1["b"])
# Question: Calculate the sum of the values of keys a  and b .
d = {"a": 1, "b": 2, "c": 3}
sumd = d["a"]+d["b"]
print("sum of a, b is : ", sumd)
d = {"name": "john", "surname": "smith"}
# print surname using smith
k = [key for key, value in d.items() if value == "smith"]
print(k)
# Question: Add a new pair of key (e.g. c ) and value (e.g. 3 ) to the dictionary and print out the new dictionary.

d = {"a": 1, "b": 2}
# using assignment operator
d["c"] = 3
print("using assignment operator : ", d)
# using update
d.update({"d": 4})
print("using update operator : ", d)
# using _setitem
d.__setitem__("e", 5)
print("using setitem operator : ", d)

# Question: Calculate the sum of all dictionary values.
d = {"a": 1, "b": 2, "c": 3}
print("sum of dictionary values is : ", sum(d.values()))
# Question: Filter the dictionary by removing all items with a value of greater than 1.
res = [(k, v) for k, v in d.items() if v<=1]
print("dictionary with values<=1 is : ", res)
# Create a dictionary of keys a, b, c where each key has as value a list from 1 to 10, 11 to 20,
# and 21 to 30, respectively. Then print out the dictionary in a nice format.
d1 = {"a": list(range(1, 10)), "b": list(range(11, 20)), "c": list(range(21, 30))}
print("**********  SIMPLE PRINT FUNCTION ************")
print(d1)
print("********** PPRINT FUNCTION ************")
pprint(d1)

# Question: Access the third value of key b  from the dictionary.
print("printing 3rd value of key b: ", d1["b"][2])
# Question: Please complete the script so that it prints out the expected output.

# Expected output:
# b has value [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# c has value [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
# a has value [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for k, v in d1.items():
    print(k, "has value ", v)
# Make a script that prints out letters of the English alphabet
# from a to z, one letter per line in the terminal.
upper = []
for letter in string.ascii_uppercase:
    upper.append(letter)
lower = []
for letter in string.ascii_lowercase:
    lower.append(letter)
print("upper case letters: ", upper)
print("lower case letters: ", lower)

# Question: Make a script that prints out numbers from 1 to 10
num = list(range(1, 11))
for i in num:
    print(i)






