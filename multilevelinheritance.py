class Box:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno

class Student:
    def __init__(self,fees):
        self.fees=fees

class Box2(Box,Student):
    def __init__(self,name,rollno,marks,fees):
        self.marks=marks
        Student.__init__(self,fees)
        Box.__init__(self,name,rollno)
class Box3(Box2):
    def __init__(self,sem):
        self.sem=sem
        Box2.__init__(self,"ravi",30,65,70000)

obj=Box3("2-1")
print(obj.sem)

obj1=Box2("Sonia",23,72,10000)
print(obj1.name)
print(obj1.rollno)
print(obj1.marks)
print(obj1.fees)

obj2=Box2("Adha",8,91,50000)
print(obj2.name)
print(obj2.rollno)
print(obj2.marks)
print(obj2.fees)
