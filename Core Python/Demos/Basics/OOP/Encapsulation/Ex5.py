class Mobile:
    def __init__(self,id1,brand1,price1):
        self.id=id1
        self.brand=brand1
        self.price=price1

    def getId(self):
        return self.id
    def setId(self,newid):
        self.id=newid

    def getBrand(self):
        return self.brand
    def setBrand(self,newbrand):
        self.brand=newbrand

    def getPrice(self):
        return self.price
    def setPrice(self,newprice):
        self.price=newprice

    def display(self):
        print(f'Id={self.id}\t Brand={self.brand}\t Price={self.price}')
m1=Mobile(101,'Samsung',25000)
m2=Mobile(102,'Redmi',18000)
print(m1.getBrand())
m1.display()
m2.display()
m2.setPrice(20000)
m2.display()