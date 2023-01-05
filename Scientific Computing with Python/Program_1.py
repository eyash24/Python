# lesson: Dictionary and Loops 
# Source: https://www.freecodecamp.org/learn/scientific-computing-with-python
print("hello world")
'''

# counting pattern 
count = dict()
line = str(input("Enter line: "))
print("line: ",line)
words = line.split();
print("Words: ",words)

for w in words:
    count[w] = count.get(w,0)+1; 

print("Count: ", count)

print()

# definite loops and dictionaries
count_2 = {'chuck':1, 'fred':42, 'jan':100}
for key in count_2:
    print(key,":", count_2[key])

print()

# retrieving list of keys and values
print(list(count_2))
print(count_2.keys())
print(count_2.values())
print(count_2.items())

print()

# two iteration variable 
for a, b in count_2.items():
    print(a,":",b)

'''

# Program to find out the most popular word in a text file
text_file = input("Enter name of text file: ")
text_ = open(text_file)

count_ = dict()
for line in text_:
    words = line.split()
    for word in words:
        count_[word] = count_.get(word,0) + 1

popular_word = None
popular_count = None
for word, count in count_.items():
    if popular_count == None or popular_count < count:
        popular_count = count
        popular_word = word

print("Most frequently used word and its count: ", popular_word, popular_count)
print("Count: ",count_)


