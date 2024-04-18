class Box:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
class Box2(Box):
    def __init__(self,name,rollno,marks):
        self.marks=marks
        Box.__init__(self,name,rollno)

obj1=Box2("Sonia",23,72)
print(obj1.name)
print(obj1.rollno)
print(obj1.marks)

obj2=Box2("Adha",8,91)
print(obj2.name)
print(obj2.rollno)
print(obj2.marks)
