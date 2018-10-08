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




### les fichiers
Les sources de tout ce que nous avons fait dans ce cours sont dans le
répertoire [Sources](../Sources/).
Regardez les fichiers commençants par *04_...* dans l'ordre ou ils sont listés

### Exercices à faire
