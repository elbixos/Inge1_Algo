### Cours 4 : Structures de données élaborées

Il s'agit ici de disposer de structures un peu plus compliquées que
des variables isolées (vues au [cours 1](01_cours1.md))
ou des tableaux 1D (vus au [cours2](02_cours2.md)

un tableau 1D, c'est ca :

|indices|0|1|2|...|n|
|:---:|
|cases|case 0|case 1|case 2|...|case n|


#### Tableaux 2D

Il peut être intéressant d'avoir sous la main un **tableau 2D** tel que
celui décrit ci dessous.
J'appellerais ce tableau *structure1*

| | col 0 |col 1|col 2|col 3|col 4|col 5|
|:---:|
|ligne 0|case [0,0]|case [0,1]|...|...|...|case[0,5]|
|ligne 1|case [1,0]|...|...|...|...|...|
|ligne 2|case [2,0]|...|...|...|...|case[2,5]|

Dans un tableau comme celui ci, on voudrait pouvoir acceder à la variable
contenue dans la case sur la ième ligne et la jème colonne avec du code comme
celui ci


```python
structure1[0][1] = 5;
```
qui mettrait la valeur 5 dans la case située ligne 0, colonne 1


Toute l'astuce en algorithmique est de recycler ce qu'on a déjà fait.

Il est facile de créer un tableau 2D a partir d'un tableau 1D.
Le tableau 2D est un tableau dont chaque case contient : un tableau...

Voici le schéma correspondant :

| tab2D |
|:---:|
|ligne0|
|ligne1|
|ligne2|

Et chaque ligne est une variable contenant un tableau.
par exemple, *ligne0* serait le tableau suivant.
<table>
<tr>
<td> case [0,0]</td>
<td> case [0,1]</td>
<td> case [0,2]</td>
<td> ...</td>
<td> case [0,5]</td>
</tr>
</table>

Le tout nous donne cette structure pour mon tableau 2D : c'est ma *structure2*
<table>
<tr> <td>
  <table><tr><td> case [0,0]</td><td> case [0,1]</td><td> case [0,2]</td><td> ...</td><td> case [0,5]</td></tr></table>
</td></tr>
<tr> <td>
  <table><tr><td> case [1,0]</td><td> case [1,1]</td><td> case [1,2]</td><td> ...</td><td> case [1,5]</td></tr></table>
</td></tr>
<tr> <td>
  <table><tr><td> case [2,0]</td><td> case [2,1]</td><td> case [2,2]</td><td> ...</td><td> case [2,5]</td></tr></table>
</td></tr>
</table>

Elle est équivalente dans son utilisation au modèle de la *structure1*.
Relisez ca calmement si cela vous pose problème.

#### Implémentation en python.

Maintenant, implémentons ça en python.
Nous allons créer un tableau contenant les noms et les notes de la promo.

```python
promo = [["Moutoussamy", 13],["Madasaib",17]]
```
On aurait pu le créer comme cela aussi :
```python
promo = []
promo.append(["Moutoussamy", 13])
promo.append(["Madasaib",17])
```
Pour l'afficher, pour le moment, je vais faire :
```python
print (promo)
```

Je vous rappelle que mon tableau a la forme suivante :
<table>
<tr> <td>
  <table><tr><td> "Moutoussamy"</td><td> 13</td></tr></table>
</td></tr>
<tr> <td>
  <table><tr><td> "Madasaib"</td><td> 17</td></tr></table>
</td></tr>
</table>

- *promo* est le **tableau externe**.

- *promo[0]* est le **tableau interne** de la première ligne.

- *promo[0][0]* est donc la première case de ce tableau interne et
contient *"Moutoussamy"*

- *promo[0][1]* est la seconde case de ce tableau interne et
contient *13*

Je peux aussi penser directement en termes lignes colonnes en disant :

- *promo[i][j]* est la valeur de la case située ligne *i*, colonne *j*

Pour bien comprendre ces notions, vous pouvez essayer le code suivant
(n'hésitez pas à modifier les chiffres entre crochets) :

```python
print(promo)
print(promo[0])
print(promo[0][1])
```

#### Quelques fonctions qui travaillent sur un seul indice

##### Afficher une ligne
Je veux un programme qui affiche une ligne de mon tableau *promo*

1. je fais une fonction a qui on passe le tableau interne (une ligne)

2. j'appelle cette fonction en lui donnant une case du tableau externe

```python
def afficherEtudiant(ligne) :
    for case in ligne :
        print (case, end = " ")

    print("")
```

je peux appeler cette fonction comme suit dans mon programme principal :

```python
afficherEtudiant(promo[0])
afficherEtudiant(promo[1])
```

J'aurais pu faire ma fonction comme ceci, en changeant la forme du *for*
```python
def afficherEtudiantV2(tabE) :

    for j in range(len(tabE)) :
        print (tabE[j], end = " ")

    print("")

afficherEtudiantV2(promo[0])
afficherEtudiantV2(promo[1])
```

##### Afficher une colonne
Je veux un programme qui affiche les noms contenus dans mon tableau *promo*.
Le problème est que mon tableau promo ne contient pas de structure contenant la colonne.

Je peux m'en sortir comme ceci sur chaque ligne *i*, j'affiche juste la case tab[i][0]

```python
def afficherNoms(tab) :

    for i in range(len(tab)) :
        print (tab[i][0])

afficherNoms(promo)
```



#### Parcours de tableaux 2D
Avec ce que nous avons fait, nous pouvons commencer à nous déplacer à la fois sur les lignes et les colonnes.

Voyons donc un parcours dont l'objectif sera d'afficher correctement toutes les cases du tableau.

Faisons une fonction qui affiche le tableau de la promotion.
Il s'agit, pour chaque ligne du tableau de promo, d'afficher la ligne.
Afficher la ligne sera fait en appelant la fonction *afficherEtudiantV2*.

```python
def afficherTab2D(tab) :

    for i in range(len(tab)) :
        afficherEtudiantV2(tab[i])

afficherTab2D(promo)
```

Si vous comprenez tout ceci, c'est bien. Encore un petit effort :
Je vais faire tout le boulot en une seule fonction.
Le code de la fonction *afficherEtudiantV2* sera intégré à la fonction *afficherTab2D*

```python
def afficherTab2DV2(tab) :

    for i in range(len(tab)) :
      ligne = tab[i]
      for j in range(len(ligne)) :
        print (ligne[j], end = " ")

      print ("")

afficherTab2DV2(promo)
```

Enfin, le code standard pour un programmeur est obtenu en faisant disparaitre la variable *ligne* (je la remplace par *tab[i]*) :

```python
def afficherTab2DV3(tab) :

    for i in range(len(tab)) :

      for j in range(len(tab[i])) :
        print (tab[i][j], end = " ")

      print ("")

afficherTab2DV2(promo)
```
Ceci est appelé une **double boucle imbriquée** (une boucle dans une boucle). Cela terrorise les jeunes informaticiens jusqu'à ce qu'ils les comprennent. Passez donc cette étape au plus vite :

Un programmeur, même débutant, interprètera ce code comme suit :

1. au coeur de la boucle, il y a *print(tab[i][j])* : J'affiche la case de la ligne *i*, colonne *j* d'un tableau 2D.

2. Cette instruction est itérée par la boucle *for* sur *j* : je me déplace donc sur les colonnes : cette boucle affiche toutes les colonnes de la ligne i.

3. Tout ce que je viens de faire est itérée par la boucle *for* sur *i* : cette boucle travaille donc successivement sur toutes les lignes.

J'ai bien une fonction qui parcours toutes les lignes, et pour chaque ligne, affiche le contenu de toutes les colonnes de la ligne.

Allez y calmement, ca va rentrer...


### les fichiers
Les sources de tout ce que nous avons fait dans ce cours sont dans le
répertoire [Sources](../Sources/).
Regardez les fichiers commençants par *04_...* dans l'ordre ou ils sont listés

### Exercices à savoir faire

Vous **devez** être en mesure de faire les exercices suivants :

- faire un programme qui calcule la moyenne de ma promo.

- créer un tableau 2D ou chaque étudiant a 3 notes (3 contrôles continus). On pourra au plus simple avoir quelque chose comme ceci :

<table><tr><td> "Moutoussamy"</td><td> 13</td><td> 12</td><td> 9</td></tr></table>
avec 2 étudiants.

- calculer la moyenne d'un étudiant.

- calculer la moyenne de tous les étudiants au CC 2

- calculer la moyenne de générale de ma promo


Voyons si vous êtes capable de jouer avec des doubles boucles imbriquées, meme s'il n'y a pas de tableau en jeu.
Avant de commencer, on va faire simple :

- faites un programme qui, pour une variable *n = 5* afficherait :
```python
XXXXX
```

- faites un programme qui, pour une variable *n* donnée, afficherait *n* lignes de *n* x. Ex, si *n=5* on afficherait :
```python
XXXXX
XXXXX
XXXXX
XXXXX
XXXXX
```

- faites un programme qui, pour une variable *n* donnée, afficherait une sorte de triangle. Ex, si *n=5* on afficherait :
```python
X
XX
XXX
XXXX
XXXXX
```

- faites un programme qui, pour une variable *n* donnée, afficherait les motifs suivants (alternance sur chaque ligne de 'X' et de '\_')
Ex, si *n=3* on afficherait 3 lignes de 3 caracteres
```python
X_X
X_X
X_X
```
si *n=5* on afficherait 5 lignes de 5 caracteres :
```python
X_X_X
X_X_X
X_X_X
X_X_X
X_X_X
```

- faites un programme qui, pour une variable *n* donnée, afficherait les un damier (alternance sur chaque ligne de 'X' et de '\_')
Ex, si *n=3* :
```python
X_X
_X_
X_X
```
si *n=5* on afficherait 5 lignes de 5 caracteres :
```python
X_X_X
_X_X_
X_X_X
_X_X_
X_X_X
```

___
Vous pouvez repartir vers le [Sommaire](99_sommaire.md)
___
