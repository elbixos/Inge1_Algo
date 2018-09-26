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
Voyons maintenant comment régler ce problème de calcul de moyenne...

#### Manipulations de base sur les tableaux

##### Création d'un tableau
Pour créer un tableau, on peut le créer déja rempli, comme nous l'avons fait. Nous aurions pu également créer un tableau vide et le remplir quand nous voulons (ce qui permettrait d'ajouter des étudiants à n'importe quel moment)

Ce qui suit crée un tableau vide, et le remplit avec des chaines de caractères contenant les noms de chaque étudiant de ma promo.
```python
noms = []

print (noms)

noms.append("moutoussamy")
noms.append("destouches")
print (noms)

noms.append("julan")
print (noms)

noms.append("najeus")
print (noms)
```
##### longueur d'un tableau
il peut être utile de connaitre le nombre de cases d'un tableau nommé *tab* : on l'obtient avec la fonction *len*
```python
nbEtudiants = len(noms)
print (nbEtudiants)
```

##### parcours de tableaux
Si je veux afficher le contenu de chaque case du tableau de notes, je peux utiliser print(notes).
Ici, je vais le faire d'une autre manière, que je réutiliserais de plusieurs façons différentes utilisant toutes la notion de parcours de tableau.
Cela me permettra de faire des choses plus compliquées plus tard (comme calculer la moyenne ou trouver le nom du major de promo).

Si je veux afficher le tableau, ce que je veux faire est en fait afficher successivement le contenu de chaque case.

Je vais donc visiter chaque case du tableau afficher le contenu de la case en cours.

Nous allons voir 3 façon de le faire, chacune ayant ses intérêts (surtout les 2 dernières en fait)

##### parcours d'un tableau avec une boucle while.
je peux le faire comme suit avec la boucle *while* vue dans le cours précédent :
```python
notes = [12, 9.5, 14, 2]

i = 0
while i<4 :
    print(notes[i])
    i = i+1
```
Mais ceci ne marche que pour un tableau de 4 cases. Je peux améliorer ceci facilement en modifiant légèrement mon code en prenant en compte la taille du tableau.

```python
notes = [12, 9.5, 14, 2]

i = 0
while i<len(notes) :
  print(notes[i])
  i = i+1
```
C'est fonctionnel mais peu sympathique a écrire. Voyons une version plus pratique.

##### parcours d'un tableau avec une boucle for.
```python
notes = [12, 9.5, 14, 2]

for e in notes :
  print (e)
```
Dans ce type de boucle, à chaque tour de boucle, la variable *e* va prendre la valeur du contenu de la case visitée. le *for* se débrouille tout seul pour se promener de case en case.

Le code précédent se lit quasiment comme en francais : pour chaque $e$ dans le tableau *notes*, j'affiche *e*

Vous choisissez le nom que vous donnez à la variable qui visite les cases. Le nom du tableau (après *in*) est celui que vous avez donné à votre variable contenant le tableau. Je pourrais tout aussi bien écrire :
```python
notes = [12, 9.5, 14, 2]

for biten in notes :
  print (truc)
```
C'est la version la plus simple pour parcourir tout tableau.

##### parcours avec une boucle for et l'indice de la case
il peut arriver que j'ai besoin de me déplacer dans mon tableau en utilisant le numéro des cases du tableau. C'est ce que nous allons essayer de faire ici...

Commençons par ce code. Vous devriez vite comprendre qu'il affiche les chiffres de 0 à 3.
```python
indices = [0,1,2,3]

for i in indices :
  print (i)
```

Je peux me servir de ce *i* variable pour afficher le contenu de la case numéro *i* d'un tableau, comme ceci :
```python
for i in indices :
  print (notes[i])
```
Le problème est que je dois définir manuellement le tableau indice. Ce qui est pénible, si mon tableau a de nombreuses cases.
Pour générer un tableau allant de 0 à n-1, nous disposons de range(n).
```python
indices  = range(4)
for i in indices :
  print (notes[i])
```
ou encore
```python
for i in range(4) :
  print (notes[i])
```
Mais ceci ne fonctionne que pour des tableaux de 4 cases. Il suffit d'intégrer la longueur du tableau à mon code et c'est réglé :

```python
for i in range(len(notes)) :
  print (notes[i])
```
