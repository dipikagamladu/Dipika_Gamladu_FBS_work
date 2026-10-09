class BankAccount:
    def __init__(self,number1,name1,balance1):
        self.number=number1
        self.name=name1
        self.balance=balance1

    def getNumber(self):
        return self.number
    def setNumber(self,newnumber):
        self.number=newnumber

    def getName(self):
        return self.name
    def setName(self,newname):
        self.name=newname

    def getBalance(self):
        return self.balance
    def setBalance(self,newbalance):
        self.balance=newbalance

    def display(self):
        print(f'Numnber={self.number}\t Name={self.name}\t Balance={self.balance}')
a1=BankAccount(101,'Bhakti',25000)
a2=BankAccount(102,'Shakti',30000)
print(a1.getName())
a1.display()
a2.display()
a2.setBalance(35000)
a2.display()