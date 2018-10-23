# Algorithmique CC 1

## Tactique (12 pts)
Reprenons l'idée du tableau de notes des étudiants de votre promotion.
C'est un tableau 2D tel que :

| note 1| note 2|... |note n |
|-|-|--|---|
|12| 9|...|5|
|...| ...| ...|..|
|13| 12 | ...| 11|

Chaque ligne contient les notes d'un étudiant pout toutes les matières
(colonnes)

1. (2 pts) donner le code qui calcule la moyenne de l'étudiant de la premiere ligne.

2. (2 pts) donner le code de la fonction qui calcule la moyenne de l'étudiant
de la ieme ligne
1
3. (2 pts) donner le code de la fonction qui calcule la moyenne de tous les étudiants
pour la matière de la colonne j.

4. (3pts) donner le code de la fonction qui calcule la moyenne générale de toute
la promotion.

5. (3 pts) faire le programme principal qui demande à l'utilisateur un numéro de ligne,
puis affiche "bravo" si sa moyenne est supérieure à la moyenne de la classe

## Strategie (8 pts)

Nous voulons automatiser la gestion de notes de vos promotions.
Nous voudrions un programme qui lise un fichier contenant les notes de toute la promotion. le format de fichier est bien défini (*csv*)

Dans ce fichier texte, sur chaque ligne, on trouve les données sous la forme :
```
nom de l'étudiant, note1, note2, note 3, ... note 9
```

Votre programme devra :
1. lire le fichier

2. créer un fichier de sortie texte dans lequel on trouve sur chaque ligne :
  nom de l'étudiant, moyenne

3. dans ce fichier de sortie, les étudiants sont triés par ordre de moyenne croissante.

- 2 pts : description des variables

- 3 pts : description des fonctions utilisées

- 3 pts : code du programme principal.
