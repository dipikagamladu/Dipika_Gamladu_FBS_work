class Student:
    def __init__(self,roll1,name1,marks1):
        self.roll=roll1
        self.name=name1
        self.marks=marks1

    def getRoll(self):
        return self.roll
    def setRoll(self,newroll):
        self.roll=newroll

    def getName(self):
        return self.name
    def setName(self,newname):
        self.name=newname

    def getMarks(self):
        return self.marks
    def setMarks(self,newmarks):
        self.marks=newmarks

    def display(self):
        print(f'Roll={self.roll}\t Name={self.name}\t Marks={self.marks}')
s1=Student(101,'karan',85)
s2=Student(102,'Arjun',78)
print(s1.getName())
s1.display()
s2.display()
s2.setMarks(90)
s2.display()