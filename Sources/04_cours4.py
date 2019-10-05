
def moyenneEtu(tab, numLigne):
    ## Calculer la moyenne de l'etudiant premier ligne

    somme = 0
    for j in range(1, len(tab[numLigne])):
        somme = somme + tab[numLigne][j]

    moyenne = somme / ( len(tab[numLigne]) -1)

    return moyenne

def afficherMoyennesPromo(tab):
    for i in range(len(tab)):
        nom = promo[i][0]
        moyenne  = moyenneEtu(promo, i)
        print ("Moyenne  : ", nom , moyenne) 

def calculerMoyenneMath(tab):
    somme = 0

    for i in range (len(tab)):
        somme = somme + tab[i][1]

    moyenne = somme / len(tab)

    return moyenne


def calculerMoyennePromo(tab):
    somme = 0
    for i in range (len(tab)):
        somme = somme + tab[i]

    moyenne = somme / len(tab)

    return moyenne

def calculerToutesMoyennesPromo(tab):
    n = len(tab)
   
    ## Creation d'un tableau de n cases rempli de 0
    moyennes = []
    for i in range(n) :
        moyennes.append(0.0)


    for i in range(n):
        nom = promo[i][0]
        moyenne  = moyenneEtu(promo, i)

        moyennes[i] = moyenne

    return moyennes

def afficher(tab):
    print ("Nom\tMath\tInfo\tAnglais")
    nlignes = len(tab)
    ncol = len (tab[0])

    for i in range (nlignes) :
        ligne = tab[i]


        for j in range(ncol):
            print (ligne[j], end="\t")
        print("")
    
def afficherLosersAnglais(tab):
    for i in range(len(tab)):
        note = tab[i][3]
        if tab[i][3] < 10:
            nom = tab[i][0]
            print (nom, " bosse ton TOEIC")


promo = [["Sville", 17,16,11], ["Suarez", 18, 15,7], ["Mayeko", 17, 18,12], ["Daphne", 17, 19,7], ["Apatout", 15, 16,5]]

afficher (promo)

afficherMoyennesPromo (promo)

m = calculerToutesMoyennesPromo (promo)
print (m)


moyennePromo = calculerMoyennePromo(m)
print("Moyenne de la promo :", moyennePromo)

moyenneMath = calculerMoyenneMath(promo)
print("Moyenne math :", moyenneMath)

afficherLosersAnglais(promo)
