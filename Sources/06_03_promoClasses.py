def afficherEtu(e):
    print ("Je m'appelle :", e.nom)
    print ("vous pouvez m'appeler :", e.prenom)
    print ("Je suis né en :", e.anneeNaissance)
    print("voici mes résultats :",e.notes)

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

promo = []

etu = Etudiant()
etu.nom= "Maurice"
etu.prenom = "Francis"
etu.anneeNaissance = 1996
etu.notes=[12,9.5,18]

promo.append(etu)
afficherEtu(etu)

etu = Etudiant()
etu.nom= "Obertan"
etu.prenom = "Melinda"
etu.anneeNaissance = 1998
etu.notes=[14,8.5,16]

promo.append(etu)
afficherEtu(etu)

print("AFFICHAGE FONCTION EXTERNE")
for e in promo:
    afficherEtu(e)

print("AFFICHAGE PAR METHODE INTERNE")
for e in promo:
    e.afficher()
