---
title:  Algorithmique 
subtitle: CC 1 2022 / 2023
author: v.pagé
geometry: margin=2cm
---

## Tactique (15 pts)

On s'interesse à des expériences chimiques. Pour chaque expérience, dépendant de 4 paramètres : pH, Température, Concentration du composant C1, Concentration du composant C2.
Pour chaque expérience, on dispose également du résultat, sous forme d'une quantité de composant C3 crée (ou non par l'expérience).

Toutes ces informations sont stockées sous forme de fichier csv, dans un fichier nommé "experiences_cc2.csv", dans le repertoire courant.
Dans ce fichier, les 5 informations sont stockées sous la forme suivante : 1 expérience par ligne, les informations concernant une ligne sont fournies dans l'ordre précédemment décrit, et séparées par une virgule.

On dispose d'une fonction *lire_csv* qui prend en argument le nom du fichier, et renvoie un tableau 2d, de type ndarray dans lequel chaque case est un float.

### Exo 1 (2 pts)

Donner le code de la portion de programme principal permettant de lire le fichier et de placer le résultat dans un tableau 2D de type ndarray.

### Exo 2 (4 pts)

Faire une fonction qui renvoie un tableau des indices des expériences pour lesquelles la concentration de C1 est supérieure à celle de C2.

Donner le code de la portion de programme principal permettant de trouver ces indices et de les afficher.

### Exo 2 (6 pts)

Faire une fonction qui calcule la moyenne d'une caractéristique, pour certaines lignes seulement.
Par exemple, on voudra connaitre la moyenne du pH pour les expériences 0, 3, 5, 6. Ou encore la moyenne de température pour les experiences 1,2,4,6

Donner le code de la portion de programme principal permettant de trouver la quantité moyenne de C3 produite pour les expériences ou la concentration de C1
est supérieure à celle de C2.

### Exo 2 (3 pts)

Une de nos hypothèses est que si C1 est supérieur à C2, et que le pH est inférieur à 8, alors la quantité de C3 produite est supérieure à 3 (unités non définies).
Donner le code permettant de montrer si, compte tenu de nos experiences, cette hypothèse semble correcte ou est clairement fausse.

## Strategie (5 pts)

