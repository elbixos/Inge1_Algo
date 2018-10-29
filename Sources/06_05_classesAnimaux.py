
class Animal:

    def __init__(self):
        self.race=""
        self.age=0

    def presenter(self):
        print ("je suis de la race des", self.race)

class Mammifere(Animal):
    def __init__(self):
        Animal.__init__(self)

    def decrireGrossesse(self):
        print ("je porte mes petits dans mon ventre")

class Insecte(Animal):
    def __init__(self):
        Animal.__init__(self)

    def decrireGrossesse(self):
        print ("je ponds des oeufs")

class Chien(Mammifere):
    def __init__(self):
        Mammifere.__init__(self)
        self.race = "chien"

    def cri(self):
        print ("ouaf")

    def decrireGrossesse(self):
        Mammifere.decrireGrossesse(self)
        print ("temps de gestation : 2 mois")

class Chat(Mammifere):
    def __init__(self):
        Mammifere.__init__(self)
        self.race = "chat"

    def cri(self):
        print ("miaou")

    def decrireGrossesse(self):
        Mammifere.decrireGrossesse(self)
        print ("temps de gestation : 9 semaines")

a = Insecte()
a.race = "ravet"

c = Mammifere()
c.race = "vache"

d = Animal()
d.race = "serpent"


a.presenter()
a.decrireGrossesse()

c.presenter()
c.decrireGrossesse()

d.presenter()

e = Chien()
e.presenter()
e.decrireGrossesse()
e.cri()

f = Chat()
f.presenter()
f.decrireGrossesse()
f.cri()
