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

##### Les fichiers sources

Les sources de tout ce que nous avons fait dans ce cours sont dans le répertoire [Sources](../Sources/index.md).

#### Les Classes
Ici, on rentre dans le domaine de la **Programmation Orientée Objet** (ou POO pour les intimes).

Nous allons pouvoir programmer des objets qui disposent de propriétés et des fonctions spécifiques...

Reprenons nos étudiants et leurs informations : nous allons créer une **Classe** *Etudiant* qui correspondra à un nouveau type de données.

Pour créer une Classe, on ecrit simplement :
```python
class Etudiant:
```
Tout ce qui concerne cette classe est indenté (décalé vers la droite).

La première chose à faire est de définir ce qu'il faut faire quand on construit un objet de type Etudiant. C'est la fonction *__init__* qui s'en charge (on pourrait parler de **constructeur** de la classe)

Cette fonction est une fonction interne de la classe (ce que l'on appelle une **méthode**). Toutes les méthodes ont comme premier paramètre la variable **self** qui représente l'objet lui même.

D'ou le code suivant :


```python
class Etudiant:
    def __init__(self):
        self.nom=""
        self.prenom=""
        self.anneeNaissance=0
        self.notes=[]
```
Ma classe *Etudiant* dispose d'un constructeur, qui pour chaque objet de type étudiant lui crée un champ *nom*, un champ prénom, un champ *anneeNaissance* et un tableau de notes.


##### Une classe avec des propriétés

Pour créer un objet de type *Etudiant* (on parle d'une **instance** de la classe Etudiant), on procèderait comme suit :

```python
etu = Etudiant()
etu.nom= "Doe"
etu.prenom = "John"
etu.anneeNaissance = 1996
etu.notes=[12,9.5,18]
```

Les champs *nom*, *prenom*, *anneeNaissance* et *notes* sont des **propriétés** de la classe.

Je pourrais faire une fonction qui permette d'afficher les informations relatives à un étudiant comme suit :
```python
def afficherEtu(e):
    print ("Je m'appelle :", e.nom)
    print ("vous pouvez m'appeler :", e.prenom)
    print ("Je suis né en :", e.anneeNaissance)
    print("voici mes résultats :",e.notes)
```
et on peut appeler cette fonction comme suit :
```python
afficherEtu(etu)
```

##### Une classe avec des méthodes

La fonction définie ci-dessus *afficherEtu* est une fonction extérieure à la classe. On peut la transformer en fonction interne à la classe. Cela devient alors une **méthode** de la classe.

Notre classe deviendrait :
```python
class Etudiant:

    def __init__(self):
        self.nom=""
        self.prenom=""
        self.anneeNaissance=0
        self.notes=[]

    def afficher(self):
        print ("Je m'appelle :", self.nom)
        print ("vous pouvez m'appeler :", self.prenom)
        print ("Je suis né en :", self.anneeNaissance)
        print("voici mes résultats :",self.notes)
```
La méthode *afficher* se comprend comme suit :
- son argument est *self*, car une méthode doit disposer d'une variable correspondant à l'objet sur lequel elle travaille.

- dans le corps de la fonction, si l'objet doit afficher son nom, il utilise bien *self.nom* soit "mon nom à moi..."

Nous pouvons maintenant créer un étudiant et afficher ses informations comme suit :

```python
etu = Etudiant()
etu.nom= "Doe"
etu.prenom = "John"
etu.anneeNaissance = 1996
etu.notes=[12,9.5,18]

etu.afficher()
```

Encore une fois, on peut utiliser ces objets en placant nos étudiants dans un tableau représentant la promotion complète :

```python
promo = []

etu = Etudiant()
etu.nom= "Doe"
etu.prenom = "John"
etu.anneeNaissance = 1996
etu.notes=[12,9.5,18]

promo.append(etu)

etu = Etudiant()
etu.nom= "Thauvin"
etu.prenom = "Florian"
etu.anneeNaissance = 1998
etu.notes=[14,8.5,16]

promo.append(etu)
```
et pour afficher le tout
```python
for e in promo:
    e.afficher()
```

Enfin, on peut également préparer quelques méthodes supplémentaires :

- Une méthode qui ajoute une note au tableau de notes :

Cette méthode est intéressante, car elle on lui passe un paramètre (en plus de self) : la note à inserer dans le tableau.

```python
  def ajouterNote(self, note):
    self.notes.append(note)
```

- la méthode qui calcule la moyenne d'un étudiant :

```Python
  def calcMoyenne(self):
    moyenne = 0
    for n in self.notes:
        moyenne += n
    moyenne = moyenne / len(self.notes)

    return moyenne
```

- une méthode qui compare l'etudiant à un autre :

Celle ci est aussi intéressante car on lui passe en argument un autre Etudiant auquel *self* doit se comparer...

```Python
  def meilleurQue(self,e):
    moyenneMoi = self.calcMoyenne()
    moyenneLui = e.calcMoyenne()

    if moyenneMoi > moyenneLui :
        print (e.nom," t'es un gros loser")
    else :
        print (e.nom," un jour je t'aurais")
```
et les appels de ces méthodes :

```python
for e in promo:
    e.afficher()
    print(e.calcMoyenne())

promo[0].meilleurQue(promo[1])
```
#### Les Classes, héritage, surcharge
Ici, nous allons travailler avec un monde rempli d'animaux de toutes sortes. La classe la plus générale sera celle des animaux.

Un animal a une race et un age...
On peut écrire ce qui suit :
```python
class Animal:

    def __init__(self):
        self.race=""
        self.age=0

    def presenter(self):
        print ("je suis de la race des", self.race)
```
Et on peut créer des animaux comme suit :
```python
a = Animal()
a.race = "ravet"

a.presenter()

c = Animal()
c.race = "vache"
c.presenter()
```
Tous les animaux savent se présenter, c'est chouette...

Si l'on veut aller plus loin, nous allons créer une Classe *Mammifere*.
Un Mammifère étant un Animal, nous souhaiterions que notre Mammifère ait aussi une race, un age et sache se présenter. Cela sera obtenu par le fait que la classe *Mammifere* **hérite** de la classe *Animal*, grâce à cette ligne

```Python
class Mammifere(Animal):
```
De plus, quand on construit un Mammifère, on commence par construire un animal. Le constructeur de la classe *Mammifere* appelle donc le constructeur de la classe *Animal*
```python
    def __init__(self):
        Animal.__init__(self)
```

Ajoutons aux objets de la classe  *Mammifere* la méthode qui décrit eur grossesse :
```python
    def decrireGrossesse(self):
        print ("je porte mes petits dans mon ventre")
```

Nous pouvons maintenant créer un Mamifère et utiliser tout ce qu'il sait faire comme suit :

```Python
b = Mammifere()
c.race = "singe"
c.presenter()
c.decrireGrossesse()
```
Il faut noter que la méthode *presenter* vient de la classe *Animal* alors que la méthode *decrireGrossesse* vient de la classe *Mammifere*. Mais comme un Mammifere est un Animal, tout fonctionne.

La classe *Mammifere* **hérite** des méthodes de *Animal*.

On peut aller encore un peu plus loin avec une classe *Chien*

```python
class Chien(Mammifere):
    def __init__(self):
        Mammifere.__init__(self)
        self.race = "chien"

    def cri(self):
        print ("ouaf")

    def decrireGrossesse(self):
        Mammifere.decrireGrossesse(self)
        print ("temps de gestation : 2 mois")
```
Notez que la classe *Chien* propose la méthode *cri* qui donne le cri du chien.

Notez surtout la méthode *decrireGrossesse* qui vient remplacer la méthode du même nom de la classe *Mammifere*. Dans cette méthode, on appelle la méthode de Mammifère (car elle reste valable) et on y ajoute des informations spécifiques aux chiens).

On dit que *decrireGrossesse* **surcharge** la méthode de la classe parente...

Voila !

##### Les fichiers sources





Les sources de tout ce que nous avons fait dans ce cours sont dans le répertoire [Sources](../Sources/index.md).

___
Vous pouvez repartir vers le [Sommaire](99_sommaire.md)
___
