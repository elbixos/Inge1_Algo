
class Etudiant:

    def __init__(self):
        self.nom=""
        self.prenom=""
        self.anneeNaissance=0
        self.notes=[]

    def afficher(self):
        print ("Je m'appelle :", self.nom)
        print ("vous pouvez m'appeler :", self.prenom)
        print ("Je suis né en :", self.anneeNaissance)
        print("voici mes résultats :",self.notes)

    def ajouterNote(self, note):
        self.notes.append(note)

    def calcMoyenne(self):
        moyenne = 0
        for n in self.notes:
            moyenne += n
        moyenne = moyenne / len(self.notes)

        return moyenne

    def meilleurQue(self,e):
        moyenneMoi = self.calcMoyenne()
        moyenneLui = e.calcMoyenne()

        if moyenneMoi > moyenneLui :
            print (e.nom," t'es un gros loser")
        else :
            print (e.nom," un jour je t'aurais")

promo = []

etu = Etudiant()
etu.nom= "Maurice"
etu.prenom = "Francis"
etu.anneeNaissance = 1996
etu.ajouterNote(12)
etu.ajouterNote(-4)

promo.append(etu)

etu = Etudiant()
etu.nom= "Obertan"
etu.prenom = "Melinda"
etu.anneeNaissance = 1998
etu.notes=[14,8.5,16]

promo.append(etu)

print("AFFICHAGE PAR METHODE INTERNE")
for e in promo:
    e.afficher()
    print(e.calcMoyenne())

promo[0].meilleurQue(promo[1])
