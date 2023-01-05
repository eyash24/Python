# lesson: Regular Expression
# Source: https://www.freecodecamp.org/learn/scientific-computing-with-python
'''
^        Matches the beginning of a line
$        Matches the end of a line 
.        Matches any character 
\s       Matches whitespaces
\S       Matches any non-whitespace character
*        Repeats a character zero or more times 
*?       Repeats a character zero or more times (non-greedy)
+        Repeats a character one or more times 
+?       Repeats a character one or more times (non-greedy)
[aeiou]  Matches a single character in the list set
[^XYZ]   Matches a single character not in the list set
[a-z0-9] Set of characters can include a range
(        Indicates where string extraction is to start
)        Indicates where string extraction is to end

# using re.search() like find()
fhand = open('Text.txt')
for line in fhand:
    line = line.rstrip()
    if line.find("From:") >=0:
        print(line)

print()

import re
fhand_2 = open("Text.txt")
for line in fhand_2:
    line = line.rstrip()
    if re.search('From:', line):
        print(line)
'''

# using re.search() like startswith()
fhand = open('Text.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith("From:"):
        print(line)

print()

import re
fhand_2 = open("Text.txt")
for line in fhand_2:
    line = line.rstrip()
    if re.search('^From:', line):
        print(line)

# Wild-card character 
'''
X.*:
X-Sieve: deiwo                  output given : yes
X-DSPAM-Result: Innocent        output given : yes
X-DSPAM-Confidence: 0.3252      output given : yes
X-Content type message: 3480    output given : yes

X.\S+:
X-Sieve: deiwo                  output given : yes
X-DSPAM-Result: Innocent        output given : yes
X-DSPAM-Confidence: 0.3252      output given : yes
X-Content type message: 3480    output given : no
'''

