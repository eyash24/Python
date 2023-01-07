# lesson: Using web services: XML
# Source: https://www.freecodecamp.org/learn/scientific-computing-with-python, https://www.youtube.com/watch?v=8DvywoWv6fI&list=PPSV

import xml.etree.ElementTree as ET

'''
XML basic
<person>                        Start Tag
    <name> xyz </name>          End Tag
    <phone type='intl'>         
        +91 1234567890          Text content
    </phone>
    <email hide='yes'/>         Attribute
</person>                       Self Closing Tag
'''

data = '''
<person>                        
    <name> xyz </name>          
    <phone type='intl'>         
        +91 1234567890          
    </phone>
    <email hide='yes'/>         
</person>
'''

tree = ET.fromstring(data)
print("Name: ",tree.find('name').text) # output: Name:   xyz 
print("Attr: ",tree.find('email').get('hide')) # output: Attr:  yes

print()
print()

input = '''
<stuff>
    <users>
        <user x="1">
            <id>001</id>
            <name>xyz_1</name>
        </user>
        <user x="2">
            <id>002</id>
            <name>xyz_2</name>
        </user>
    </users>
</stuff>
'''

stuff_ = ET.fromstring(input)
list_ = stuff_.findall('users/user')
print("Len: ",len(list_))

for user_info in list_:
    print("Name: ", user_info.find('name').text)
    print("ID: ", user_info.find('id').text)
    print("Attr: ", user_info.get('x'))
    print()

'''
output:
Len:  2
Name:  xyz_1
ID:  001
Attr:  1

Name:  xyz_2
ID:  002
Attr:  2
'''





