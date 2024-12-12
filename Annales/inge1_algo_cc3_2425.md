---
title:  Algorithmique 
subtitle: CC 3 2024 / 2025
author: v.pagé
geometry: margin=2cm
---

## Tactique - Fonctions (9 pts)
Soit un fichier (au format *csv*) contenant les pH et la concentration de la solution résultant d'expériences. Certaines de ces experiences ont réussi, d'autres non.
Le fichier est ainsi constitué :

- une ligne par experience.
- La premiere colonne contient 1.0 si l'experience est réussie, 0.0 sinon.
- La seconde colonne contient le pH de la solution résultat.
- La troisième colonne contient la concentration initiale d'un produit de la solution (pourcentage)

On supposera pouvoir lire le fichier et en faire un tableau 2D ayant la meme structure

### Question 1 (3 pts)
Donner le code d'une fonction **experience_reussie** à laquelle on passe le tableau 2D,
et le numéro de ligne.
La fonction doit renvoyer **True** si l'expérience correspondant à cette ligne est réussie, et **False** sinon.

### Question 2 (3 pts)
Donner le code d'une fonction **condition_vérifiée** à laquelle on passe le tableau 2D, et le numéro de ligne.
La fonction doit renvoyer **True** si la condition **ph x concentration > 12000** est vraie, et **False** sinon.

### Question 3 (3 pts)
Notre *hypothèse* est que, pour une expérience, **ph x concentration > 12000** est la condition nécessaire et suffisante pour que l'expérience soit réussie.

Donner le code d'une fonction **hypothèse_valide** à laquelle on passe le tableau 2D, et le numéro de ligne.
La fonction doit renvoyer **True** si notre hypothèse est valide d'après l'expérience et **False** sinon.

*Remarque : L'hypothèse est valide selon notre hypothèse si :*

- *l'experience est réussie et la condition vérifiée*
- *l'experience est ratée et la condition non vérifiée*

## Stratégie - fonctions (6 pts)
Vous souhaitez faire un programme qui vous dise si cette hypothèse semble correcte.
Elle est correcte si elle est valide pour toute les lignes.
Nos données sont dans un fichier nommé *chimie.csv*.

Vous disposez d'une fonction **lire** à laquelle on donne le nom du fichier
et qui renvoie le tableau 2D correspondant.

Vous disposez également de toutes les fonctions de la partie *Tactique*

### A Faire
Donnez le code du programme qui regarde dans le fichier et affiche "l'hypothese semble vraie" si l'hypothèse est vérifiée pour toutes les lignes du tableau.

Dans le cas contraire, le programme affichera "l'hypothèse est fausse".

## Stratégie - Objets (5 pts)

On souhaite développer un logiciel de gestion de notes.

On dispose d'un fichier (csv) nommé *"notes.csv"* contenant les noms, les prénoms
et toutes les notes des étudiants.

On dispose aussi d'une fonction *lire* qui permet de lire un fichier de notes
et renvoie un tableau dont chaque case est un objet de type **Etudiant** (voir ci dessous). Le seul argument de la fonction lire est le nom du fichier.

Chaque objet de type **Etudiant**. connait son nom, son prénom, sa liste de note, et l'on dispose dans cette classe, entre autres, des méthodes :

    - *valide_annee* (pas d'argument) qui renvoie, en fonction de ses notes, True si l'étudiant valide son année, et False sinon.
    - *get_nom* (pas d'argument) qui renvoie une chaine de caractère contenant le nom de l'étudiant.

### A faire 
Donner le code du programme permettant d'afficher le nom des étudiants qui doivent repasser en seconde session.

Si vous n'y arrivez pas, faites un programme qui indique si le premier étudiant de la promotion valide ou pas son annee (ca vaudra 2 points et c'est peut être un indice pour faire le reste)
