# Question:
# Create a function that calculates acceleration given initial velocity v1, final velocity v2,
# start time t1, and end time t2. The formula for acceleration is:
# a = (v2-v1)/(t2-t1)
# To test your solution, call the function by inputting values 0, 10, 0, 20 for v1, v2, t1, and t2,
# respectively, and you should get the expected output.
import math


def acceleration(v1, v2, t1, t2):
    a = (v2 - v1) / (t2 - t1)
    return a


v1 = 0
v2 = 10
t1 = 0
t2 = 20
print("acceleration is : ", acceleration(v1, v2, t1, t2))


# Question:  Please write a function that calculates liquid volume in a sphere using the following formula
# The radius r  is always 10, so consider making it a default parameter.
# partially filled sphere formula
# liquid volume = ((4*pi*(r*r*r))/3) - ((pi*(h*h)*((3*r)-h))/3)
# You can then test your solution by passing 2 for h and you should get the expected output.
#
# Expected output:
#
# 4071.5040790523717


def liquid_volume(h, r=10):
    volume = ((4 * math.pi * (r * r * r)) / 3) - ((math.pi * (h * h) * ((3 * r) - h)) / 3)
    return volume


print("liquid volume of sphere is : ", liquid_volume(2))

c = 1


def foo():
    c = 2
    return c


c = 3
print(foo())


# Question: The following script throws a NameError  in the last line saying that c  is not defined.
# Please fix the function so that there is no error and the  last line can print out the value of c
# (i.e. 1 ).
# def foo():
#     c = 1
#     return c
# foo()
# print(c)


def foo1():
    global c1
    c1 = 1
    return c1


foo1()
print(c1)


# Question: Create a function that takes any string as input and returns the number of words for
# that string.


def words_string(s):
    s1 = s.split(" ")
    return len(s1)


str1 = "my name is shathulu"
print("number of words in the given string ", str1, "are : ", words_string(str1))
