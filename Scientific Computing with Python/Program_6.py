# lesson: Regular Expression: Practical Applications
# Source: https://www.freecodecamp.org/learn/scientific-computing-with-python
'''
data = 'From eyash.prasad24@gmail.com Fri 6 Jan 20:11:35 2023'
at_pos = data.find('@')
print(at_pos) # output: 19
end_pos = data.find(" ",at_pos)
print(end_pos) # output: 29
host = data[at_pos+1:end_pos]
print(host) # output: gmail.com

print() 

# The double split pattern 
word = data.split()
email_id = word[1]
email_list = email_id.split("@")
host_ = email_list[1]
print(host_) # output: gmail.com

print()

# The Regex version 
import re
host_2 = re.findall('@([^ ]*)',data)
print(host_2) # output: ['gmail.com']
print()
host_3 = re.findall('^From .*@([^ ]*)',data)
print(host_3) # output: ['gmail.com']

import re
file_name = input()
fhand = open(file_name)
num_list = list()
for line in fhand:
    line = line.rstrip()
    data = re.findall('^X-DSPAM-Confidence: ([0-9.]+)',line)
    print(len(data))
    if len(data) != 1: continue
    print(data)
    num = float(data[0])
    num_list.append(num)
print(num_list)
print("Max: ", max(num_list)) 
'''
# to have a special regular expression cahracter to just behave normally one prefix it with '\'
import re
x = 'We sell Tshirts at $10.00 per kg.'
y = re.findall('\$[0-9.]+',x)
print(y) # output: ['$10.00']












