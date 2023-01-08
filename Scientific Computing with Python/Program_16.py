# lesson: Object Lifecycle
# Source: https://www.freecodecamp.org/learn/scientific-computing-with-python
'''
class PartyAnimal:
    x=0

    def __init__(self):
        print("PartyAnimal contructed")

    def party(self):
        self.x = self.x + 1
        print("So far the value of x: ",self.x)

    def __del__(self):
        print("PartyAnimal deconstructed ",self.x)
    
an = PartyAnimal()
an.party()
an.party()

an =23
print('an contains: ',an)
'''
'''
Output:
PartyAnimal contructed
So far the value of x:  1
So far the value of x:  2
PartyAnimal deconstructed  2
an contains:  23
'''
'''
class PA:
    x=0
    def __init__(self,z):
        self.name = z
        print(self.name," is contructed.")
    
    def party(self):
        self.x = self.x + 1
        print(self.name,'party count: ',self.x)

s = PA('sal')
s.party()

j = PA('Jane')
j.party()
j.party()

s.party()
'''
'''
Output:
sal  is contructed.
sal party count:  1
Jane  is contructed.
Jane party count:  1
Jane party count:  2
sal party count:  2
'''

class PartyAnimal:
    x = 0
    name = ''
    def __init__(self, nam):
        self.name = nam
        print(self.name,'constructed')
    def party(self):
        self.x = self.x + 1
        print(self.name,'party count',self.x)

q = PartyAnimal('Quincy')
m = PartyAnimal('Miya')

q.party()
m.party()
q.party()