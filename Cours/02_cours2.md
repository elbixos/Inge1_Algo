## Cours 2

### les tableaux

#### intérêt
Avec les types de variables que nous avons vus dans le cours précédent, nous pouvons faire beaucoup de choses, mais cela devient vite pénible.

Imaginons que je doive faire un programme qui gère vos notes, je doiS stocker une note (un float) par étudiant. Je pourrait par exemple choisir un ordre pour rentrer les notes et stocker la note de chaque étudiant dans une variable.
Disons que ma classe ne contient que 3 étudiants.

```python
e1 = 12
e2 = 9.5
e3 = 14
```
Pour calculer la moyenne de ma promotion, je pourrais ajouter ceci au code qui précède :
```python
moyenne = (e1+e2+e3) / 3
print (moyenne)
```

Si finalement, je dois ajouter un 4eme étudiant arrivé en retard, mon code est transformé à de multiples endroits pour devenir :
```python
e1 = 12
e2 = 9.5
e3 = 14
e4 = 2 # oui, il est mauvais, en plus

moyenne = (e1+e2+e3+e4) / 4
print (moyenne)
```
A chaque ajout d'étudiant, il faudra que je pense a faire toutes les modifications. A terme, je suis sûr de faire une erreur...

De plus, dans le cas de votre promotion, il me faudrait une vingtaine de variables, ce qui devient lourd et pénible. Il est temp d'introduire les tableaux. En python, on les appelle des *listes*, mais c'est sans importance pour nous.

Voici ce que je voudrais : une seule variable contenant ces informations, rangées dans des cases séparées.

| notes |
|---|
|12|
|9.5|
|14|
|2|

Ici, *notes* est le nom de mon tableau.
L'intérêt est simple : si j'ajoute un étudiant, j'ajoute juste une case a mon tableau. **Mes notes ne sont contenues que dans une seule variable** : *notes*

Je peux créer un tableau de ce type comme ceci
```python
notes = [12, 9.5, 14, 2]
print(notes)
```
Pour accéder à une case, je vais utiliser son numéro (on parle d'*indice* de la case). Les indices commencent à 0. Une bonne représentation de mon tableau serait la suivante :

indice | valeur
---|---
0|12
1|9.5
2|14
3|2

Si je veux accéder à la case numéro 2, j'utiliserais l'écriture suivante : notes[2]

Le code suivant :
- affiche la valeur de la case 2 (qui vaut 14)
- puis modifie la valeur de la case 3 pour y mettre la valeur 11
- afficher tout le tableau

```python
print (notes [2])
notes[3] = 11
print(notes)
```

#### Manipulations de base sur les tableaux

Pour créer un tableau, on peut le créer déja rempli, comme nous l'avons fait

parcours d'un tableau avec des boucles.
