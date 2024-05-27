# Question: Print out the last name of the second employee.
# d = {"employees":[{"firstName": "John", "lastName": "Doe"},
#                 {"firstName": "Anna", "lastName": "Smith"},
#                 {"firstName": "Peter", "lastName": "Jones"}],
# "owners":[{"firstName": "Jack", "lastName": "Petter"},
#           {"firstName": "Jessy", "lastName": "Petter"}]}
# Expected output:
# Smith
import json
from pprint import pprint

emp_dict = {"employees": [{"firstName": "John", "lastName": "Doe"},
                          {"firstName": "Anna", "lastName": "Smith"},
                          {"firstName": "Peter", "lastName": "Jones"}],
            "owners": [{"firstName": "Jack", "lastName": "Petter"},
                       {"firstName": "Jessy", "lastName": "Petter"}]}
print("last name of the second employee is : ", emp_dict["employees"][1]["lastName"])

#Question: Please update the dictionary by changing the last name of the second employee
# from Smith to Smooth or whatever takes your fancy.

emp_dict["employees"][1]["lastName"] = "smooth"
print("last name of the second employee is : ", emp_dict["employees"][1]["lastName"])

#Question: Please add a new employee to the dictionary.

emp_dict["employees"].append({"firstName": "daffa", "lastName": "jaffa"})

pprint(emp_dict)

with open("new_json.json", "w") as file:
    json.dump(emp_dict, file, indent=4)

# Question: Please download the file in the attachment and use Python to print out its content.
# Expected output:
# {'employees': [{'firstName': 'John', 'lastName': 'Doe'},
#                {'firstName': 'Anna', 'lastName': 'Smith'},
#                {'firstName': 'Peter', 'lastName': 'Jones'}],
#  'owners': [{'firstName': 'Jack', 'lastName': 'Petter'},
#             {'firstName': 'Jessy', 'lastName': 'Petter'}]}
f1 = open("/Users/manugundu/PycharmProjects/Python_practice/company1.json", "r")
json_dict = json.load(f1)
pprint(json_dict)
f1.close()



#Please download the json file in the attachment and use Python to
# add a new employee to the file's content so that the file looks like in the expected output below.
f = open("/Users/manugundu/PycharmProjects/Python_practice/company1.json", "r+")
dict_json = json.loads(f.read())
dict_json["employees"].append({'firstName': 'jaffa', 'lastName': 'gaffa'})
f.seek(0)
json.dump(dict_json, f, indent=4)
f.close()

