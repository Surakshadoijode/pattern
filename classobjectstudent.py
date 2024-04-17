class Box:
    def __init__(self,Name,RollNumber,DBMSMarks,PythonMarks,CMarks,OsMarks,CnMarks):
        self.name=Name
        self.rollNumber=RollNumber
        self.dbmsMarks=DBMSMarks
        self.pythonMarks=PythonMarks
        self.cMarks=CMarks
        self.osMarks=OsMarks
        self.cnMarks=CnMarks
    def details(self):
        print(self.name,self.rollNumber,self.dbmsMarks,self.pythonMarks,self.cMarks,self.osMarks,self.cnMarks)
        
Student1=Box("Harika","5A1",78,67,77,89,46)
Student1.details()
Student2=Box("Swapna","5A2",38,65,97,59,41)
Student2.details()
Student3=Box("Sushma","5A3",88,95,47,89,31)
Student3.details()
