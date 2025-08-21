# init how to work
class Harry :
    def __init__(self,name,role,tech):
        self.name = name
        self.role = role
        self.tech = tech

harry = Harry("satyajit","dev","python")
print(harry.tech)

class Garry :
    def xprint(self,name,role,tech):
        self.name = name
        self.role = role
        self.tech = tech

aharry = Garry()
aharry.xprint("satyajit","dev","python")
print(aharry.tech)