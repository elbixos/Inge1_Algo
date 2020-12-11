def afficher(tab):
    print("    |",end="")
    for j in range(3):
        print (j,end="|")
    print("")

    for i in range (3):
        print(i,": |",end="")
        for j in range(3):
            print (tab[i][j],end="|")
        print("")

        

def saisieValide(tab, lig, col):
    if lig <0 or lig>2:
        print("ligne incorrecte")
        return False

    if col <0 or col>2:
        print("colonne incorrecte")
        return False

    if tab[lig][col]!=" ":
        print("case occupée")
        return False

    return True

def choisir(tab):
    print ("choisir un numéro de ligne")
    lig = int(input())
    print ("choisir un numéro de colonne")
    col = int(input())

    while saisieValide(tab, lig, col) != True:
        print("erreur, recommencez")
        print ("choisir un numéro de ligne")
        lig = int(input())
        print ("choisir un numéro de colonne")
        col = int(input())

    return lig, col

def fini(tab):
    return False

grille = [[" "," "," "],[" "," "," "],[" "," "," "]]
joueur = 1

while fini(grille)==False:
    afficher(grille)
    lig, col = choisir(grille)
    
    if joueur==1:
        pion="X"
    else:
        pion ="O"

    grille[lig][col]=pion

    if joueur==1:
        joueur=2
    else :
        joueur=1


