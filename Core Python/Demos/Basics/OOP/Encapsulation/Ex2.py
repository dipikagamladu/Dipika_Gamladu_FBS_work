class Car:
    def __init__(self,color1,brand1,price1):
        self.color=color1
        self.brand=brand1
        self.price=price1

    def getcolor(self):
        return self.color
    def setcolor(self,newcolor):
        self.color=newcolor

    def getBrand(self):
        return self.brand
    def setBrand(self,newbrand):
        self.brand=newbrand

    def getPrice(self):
        return self.price
    def setPrice(self,newprice):
        self.price=newprice

    def display(self):
        print(f'No={self.color}\t Brand={self.brand}\t Price={self.price}')
c1=Car(101,'Tata',800000)
c2=Car(102,'Honda',900000)
print(c1.getBrand())
c1.display()
c2.display()
c2.setPrice(950000)
c2.display()