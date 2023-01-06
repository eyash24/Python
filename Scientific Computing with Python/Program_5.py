# lesson: Regular Expression: Matching and Extracting Data
# Source: https://www.freecodecamp.org/learn/scientific-computing-with-python

# re.search(): returns a true/false on wether the string matches regular expression 
# re.findall(): extracts the matching string 
# [0-9]+ : one or more digit number string  

import re 
'''
x = "My fav 2 numbers are 12 and 56."
y = re.findall('[0-9]+',x)
print(y) # output: ['2', '12', '56']
y_2 = re.findall('[AEIOU]+',x)
print(y_2) # output: []

# Greedy Matching 
x_2 = 'From: Understand me: completely.'
y_3 = re.findall('F.+:',x_2) 
print(y_3) # output: ['From: Understand me:'] 
# Non-Greedy Matching 
y_4 = re.findall('F.+?:',x_2) 
print(y_4) # output: ['From:'] 

x_3 = 'From eyash.prasad24@gmail.com Fri 6 Jan 20:11:35'
y_5 = re.findall('\S+@\S+',x_3)
print(y_5) # output: ['eyash.prasad24@gmail.com']

# parentheses says from where to start and end the string extraction 
y_6 = re.findall('^From (\S+@\S+)', x_3)
print(y_6) # output: ['eyash.prasad24@gmail.com']
'''

s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\\S+@\\S+', s)
lst_1 = re.findall('\S+@\S+', s)
print(lst, lst_1, sep="\n")
print()

