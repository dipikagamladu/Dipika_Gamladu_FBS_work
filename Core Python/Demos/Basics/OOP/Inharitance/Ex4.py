
class Product:
    def __init__(self,id,name,price):
        self.id=id
        self.name=name
        self.price=price

    def getId(self):
        return self.id
    def setId(self,nid):
        self.id=nid

    def getName(self):
        return self.name
    def setName(self,nname):
        self.name=nname

    def getPrice(self):
        return self.price
    def setPrice(self,nprice):
        self.price=nprice

    def display(self):
        print(f'Id={self.id}\t Name={self.name}\t Price={self.price}')


class Mobile(Product):
    def __init__(self,id,name,price,camera):
        super().__init__(id,name,price)
        self.camera=camera

    def getCamera(self):
        return self.camera
    def setCamera(self,ncamera):
        self.camera=ncamera

    def display(self):
        super().display()
        print(f'Camera={self.camera}')


class Laptop(Product):
    def __init__(self,id,name,price,ram):
        super().__init__(id,name,price)
        self.ram=ram

    def getRam(self):
        return self.ram
    def setRam(self,nram):
        self.ram=nram

    def display(self):
        super().display()
        print(f'RAM={self.ram}')


p1=Product(1,'Electronic',10000)
m1=Mobile(2,'Redmi',15000,'50MP')
l1=Laptop(3,'HP',45000,'8GB')

p1.display()
m1.display()
l1.display()