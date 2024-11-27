---
title:  Algorithmique 
subtitle: CC 3 2022 / 2023
author: v.pagé
geometry: margin=2cm
---

## Tactique Fonctions (10 pts)

On souhaite faire jouer deux joueurs humains au jeu des allumettes. Dans ce jeu,
le plateau initial est composé de 4 lignes d'allumettes, présenté comme suit :

I
III
IIIII
IIIIIII

Les 2 joueurs jouent à tour de rôle et doivent choisir une ligne sur laquelle il retirent entre 1 et 3 allumettes. Le joueur qui retire la derniere allumette a perdu.

Pour vous simplifier la tache, le plateau peut être vu comme un tableau de 4 case, chaque case contenant le nombre d'allumettes présent sur la ligne correspondante. Le plateau initial peut donc être représenté par la liste python [1,3,5,7]

### Exo 1 (3 pts)
Donner le code de la fonction permettant d'afficher le plateau sous la forme d'une succession de I. Par exemple, si le tableau représentant le plateau contient [0,2,1,3], l'affichage sera
 

II
I
III

*Pour afficher une chaine sans passer à la ligne, le code est :*
```python
print ("message",end='')
```

Donner aussi le code correspondant au programme principal permettant d'initialiser le plateau puis de l'afficher.

### Exo 2 (3 pts)
Imaginons qu'on dispose d'une fonction qui demande à un joueur ce qu'il veut jouer (sans vérification). Cette fonction renvoie un numéro de ligne (entre 0 et 3) et le nombre d'allumettes que ce joueur veut jouer. Quelque chose comme :

```python
def ask_player():
    print("entrez le numéro de ligne")
    lig = int(raw_input())
    
    print ("entrez le nombre d'allumettes a retirer sur la ligne", lig)
    n = int(raw_input())

    return lig,n
```

Donner le code de la fonction **choix_valide** qui vérifie si le joueur peut effectivement jouer le coup qu'il propose, composé d'un numéro de ligne et d'un nombre d'allumettes. Cette fonction renvoie **True** si le choix est valide, et **False** sinon.

### Exo 3 (1 pts)
Imaginons que le choix de l'utilisateur, valide, soit contenu dans des variables *lig* et *n*
Donner le code permettant de retirer *n* allumettes de la ligne *lig* dans le tableau représentant le plateau ?

### Exo 4 (2 pts)
Donner le code d'une fonction qui calcule combien d'allumettes restent sur le plateau.

Donner un exemple d'appel de cette fonction permettant de mettre une variable à True si la partie est terminée.

## Tactique Classes (5 pts)

## Exo 1 (2 pts)
Creer une classe Point permettant de stocker des coordonnées (x,y) de points en 2D.

La fonction d'initialisation prends comme arguments un x et un y et les stocke dans l'objet.

Donnez le code du programme principal permettant de creer les points de coordonnées (0,0) et (1,3)

## Exo 2 (3 pts)
Creez une classe Cercle, permettant de créer un cercle. Lors de sa création, la fonction d'initialisation a comme argument 2 Points : le centre du cercle, ainsi qu'un point du cercle.

donner le code de la méthode permettant de savoir si un point est dans la surface couverte par le cercle.

Donnez le code du programme principal affichant si oui ou non le point (2,2) est dans le cercle de centre (0,0) et passant par (1,3)

## Strategie (5 pts)

On souhaite développer un logiciel de gestion de notes.
Pour cela, on dispose des classes déja écrites suivantes :

- **Etudiant**. Un Etudiant connait son nom, son prénom, sa liste de note, et l'on dispose dans cette classe, entre autres, des méthodes :

    - *valide_annee* (pas d'argument) qui renvoie, en fonction de ses notes, True si l'étudiant valide son année, et False sinon.
    - *get_nom* (pas d'argument) qui renvoie une chaine de caractère contenant le nom de l'étudiant.

- **Promo**. La promotion connait l'ensemble des Etudiants de la promotion. Pour creer une Promotion, sa méthode init prend comme argument le nom d'un fichier csv contenant le nom, le prénom, et toutes les notes de tous les étudiants. La classe Promotion se charge créer tous les Etudiants, et de leur faire stocker leurs notes. Dans cette classe, on dispose, entre autres, d'une méthode :

    - get_etudiants (pas d'arguments) : renvoie la liste (un tableau) des **Etudiant** de la promotion.

Donner le code du programme permettant de créer la promotion à partir d'un fichier nommé "liste_inge1_2023.csv", puis d'afficher le nom des étudiants qui doivent repasser en seconde session.

Si vous n'y arrivez pas, faites un programme qui me dise si le premier étudiant de la promotion valide ou pas son annee (ca vaudra 2 points et c'est peut être un indice pour faire le reste)

