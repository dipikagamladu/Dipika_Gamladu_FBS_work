class Student:
    iName='FBS'
    @staticmethod
    def setIName(newiname):
        Student.iName=newiname
    def __init__(self,frn,name,batch):
        self.frn=frn
        self.name=name
        self.batch=batch

        
    def display(self):
        print(f'FRN={self.frn}\t Name={self.name}\t Batch={self.batch}\t IName={Student.iName}')
s1=Student(12,'Gaurav','17April')
s2=Student(22,'Suraj','17Aug')
print(Student.iName)
s1.display()
Student.setIName('Firstbit Solutions')
print(Student.iName)
s1.display()