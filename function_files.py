# Question: Please download the words1.txt file from the attachment and then create a Python
# function that takes a text file as input and returns the number of words contained in the text file.
# Expected output:
# 10
import glob
import json
import math
import re
import string
from pprint import pprint

import requests

# def text_file_words(str):
#     f = open(str, "r")
#     words = f.read().split(" ")
#     print(len(words))
#
#
# path = "/Users/manugundu/PycharmProjects/Python_practice/words1.txt"
# text_file_words(path)


# Question: Create a function that takes a text file as input and returns the number of words contained
# in the text file. Please take into consideration that a comma can separate some words with no space.
# For example, "Hi, it's me." would need to be counted as three words
# A tree is a woody perennial plant,typically with branches.

# def text_file_words_two_splits(str):
#     f = open(str, "r")
#     words = f.read()
#     # words = words.replace(",", " ")
#     # words = words.split(" ")
#     words_split = re.split(",| ", words)
#     print(len(words_split))
#
#
# path = "/Users/manugundu/PycharmProjects/Python_practice/words2.txt"
# text_file_words_two_splits(path)
#
# print("square root of 9 is : ", math.sqrt(9))
# print(dir(math))
# print(math.cos(1))


# Question: Create a script that generates a text file with
# all letters of the English alphabet inside it, one letter per line.

# def write_file():
#     f = open("/Users/manugundu/PycharmProjects/Python_practice/write.txt", "w")
#     for letter in string.ascii_letters:
#         f.write(letter + "\n")
#     #print(f.readlines())
#
#
# write_file()


# Question: Create a script that generates a file where all letters of the English alphabet
# are listed two in each line. The inside of the text file would look like:
# ab
# cd
# ef
# and so on.


# def alpha_two():
#     f = open("/Users/manugundu/PycharmProjects/Python_practice/alpha_two.txt", "w")
#     count = 0
#     for letter in string.ascii_lowercase:
#         f.write(letter)
#         count = count + 1
#         if count > 1:
#             f.write("\n")
#             count = 0
#
#
# alpha_two()


# Question: Create a script that generates a file where all letters of the English alphabet are listed
# three in each line. The inside of the text file would look like:
# abc
# def
# ghi


# def alpha_three():
#     f = open("/Users/manugundu/PycharmProjects/Python_practice/alpha_three.txt", "w")
#     for l1, l2, l3 in zip(string.ascii_lowercase[0::3], string.ascii_lowercase[1::3], string.ascii_lowercase[2::3]):
#         f.write(l1 + l2 + l3 + "\n")
#
#
# alpha_three()


# Question: Please create a script that generates 26 text files named a.txt, b.txt,
# and so on up to z.txt. Each file should contain a letter reflecting its filename.
# So, a.txt will contain letter a, b.txt will contain letter b, and so on.


# def txt_26_files():
#     for letter in string.ascii_uppercase:
#         path_txt = "/Users/manugundu/PycharmProjects/Python_practice/txtfiles/" + letter + ".txt"
#         f = open(path_txt, "w")
#         f.write(letter)
#         f.close()
#
#
# txt_26_files()


# write a script that extracts letters from 26 text files and put the letters in a text file


# def letter_extractor(letter_list):
#     file_list = glob.glob("letters/*.txt")
#     print(list(file_list))
#     for filename in file_list:
#         file = open(filename, "r")
#         letter_list.append(file.read())


# letter_list = []
# letter_extractor(letter_list)
# print("all file's data in one list : ", letter_list)


# write a script that iterates through each of the 26 text files, check if the
# letter inside the text file is in string "python" and puts letter in the list if the character is in
# "python"

# def check_letter_26_txt_files_python(letters_python):
#     file_list = glob.glob("letters/*.txt")
#     for filename in file_list:
#         file = open(filename, "r")
#         letter = file.read()
#         # if("PYTHON".__contains__(letter)):
#         #     letters_python.append(letter)
#         if letter in "PYTHON":
#             letters_python.append(letter)
#
#
# letters_python = []
# check_letter_26_txt_files_python(letters_python)
# print("PYTHON = ", letters_python)

# age = int(input("What's your age? "))
# age_last_year = age - 1
# print("Last year you were %s.", age_last_year)
#
# firstname = input("Enter first name: ")
# secondname = input("Enter second name: ")
# print("Your first name is %s and your second name is %s" , firstname, secondname)


# Question: Print out the text of this file https://pythonhow.com/media/data/universe.txt
# Don't manually download the file. Let Python do all the work.

# response = requests.get("https://pythonhow.com/media/data/universe.txt")
# text = response.text
# print(text)
# print(type(text))

# Question: Count the number of "a" characters in this text file:
# http://www.pythonhow.com/data/universe.txt

response = requests.get("https://pythonhow.com/media/data/universe.txt")
text = response.text
print(text)
text1 = list(text)
count = 0
print("using count to get the count of a's", text.count('a'))
for char in text1:
    if char == 'a':
        count = count + 1

print("number of a's in the above document are : ", count)