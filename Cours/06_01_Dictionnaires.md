### Structures de données plus complexes

Au delà des variables primitives et des tableaux, on peut avoir besoin de choses plus spécifiques.
Nous traiterons ici des **tableaux associatifs** et des **classes**

#### Tableaux associatifs
Les tableaux associatifs sont les objets permettant de stocker une association entre une **clef** et une **valeur**

Reprenons notre tableau de notes par étudiant.

<table>
<th>indice</th><th>nom</th><th> note </th>
<tr><td>0</td><td> "Moutoussamy"</td><td> 13</td></tr>
<tr><td>1</td><td>"Madasaib"</td><td> 17</td></tr>
</table>

Les tableaux associatifs permettent de remplacer les indices par autre chose (par exemple une chaine de caractères, comme le nom de l'étudiant)

Le nom (la clef) permet ainsi d'accéder à la valeur (la note de l'étudiant)

En **Python** les dictionnaires sont une forme de tableaux associatifs.

##### Dictionnaires, Introduction

On peut créer un dictionnaire et le remplir comme suit :
```python
notes={}

notes["Moutoussamy"]=13

notes["Madasaib"]=17

notes["Naejus"] = 21

print (notes)
```

Pour modifier une note, il suffit de réaffecter la valeur associée à sa clef :
```python
notes["Naejus"] = 7
print (notes)
```

Pour parcourir un dictionnaire, on utilise la syntaxe suivant, qui permet de parcourir les clefs du dictionnaire :
```python
print (notes)

for clef in notes :
    print (notes[clef])
```

Si, lors du parcours, on veut afficher la clef (le nom de l'étudiant) et la valeur (la note associée), on procèderait comme suit :
```python
for clef in notes :
    print (clef, notes[clef])
```

#### Autre application
On peut également se servir de cela pour coder des associations entre une variable et une action à effectuer.

```python
action= {}
action["haut"] = "je monte"
action["bas"] = "je descends"
action["gauche"] = "je cours a gauche"
action["droite"] = "je rampe vers la droite"

direction = "droite"

print (action[direction])
```

#### Stockages plus élaborés
La valeur stockée peut être plus complexe qu'un simple réel. Pour stocker les notes de la promotion la valeur associée à un nom pourrait être le tableau des notes de l'étudiant :

```python
notes2={}

notes2["Moutoussamy"]=[13, 8, 18]

notes2["Madasaib"]=[17, 9, 5]

notes2["Naejus"] = [12, 9, 14]

print (notes2["Naejus"])

print (notes2["Naejus"][1])
```

#### Stockages encore plus élaborés
Je ne ferais jamais ce qui suit dans un programme réel, j'utiliserais plutôt des classes, ce qui fera l'objet de notre prochain cours.

Cependant, cela me permettra de vous montrer deux ou trois choses et de gagner du temps après...

Imaginons que pour chaque étudiant, je veuille stocker :

- son nom

- son prénom

- son annee de naissance

- ses notes.

Je pourrais envisage de stocker les informations relatives à chaque étudiant dans un dictionnaire :

```Python
etu = {}
etu["nom"]= "Doe"
etu["prenom"] = "John"
etu["anneeNaissance"] = 1996
etu["notes"]=[12,9.5,18]
```
Quand je dispose d'un étudiant, je peux afficher ses informations a l'aide d'une fonction telle que *afficherEtu*
```python
def afficherEtu(e):
    print ("Je m'appelle :", e["nom"])
    print ("vous pouvez m'appeler :", e["prenom"])
    print ("Je suis né en :", e["anneeNaissance"])
    print("voici mes résultats :",e["notes"])
```

Je pourrais aussi stocker tous mes étudiants dans un tableau de promo, chaque case contenant un dictionnaire des infos sur l'étudiant...

```python
promo = []

etu = {}
etu["nom"]= "Doe"
etu["prenom"] = "John"
etu["anneeNaissance"] = 1996
etu["notes"]=[12,9.5,18]

promo.append(etu)

etu = {}
etu["nom"]= "Sarr"
etu["prenom"] = "Bouna"
etu["anneeNaissance"] = 1998
etu["notes"]=[14,8.5,16]

promo.append(etu)
```

Pour afficher les infos d'un étudiant de la promo, je ferais par exemple :
```python
afficherEtu(promo[0])
```

pour afficher toutes les infos de toute la promo :
```python
for e in promo :
    afficherEtu(e)
```
