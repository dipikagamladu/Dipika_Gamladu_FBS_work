class Vehicle:
    def __init__(self,number,brand,price):
        self.number=number
        self.brand=brand
        self.price=price

    def getNumber(self):
        return self.number
    def setNumber(self,newnumber):
        self.number=newnumber

    def getBrand(self):
        return self.brand
    def setBrand(self,newbrand):
        self.brand=newbrand

    def getPrice(self):
        return self.price
    def setPrice(self,newprice):
        self.price=newprice

    def display(self):
        print(f'Number={self.number}\t Brand={self.brand}\t Price={self.price}')


class Car(Vehicle):
    def __init__(self,number,brand,price,seats):
        super().__init__(number,brand,price)
        self.seats=seats

    def getSeats(self):
        return self.seats
    def setSeats(self,newseats):
        self.seats=newseats

    def display(self):
        super().display()
        print(f'Seats={self.seats}\t')


class Bike(Vehicle):
    def __init__(self,number,brand,price,cc):
        super().__init__(number,brand,price)
        self.cc=cc

    def getCC(self):
        return self.cc
    def setCC(self,newcc):
        self.cc=newcc

    def display(self):
        super().display()
        print(f'CC={self.cc}\t')


v1 = Vehicle(101,'Tata',800000)
c1 = Car(102,'Honda',1200000,5)
b1 = Bike(103,'Honda',90000,125)

v1.display()
c1.display()
b1.display()