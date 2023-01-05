# lesson: Camparing and sorting tuples
# Source: https://www.freecodecamp.org/learn/scientific-computing-with-python

d = {'a':10,'c':1, 'b':22}
'''
print(d.items())
print(sorted(d.items()))

# Sort by key
for k,v in sorted(d.items()):
    print(k,v)

# Sort by value
tmp = list()
for k,v in sorted(d.items()):
    tmp.append((v,k))

print(tmp)
tmp = sorted(tmp, reverse=True)
print(tmp)

# Program to print top 10 most common words
file_ = input("File name: ")
text = open(file_)

count_ = dict()
for line in text:
    word = line.split()
    for w in word:
        count_[w] = count_.get(w,0) + 1

lst = list()
for k,v in count_.items():
    lst.append((v,k))

lst = sorted(lst, reverse = True)

for v, k in lst[:10]:
    print(k,v)
'''

c = {'a':12,'c':10,'b':0}
print(sorted([ (v,k) for k,v in c.items()]))
print("Reverse version: ",sorted([ (v,k) for k,v in c.items()], reverse=True))
