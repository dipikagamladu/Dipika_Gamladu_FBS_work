class Animal:
    def __init__(self,name,age,weight):
        self.name=name
        self.age=age
        self.weight=weight

    def getName(self):
        return self.name
    def setName(self,newname):
        self.name=newname

    def getAge(self):
        return self.age
    def setAge(self,newage):
        self.age=newage

    def getWeight(self):
        return self.weight
    def setWeight(self,newweight):
        self.weight=newweight

    def display(self):
        print(f'Name={self.name}\t Age={self.age}\t Weight={self.weight}')


class Dog(Animal):
    def __init__(self,name,age,weight,breed):
        super().__init__(name,age,weight)
        self.breed=breed

    def getBreed(self):
        return self.breed
    def setBreed(self,newbreed):
        self.breed=newbreed

    def display(self):
        super().display()
        print(f'Breed={self.breed}\t')


class Cat(Animal):
    def __init__(self,name,age,weight,color):
        super().__init__(name,age,weight)
        self.color=color

    def getColor(self):
        return self.color
    def setColor(self,newcolor):
        self.color=newcolor

    def display(self):
        super().display()
        print(f'Color={self.color}\t')


a1 = Animal('Animal',5,20)
d1 = Dog('Tommy',3,15,'Labrador')
c1 = Cat('Kitty',2,5,'White')

a1.display()
d1.display()
c1.display()