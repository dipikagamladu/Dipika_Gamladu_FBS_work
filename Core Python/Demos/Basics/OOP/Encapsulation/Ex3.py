class Book:
    def __init__(self,id1,name1,price1):
        self.id=id1
        self.name=name1
        self.price=price1

    def getId(self):
        return self.id
    def setId(self,newid):
        self.id=newid

    def getName(self):
        return self.name
    def setName(self,newid):
        self.name=newid

    def getPrice(self):
        return self.price
    def setPrice(self,newid):
        self.price=newid

    def display(self):
        print(f'Id={self.id}\t Name={self.name}\t Price={self.price}')
b1=Book(10,'ThePower',500)
b2=Book(11,'History',300)
print(b1.getName())
b1.display()
b2.display()
b2.setPrice(450)
b2.display()