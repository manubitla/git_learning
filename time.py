# Create a program that prints Hello repeatedly
import time

# while 1:
#     print("hello")

# Question: Create a program that prints out Hello  every two seconds.

# while True:
#     print("hello")
#     time.sleep(2)

# Question: Create a program that, once executed the program prints Hello  instantly first,
# then it prints it after 1 second, then after 2, 3, 4, and so on the interval increases between prints.
# count = 0
# while 1:
#     time.sleep(count)
#     print("hello")
#     count = count + 1
# Question: Create a program that, once executed the programs prints Hello  instantly first,
# then it prints it after 1 second, then after 2, 3, and then the program prints out the message
# "End of the Loop" and stops.
# count = 0
# while 1:
#     time.sleep(count)
#     print("hello")
#     count = count + 1
#     if count > 3:
#         print("End of the loop")
#         break
# The following code prints hello, check if 2 is > and then breaks the loop because 2 is always
# greater than 1.therefore hi is not printed out. please replace break with something else so that hello is
# printed out repeatedly and hi is never printed
# while true
# print("hello")
# if 2>1:
#    break
# print(hi)

while True:
    print("hello")
    if 2>1:
        continue
    print("hi")
