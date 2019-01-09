import csv

def lireCSV(filename)
    csvFile = open(filename)

    mapromo = []

    lecteur = csv.reader(csvFile, delimiter=',')
    i=0
    for ligne in lecteur:
        print(ligne)
        if i > 0 :
            etu = Etudiant()
            etu.nom= ligne[0]
            etu.prenom= ligne[1]
            etu.moisNaissance = ligne[2]
            etu.anneeNaissance = ligne[3]
            etu.ajouterNote(float(ligne[4]))
            etu.ajouterNote(float(ligne[5]))
            etu.ajouterNote(float(ligne[6]))
            mapromo.append(etu)
        i+=1

    csvFile.close()

    return mapromo

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



filename = '07_01_exempleCsv.csv'

promo = lireCsv(filename)

print("j'ai lu ",i, " lignes ")

print("AFFICHAGE PAR METHODE INTERNE")
for e in promo:
    e.afficher()
    print(e.calcMoyenne())

csvfile = open('07_03_resu.csv', 'w')

ecriteur = csv.writer(csvfile, delimiter=',')

for e in promo:
    print (e.nom, e.calcMoyenne())
    ecriteur.writerow([e.nom,e.calcMoyenne()])

csvFile.close()
