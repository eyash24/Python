# lesson: Python Objects, Objects: A Sample Class
# Source: https://www.freecodecamp.org/learn/scientific-computing-with-python

class PartyAnimal:
    x=0
    def party(self):
        self.x = self.x+1
        print("So far value of x: ",self.x)

an = PartyAnimal()
an.party()
an.party()
an.party()

'''
Output:
So far value of x:  1
So far value of x:  2
So far value of x:  3
'''




