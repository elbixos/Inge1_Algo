# Explication du principe de la correction
# comme je ne vous fournis qu'un fichier,
# et que je veux qu'il soit fonctionnel
# je dois d'abord faire figurer les fonctions
# y compris celles qui ne sont pas demandées par l'énoncé.
# Je vous les fournis à toutes fins utiles.

## Fonctions

### Vous n'avez pas besoin de savoir faire ceci. je le met juste
### pour que le code fonctionne et vous pouvez regarder par curiosité
def lire(filename):
    donnees = [] # on cree un tableau vide pour mettre les donnes

    # on va lire le fichier ligne par ligne, transformer les donnees d'une
    # ligne en tableau et ajouter ce tableau à données.

    fp = open(filename,"r") # ici, fp "pointe" sur le contenu du fichier
    for ligne in fp: # python va parcourir le fichier ligne par ligne
        # ligne contient donc une ligne du fichier à chaque itération

        ligne = ligne.rstrip() # une petite manip pour supprimer le \n en fin de ligne
        tab = ligne.split(",") # ici, je découpe la chaine en un tableau, en utilisant "," comme séparateur
        tab = [float(x) for x in tab]  # une petite manip pour transformer chaque case en float

        # après tout ca, tab est un tableau de float contenant les données d'une ligne
        
        # obligé de transformer la premiere colonne en int (c'est une année)
        tab[0] = int(tab[0])
        donnees.append(tab) # je l'ajoute à mon tableau de données.
    
    # on ferme l'acces au fichier
    fp.close()
    return donnees


### Vous n'avez pas besoin de savoir faire ceci. je le met juste
### pour que le code fonctionne et vous pouvez regarder par curiosité
def ecrire(filename,donnees):
    # on va ecrire dans le fichier, ligne par ligne

    fp = open(filename,'w') # on ouvre le fichier en ecriture
    for i in range(len(donnees)):
        # pour chaque ligne du tableau de données
        ligne = donnees[i]
        
        # on transforme toute la ligne en str (ce sont des float)
        ligne = [str(x) for x in ligne]

        # on concatene tout ca en séparant par des virgules
        ligne = ",".join(ligne)

        # on ecrit la ligne dans le fichier
        fp.write(ligne)
        fp.write(",")

        # on ajoute un retour chariot en fin de ligne
        fp.write("\n")
    
    # on ferme le fichier
    fp.close()

## Tactique question 1
def calc_min(tab):
    mini = tab[0][1] # premiere case contenant une temperature

    for i in range(len(tab)):
        nb_col = len(tab[i])
        for j in range(1,nb_col):
            if tab[i][j] < mini:
                mini = tab[i][j]
    
    return mini

## Tactique question 2
def calc_moy(tab,i):
    nb_col = len(tab[i])

    somme = 0
    for j in range(1,nb_col):
        somme += tab[i][j]
    moy = somme / (nb_col - 1)

    return moy

## Tactique question 3
def var_temp(tab,i):
    variations = []
    nb_col = len(tab[i])
    for j in range(1,nb_col-1):
        delta = tab[i][j]-tab[i][j+1]
        variations.append(delta)
    
    return variations


## Strategie question 1
nom_fichier = "donnees.csv"
donnees = lire(nom_fichier)
print(donnees)

mini = calc_min(donnees)
print("minimum du tableau",mini)

## Strategie question 2
donnees_out = []
nb_annees = len(donnees)
for i in range(len(donnees)):
    annee = donnees[i][0]
    moy = calc_moy(donnees,i)
    donnees_out.append([annee,moy])

print(donnees_out)

## Strategie question 3
nom_fichier_out = "sorties.csv"
ecrire(nom_fichier_out,donnees_out)

## Pas dans l'enonce, mais teste la variation de temp
i = 1
var = var_temp(donnees, i)
print("variations annees",donnees[i][0],var)
