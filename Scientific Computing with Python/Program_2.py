# lesson: The Tuples Collection
# Source: https://www.freecodecamp.org/learn/scientific-computing-with-python
'''
Tuple 
immutable meaning it's content cannot be altered
strings r immutable 

t = tuple()
print(dir(t)) # 'count', 'index'
# dir(x) gives what all can we do with the data type of x 

print()

t_1 = ("A","Z","B","D","K")
print(sorted(t_1))

# tuples and assignmnet
(x, y) = (4, "pet")
print("x, y: ", x, y)

a, b  = 98, 99
print(a,b)

# tuples and dictionaries 
dict_ = {"k1": 3,"k2": 5}
tups = dict_.items()
print(tups)
'''
# comparing tuples 
print((0,1,3)>(1,0,4)) # False
print((1,3,20)>(1,0,4)) # True
print(("Jones","Sal")>("Jones","Sam")) # False
print(("Jones","Sal")>("Adams","Sam")) # True




