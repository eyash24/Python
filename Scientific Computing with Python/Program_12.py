# lesson: JavaScript Object Notation, Web Services: JSON
# Source: https://www.freecodecamp.org/learn/scientific-computing-with-python, https://www.youtube.com/watch?v=8DvywoWv6fI&list=PPSV

import json

data='''{
    "name" : "xyz",
    "phone" : {
        "type" : "intl",
        "number" : "+91 123 456 7890"
    },
    "email" : {
        "hide" : "yes"
    }
}
'''

info = json.loads(data)
print("Name: ",info["name"]) 
print("Hide: ",info["email"]["hide"]) 

"""
Output:
Name:  xyz
Hide:  yes
"""

print()
print()

data_2 = '''[
    {
        "id" : "001",
        "x" : "2",
        "name" : "xyz_1"
    },
    {
        "id" : "002",
        "x" : "4",
        "name" : "xyz_2"
    }
]
'''

info_2 = json.loads(data_2)
print("User count: ", len(info_2))
for item in info_2:
    print("Name: ",item['name'])
    print("x: ",item["x"])
    print("ID: ",item["id"])
    print()

'''
Output:
User count:  2
Name:  xyz_1
x:  2
ID:  001

Name:  xyz_2
x:  4
ID:  002

'''




