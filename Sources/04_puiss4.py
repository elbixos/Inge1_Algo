def afficher(grille):
    lig = len(grille)
    col = len(grille[0])
    for i in range(lig):
        print("|",end="")
        for j in range(col):
            print (grille[i][j], end="|")
        print ("")

    # affichage des chiffres
    print("|",end="")
    for j in range(col):
        print (j,end="|")
    print ("")

def choisir(grille):
    print("choisir la colonne")
    colonne = int(input())

    while grille[0][colonne] != " ":
        print("Impossible, colonne pleine")
        print("choisir une autre colonne")
        colonne = int(input())
    
    return colonne

def tomber(choixCol, grille):
    enBas= 6

    while grille[enBas][choixCol] != " ":
        enBas -=1


    return enBas

def partieFinie(grille,choixLig,choixCol):

    pion = grille[choixLig][choixCol]

    # Verifier horizontalement
    alignes = 0

    # compte a gauche
    j= choixCol
    while grille[choixLig][j] == pion:
        alignes +=1
        j-=1

    print("alignes,vers la gauche", alignes)

    j= choixCol
    while grille[choixLig][j] == pion:
        alignes +=1
        j+=1

    alignes= alignes -1
    print("alignes total", alignes)
    if alignes >= 4:
        return True


    return False


grille = [[" "," "," "," "," "," "," "], [" "," "," "," "," "," "," "], [" "," "," "," "," "," "," "], [" "," "," "," "," "," "," "], [" "," "," "," "," "," "," "], [" "," "," "," "," "," "," "], [" "," "," "," "," "," "," "]]

joueur=1
fini = False

while fini==False:

    afficher(grille)

    choixCol = choisir(grille)
    choixLig = tomber(choixCol,grille)

    if joueur == 1:
        grille[choixLig][choixCol] = "X"
    else:
        grille[choixLig][choixCol] = "O"

    fini = partieFinie(grille,choixLig,choixCol)

    if joueur == 1:
        joueur = 2
    else :
        joueur=1

print("Joueur", joueur, "vous avez...")
