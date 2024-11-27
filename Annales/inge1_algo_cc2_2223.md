---
title:  Algorithmique 
subtitle: CC 2 2022 / 2023
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

Il s'agira ici de faire un programme permettant de faire jouer aux echec un joueur humain contre une intelligence artificielle (sans Pat).
Les joueurs sont identifiés par un entier. Un des joueurs (celui que vous voulez) est le joueur 0, l'autre est le joueur 1.
Pour cela, vous disposez des fonctions suivantes :

- *mise_en_place* : aucun argument, renvoie un objet de type plateau_de_jeu, avec les pieces positionnes dessus.
- *demander_coup* : prend un *plateau_de_jeu* comme argument, et demande à un joueur humain quel coup il veut jouer. La fonction vérifie si le coup est légal et redemande en cas de coup illicite. Renvoie un objet de type *coup*.
- *choisir_coup* : prend un *plateau_de_jeu* comme argument et demande à l'IA quel coup elle voudrait jouer. Renvoie un objet de type *coup*. Ce coup est toujours légal.
- *appliquer_coup* : prend en argument un *plateau_de_jeu* et un *coup*. Elle modifie le *plateau_de_jeu* en fonction du *coup* proposé.
- *afficher_plateau* : prend en argument un *plateau_de_jeu* et l'affiche à l'écran
- *vérifier_fin* : prend en argument en plateau de jeu et le numéro du joueur qui va jouer. Renvoie 1 si ce joueur est Mat, 0 sinon.
- *changer_joueur* : prend en argument un entier représentant le numéro du joueur actuel et renvoie un entier représentant le prochain joueur (si on lui passe 0, elle renvoie 1 et si on lui passe 1, elle renvoie 0)

Donnez le code du programme principal qui permet au joueur d'affronter l'IA, puis d'afficher le vainqueur.

Si vous n'y arrivez pas, vous pouvez toujours donner la série d'instructions correspondant à un tour de jeu du joueur humain, ainsi que celle correspondant à un tour de jeu de l'IA.