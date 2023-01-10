# lesson: Objects: Inheritance
# Source: https://www.freecodecamp.org/learn/scientific-computing-with-python

class PA:
    x = 0
    name = ""
    def __init__(self, nam):
        self.name = nam
        print(self.name," constructed")
    
    def party_time(self):
        self.x = self.x +1;
        print("x : ",self.x)

class Football_fan(PA):
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        self.party_time()
        print(self.name," points :",self.points)

s = PA("sally")
s.party_time()

j = Football_fan("Jin")
j.party_time()
j.touchdown()

'''
output: 
sally  constructed
x :  1
Jin  constructed
x :  1
x :  2
Jin  points : 7
'''



        