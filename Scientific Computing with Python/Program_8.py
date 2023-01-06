# lesson: Networking: Text Processing and Networking: Using urllib in Python
# Source: https://www.freecodecamp.org/learn/scientific-computing-with-python

print(ord('A'), ord('Z')) # output: 65 90 
print(ord('a'), ord('z')) # output: 97 122
print(ord('0'), ord('9')) # output: 48 57

x=b'abc'
print(type(x)) # output: <class 'bytes'>
y='男'
print(type(y)) # output: <class 'str'>
z='srt'
print(type(z)) # output: <class 'str'>
print()

import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen('https://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())
print()
fhand_2 = urllib.request.urlopen('https://www.dr-chuck.com/page1.html')
for line in fhand_2:
    print(line.decode().strip())