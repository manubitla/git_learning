# Question: Please complete the code so that it prints out the expected output.
# a = [1, 2, 3]
# Expected output:
# Item 1 has index 0
# Item 2 has index 1
# Item 3 has index 2
import time
from pprint import pprint

a = [1, 2, 3]
print("original list is : ")
pprint(a)
for index, item in enumerate(a):
    #print("Item", item, "has", "index", index)

    print("Item %s has index %s" % (item, index))

