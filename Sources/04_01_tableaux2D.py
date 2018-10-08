def afficherEtudiant(tabE) :

    for info in tabE :
        print (info, end = " ")

    print("")

def afficherEtudiantV2(tabE) :

    for i in range(len(tabE)) :
        print (tabE[i], end = " ")

    print("")

def afficherPromo(tab) :

    for e in tab :
        afficherEtudiant(e)

def afficherPromoV2(tab) :

    for e in tab :
        afficherEtudiantV2(e)

def afficherTab2D(tab) :

    for ligne in tab :
        for col in ligne :
            print (col, end = " ")

        print("")

def afficherTab2DV2(tab) :

    for i in range(len(tab)) :
        ligne = tab[i]
        for j in range(len(ligne)) :
            print (ligne[j], end = " ")

        print("")

def afficherTab2DV3(tab) :

    for i in range(len(tab)) :
        for j in range(len(tab[i])) :
            print (tab[i][j], end = " ")

        print("")

def calculMoyenne(tab) :
    somme = 0

    for i in range(len(tab)) :
        somme = somme + tab[i][1]

    moyenne = somme / len(tab)

    return moyenne

promo = [["Moutoussamy", 13],["Madasaib",17]]

print (promo)

promo1 = []

e = ["Moutoussamy", 13]
promo1.append(e)

promo1.append(["madasaib",7])

promo1[1] = ["Madasaib",17]

print (promo1)

afficherEtudiant(promo[0])
afficherEtudiant(promo[1])

print("==========")
afficherPromo(promo)

print("==========")
afficherPromoV2(promo)

print("==========")
afficherTab2DV2(promo)

print("==========")
afficherTab2DV3(promo)

print("==========")
afficherTab2D(promo1)

print("==========")
print ("moyenne ", calculMoyenne(promo))
