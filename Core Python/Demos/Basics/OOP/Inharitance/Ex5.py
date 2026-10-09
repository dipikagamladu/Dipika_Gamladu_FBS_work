
class Game:
    def __init__(self,id,name,players):
        self.id=id
        self.name=name
        self.players=players

    def getId(self):
        return self.id
    def setId(self,nid):
        self.id=nid

    def getName(self):
        return self.name
    def setName(self,nname):
        self.name=nname

    def getPlayers(self):
        return self.players
    def setPlayers(self,nplayers):
        self.players=nplayers

    def display(self):
        print(f'Id={self.id}\t Name={self.name}\t Players={self.players}')


class Cricket(Game):
    def __init__(self,id,name,players,overs):
        super().__init__(id,name,players)
        self.overs=overs

    def getOvers(self):
        return self.overs
    def setOvers(self,novers):
        self.overs=novers

    def display(self):
        super().display()
        print(f'Overs={self.overs}')


class Football(Game):
    def __init__(self,id,name,players,duration):
        super().__init__(id,name,players)
        self.duration=duration

    def getDuration(self):
        return self.duration
    def setDuration(self,nduration):
        self.duration=nduration

    def display(self):
        super().display()
        print(f'Duration={self.duration}')

c1=Cricket(1,'Cricket',11,20)
f1=Football(2,'Football',11,90)

c1.display()
f1.display()