class Student:
    stCount=0
    def __init__(self,frn,name,batch):
        self.frn=frn
        self.name=name
        self.batch=batch
        Student.stCount+=1
    def display(self):
        print(f'FRN={self.frn}\t Name={self.name}\t Batch={self.batch}\t Student Count={Student.stCount}')

class PlacedStudent(Student):
    def __init__(self,frn,name,batch,cName):
        super().__init__(frn,name,batch)
        self.cName=cName

    def setCname(self,cName):
        self.cName=cName
    def getCname(self):
        return self.cName
    def display(self):
        print(f'Company name = {self.cName}')
        super().display()
   
s1=Student(12,'Gaurav','April')
s2=Student(22,'Atharv','Aug')
s3=Student(17,'Rutika','Jul/Aug')
s4=PlacedStudent(1,'Gauri','Jul/Aug','TCS')
s5=PlacedStudent(18,'Virat','Jul/aug','One8')
print(Student.stCount)