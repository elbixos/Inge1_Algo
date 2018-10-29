### Cours 5 : rappels stratégie et CC1

#### stratégie

Suite à vos demandes, le début de ce cours a été consacré à la
réalisation d'un exemple de programme.
Il s'agissait de réaliser un programme permettant de gérer le déplacement
d'un drone, simplement en prévoyant les variables et fonctions nécessaires.

- Le drone part d'un point déterminé au début du programme grace au GPS.

- Il doit parcourir une liste de points de passages notés sur une carte (Maps ?)

- Il doit revenir au point de départ et se poser.

- il volera à une altitude prédéterminée (disons 30m)

##### Les variables

- Position actuelle du drone :

Notre programme va gérer la position du drone en l'air.
On pourrait stocker cette position dans un tableau 1D de float
(si ce sont des coordonnées GPS). Ce tableau sera nommé *position*

|x|y|z|
|-|-|-|
|127.14|23.47|30|

- Points de passsage :

On dispose d'une liste de point, reperés par leurs coordonnées 2D (x,y) sur une carte

|x|y|
|-|-|
|127.14|23.47|
|127.14|20.47|
|125.14|20.47|
|125.14|23.47|

Il semble naturel de placer ces points dans un tableau 2D nommé *trajet*

- objectif actuel :
Dans ce trajet, il faut que notre programme sache a chaque instant quel est l'objectif actuel (un des points du tableau).
On peut par exemple stocker l'indice du tableau correspondant a l'objectif actuel.
Cet indice sera noté *iobjectif*

- l'altitude voulue est un simple float.

##### Les fonctions

1. Pour connaitre la position du drone :
il nous faudrait la fonction *lireGPS()* qui renvoie une position (3D)

2. Pour connaitre le trajet a effectuer, on utilisera la fonction lireTrajet() qui renvoie un tableau tel que *trajet*. Cette fonction pourrait lire un fichier par exemple

3. Pour savoir si un objectif est atteint (avec une marge d'erreur) il nous faut connaître la position du drone et la position de l'objectif. On utilisera la fonction *objectifAtteint* qui renvoie True ou False.

3. Pour déplacer le drone, on utilise la fonction *deplacer* a qui l'on communique la position 3D du drone, la position 2D de l'objectif, et l'altitude de vol voulue.

4. Pour faire atterir le drone, on utilise la fonction *atterir*.

##### Le programme principal

```python

depart3D = lireGPS()

trajet = lireTrajet()

altitude = 30.0

# ajoutons le point de départ au trajet.
depart2D = [depart3D[0], depart3D[1]]
trajet.append(depart2D)

# notre premier objectif est dans la case 0 du tableau trajet.
iobjectif  = 0

# décollage
monter(depart3D, altitude)

# la boucle qui gère les déplacement du drone
fini = False
while (fini == False):
  # on récupere la position du drone
  position = lireGPS()

  # on déplace un peu le drone vers l'objectif, à une altitude donnée
  deplacer (position, trajet[iobjectif], altitude)

  # Si l'objectif en cours est atteind
  if (objectifAtteint(position, trajet[iobjectif] )) :
    # on passe à l'objectif suivant
    iobjectif +=1

    # si on a fini tous les objectifs
    # il est temps d'atterrir !
    if iobjectif>= len(trajet):
      fini = True

atterir (départ3D)

```
