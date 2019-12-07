# Algorithmique CC 1

## Cours (3 pts)

### (1.5 pt) Question 1

Voici un extrait de la documentation de la **méthode** *sort* de la classe *List* (les tableaux que nous utilisons en permanence)
```
    sort(reverse=False)

    This method sorts the list in place, in increasing order, using
    only < comparisons between items. it does not return the sorted sequence.

    reverse is a boolean value. If set to True, then the list elements are
    sorted as if each comparison were reversed
```

Donnez le code d'un programme qui affiche le tableau suivant, trié par ordre décroissant en utilisant la méthode *sort*
```python
tab = [4,12,-15.5,21.3,2]
```
### (1.5 pt) Question 2
Voici un extrait de la documentation de la **fonction** *sorted* intégrée à Python :
```
sorted(iterable, reverse=False)

   Return a new sorted list from the items in iterable.

   reverse is a boolean value. If set to True, then the list elements are
   sorted as if each comparison were reversed.
```

Donnez le code d'un programme qui affiche le tableau suivant, trié par ordre décroissant en utilisant la fonction *sorted*
```python
tab = [4,12,-15.5,21.3,2]
```

## Tactique Et Stratégie (13 pts)

Le gouvernement désire ajouter un jour férié mais il voudrait le faire à une
date éloignée des jours fériés existant. On suppose également que ce jour ne
sera pas inséré entre Noël et le jour de l’an. On va donc calculer le nombre de
jours qui sépare deux jours fériés dont voici la liste pour l’année2007 :

| Fete | date |
|-|-|
| Jour de l’an | 1er janvier 2007 |
| Lundi de Pâques | 9 avril 2007 |
| Fête du travail |1er mai 2007 |
| Victoire de 1945 | 8 mai 2007 |
| Ascension | 17 mai 2007 |
| Lundi de Pentecôte | 4 juin 2007 |
| Fête nationale | 14 juillet 2007 |
| Assomption | 15 août 2007 |
|Toussaint | 1er novembre 2007 |
| Armistice de 1918 | 11 novembre 2007 |
| Noël | 25 décembre 2007 |

Afin de simplifier la tâche, on cherche à attribuer un numéro de jour à chaque
jour férié : Le numéro du lundi de Pâques est
```
31 (mois de janvier) + 28 (février) + 31 (mars)+ 9 = 89.
```

### (4pts) Question 1

La première question consiste à construire une fonction qui calcule le numéro
d’une date étant donné un jour et un mois.
Cette fonction prend comme entrée :
- un numéro de jour
- un numéro de mois
- une liste de 12 nombres correspondant au nombre de jours dans chacun des douze mois de l’année2

### (4pts) Question 2

Si on définit la liste des jours fériés comme étant une liste de couples
(jour, mois) triée par ordre chronologique, il est facile de convertir cette
liste en une liste de nombres correspondant à leur numéro dans l’année.

La fonction à écrire ici appelle la précédente et prend une liste de couples
en entrée et retourne comme résultat une liste d’entiers correspondant à leur
numéro.

### (4pts) Question 3

A partir de cette liste d’entiers, il est facile de calculer l’écart ou le nombre de jours qui séparent deux jours fériés. Il ne reste plus qu’à écrire une fonction qui retourne l’écart maximal entre deux jours fériés, ceux-ci étant définis par la liste de numéros définie par la question précédente.

Ecrire une fonction qui renvoie l'indice dans le tableau du
jour férié qui débute l'ecart maximal. cette fonction prend comme entrée
la liste des couples (jour,mois) des jours fériés.

### (3pts) Question 4

Ecrire le programme principal qui affiche
le nom des deux jours fériés les plus éloignés l’un de l’autre.

Il vous faudra choisir comment stocker l'ensemble des noms et des dates
des jours fériés.
