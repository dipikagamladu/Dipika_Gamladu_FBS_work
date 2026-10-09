class BankAccount:
    def __init__(self,accno,name,balance):
        self.accno=accno
        self.name=name
        self.balance=balance

    def getAccno(self):
        return self.accno
    def setAccno(self,newaccno):
        self.accno=newaccno

    def getName(self):
        return self.name
    def setName(self,newname):
        self.name=newname

    def getBalance(self):
        return self.balance
    def setBalance(self,newbalance):
        self.balance=newbalance

    def display(self):
        print(f'AccNo={self.accno}\t Name={self.name}\t Balance={self.balance}')


class SavingAccount(BankAccount):
    def __init__(self,accno,name,balance,interest):
        super().__init__(accno,name,balance)
        self.interest=interest

    def getInterest(self):
        return self.interest
    def setInterest(self,newinterest):
        self.interest=newinterest

    def display(self):
        super().display()
        print(f'Interest={self.interest}\t')


class CurrentAccount(BankAccount):
    def __init__(self,accno,name,balance,overdraft):
        super().__init__(accno,name,balance)
        self.overdraft=overdraft

    def getOverdraft(self):
        return self.overdraft
    def setOverdraft(self,newoverdraft):
        self.overdraft=newoverdraft

    def display(self):
        super().display()
        print(f'Overdraft={self.overdraft}\t')


b1 = BankAccount(101,'Rahul',50000)
s1 = SavingAccount(102,'Amit',60000,5)
c1 = CurrentAccount(103,'Rohit',80000,20000)

b1.display()
s1.display()
c1.display()