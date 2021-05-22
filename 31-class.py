class PartyAnimal:
    x=0
    name=""
    def __init__(self,z):
        self.name=z
        print(self.name, "constructed")

    def party(self):
        self.x=self.x+1
        self.name=self.name+" Rahman"
        print(self.name,"party count:",self.x)

class Football(PartyAnimal):
    goal=0
    def match(self):
        self.x=self.x+8
        self.party()
        print(self.name,"scored",self.goal)

s=PartyAnimal("Sally")
s.party()

j=PartyAnimal("Jim")
j.party()
s.party()

k=Football("Nirab")
k.party()
k.match()
