class Student:
    def __init__(self,Name,id,branch):
        self.Name=Name
        self.id=id
        self.branch=branch
    def details(self):
        print("""Name:{}
ID:{}
Branch:{}""".format(self.Name,self.id,self.branch),end="\n\n")

class Teacher(Student):
    def __init__(self,Name,id,branch):
        self.Name=Name
        self.id=id
        self.branch=branch
            
class HOD(Teacher):
    def __init__(self,Name,id,branch):
        self.Name=Name
        self.id=id
        self.branch=branch
s=Student("Aditya","58469sw4","IT")
t=Teacher("balaraju","4898948465","IT")
h=HOD("Pragati","IT48547","IT")
s.details()
t.details()
h.details()
print("""HOD ID:{}
Teacher ID:{}
Student ID:{}""".format(h.id,t.id,s.id))


    
