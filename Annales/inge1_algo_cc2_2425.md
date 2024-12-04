---
title:  Algorithmique 
subtitle: CC 2 2024 / 2025
author: v.pagé
geometry: margin=2cm
---

Tout le cc va tourner autour du même problème :
la gestion de données météorologiques.

Imaginons que l'on dispose des données de température moyenne mensuelle
pendant un certain nombre d'années. Ces données sont stockées dans un fichier csv nommé *donnees.csv* :

sur chaque ligne sont stockées les données suivantes :
```python
annee, t1, t2,..., t12
```
ce qui donnerait par exemple :
```python
2001,14.5,16.3,17.4,.....
```

## Stratégie (6 points)

On suppose disposer des fonctions suivantes :

- **lire** : Lit les données dans un fichier csv. Arguments : nom du fichier à lire. Retour : un tableau 2D (une liste de liste) contenant les données. Chaque ligne du tableau correspond à une année, chaque colonne correspond à un mois
- **calc_min** : Calcule le minimum d'un tableau 2D. Arguments : un tableau 2D. Retour : la valeur du minimum dans le tableau 2D. *remarque : la fonction ne considère pas la première colonne, qui n'est pas une température, mais une année*
- **calc_moy_ligne** : Calcule la moyenne des températures d'une ligne. Arguments : un tableau 2D, un numéro de ligne. Retour : la moyenne des températures de la ligne indiquée. *remarque : la fonction ne considère pas la première colonne, qui n'est pas une température, mais une année*
- **ecrire_donnees** : Ecrit sur le disque un fichier csv contenant les données d'un tableau 2D. Arguments : le nom du fichier csv à créer, le tableau 2D. Retour : aucun

### A Faire : 
Donner le code du programme principal permettant

1. (2 pt) d'afficher la température minimale rencontrée dans les données du fichier
2. (3 pt) créer un tableau 2D contenant, pour chaque année, le numéro de l'année et la moyenne de température de l'année.
2. (1 pt) sauvegarder dans un fichier csv, pour chaque année, la moyenne de température de l'année. (chaque ligne du fichier csv contiendra alors l'année et la température moyenne). par exemple : 2001,27.9


Si vous avez des problèmes pour les points 2 et 3, vous pouvez simplement afficher l'année et la température moyenne (dans ce cas, tout cela vaut au maximum 2 pts)

## Tactique (14 points)
Dans toute cette partie, je vous demande de faire des fonctions.
Si cela vous pose problème, donnez simplement le code du programme principal qui ferait cela, sans fonction. Vous perdez 1 point par question, mais ne serez pas plus pénalisé.

### Question 1 : **calc_min** (4 pts)

Donner le code de la fonction **calc_min**, décrite précédemment.

### Question 2 : **calc_moy_ligne** (4 pts)

Donner le code de la fonction **calc_moy_ligne**, décrite précédemment.

### Question 2 : Variations de température (6 pts)

Soit $i$ un mois, et $T_i$ la température de ce mois
On appelle **variation de température** entre deux mois la valeur
$$dt = T_i - T_{i+1}$$

pour simplifier, on ne calculera jamais la variation de température entre décembre
et janvier de l'année d'après.

Donner le code d'une fonction qui calcule la variation de température
pour tous les mois d'une ligne du tableau 2D (sauf décembre).
on passera à la fonction le tableau complet, ainsi que le numéro de ligne à traiter.
La fonction renverra un tableau contenant les variations de température dans l'ordre
des mois.

exemple : pour les données
```python
2000,10.5,10.3,10.4,.....
2001,14.5,16.3,17.4,.....
```
si on l'applique à la ligne 1, la fonction renvoie le tableau suivant :
```python
[-1.8, -1.1,.....]
```
