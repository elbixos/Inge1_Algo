## Cours 1

### Concepts d'algorithmique d'aujourd'hui.
Ceci est ma vision de la programmation actuelle. Tout le monde ne s'y retrouvera peut être pas, mais il me semble que la plupart des développeurs en entreprise seront d'accord avec le constat suivant :
Programmer (ou coder) fait appel à deux grands capacités :
- la stratégie
- la tactique

#### La stratégie
C'est, dans le domaine militaire, ce qui vous fait gagner une guerre (*si vous le faites bien et que vous avez de la chance*). C'est la planification vue de loin.

Les généraux, autour d'une table, décident d'envoyer tel bataillon à gauche, pendant que tel autre bataillon partira à droite pour prendre en sandwich l'armée adverse. Ils peuvent aussi planifier de faire un siège pour affamer l'armée ennemie, et quand ils auront faim, ils attaqueront.

#### La tactique
C'est, dans le domaine militaire, ce qui vous fait gagner une bataille (*si vous le faites bien et que vous avez de la chance*). C'est la planification vue de très près.

Le sergent, au coeur du champ de bataille, décide d'envoyer 2 hommes a gauche de la petite colline, pendant que ...

Les sergents font souvent de mauvais généraux, les généraux font souvent de mauvais sergents.

#### Quel rapport avec l'algorithmique et la programmation ?
Prenons un exemple plus ou moins simple : Vous souhaitez faire un programme qui reconnaisse le visage des différents étudiants de la promotion.

Plus précisément, nous devons faire un programme auquel on donne une image, et il doit retrouver le nom de l'étudiant correspondant.

Je vais supposer que nous disposons d'images des visage chaque étudiant de la promotion, associé à son nom.

La partie **Stratégie** c'est la définition des grandes étapes de mon programme. Pour l'exemple, on pourrait penser à quelque chose comme ceci :
lorsqu'on me donne un fichier image à reconnaitre, je vais :

---------
1. lire l'image du fichier -> une image *inconnue*
2. lire l'ensemble de mes images connues -> *maBase*
3. pour chaque image de *maBase* :

  3.1 Je mesure la distance de mon image *inconnue* a l'image connue -> dist

  3.2 Je retiens l'image connue ayant la plus distance *dist* -> *imageLaPlusProche*

4. J'annonce avoir reconnu l'étudiant dont le nom corresspond à *imageLaPlusProche*
----------

Vous ne savez pas lire une image ? Ce n'est pas très grave (internet ou votre sergent le sait)

Vous ne savez pas définir une distance entre deux images ?  Raffinez votre stratégie. Par exemple, une solution classique (assez peu efficace, il faut reconnaître) consiste à calculer la somme des carrés des différences pixel à pixel entre les 2 images.

Tout ce travail n'est pas forcément fait par un informaticien.

La partie **tactique** c'est, pour une partie précise de mon programme, la réalisation d'un algorithme dans un langage donné.

Pour l'exemple, Si je dois faire cette somme des carrés ... je pourrais faire quelque chose comme ceci :

```python
  distance = 0;
  for x in range(len(image1.width) :
    for y in range()(image1.height)) :
      dist += (image1[x][y] - image2[x][y]) **2
```

Vous ne comprenez pas ce code ? c'est normal. Vous devriez en comprendre l'essentiel d'ici quelques cours.

La **tactique**, c'est de la programmation les mains dans le cambouis (*ou dans la boue si on conserve l'image du sergent*)

Les cours d'algorithmique focalisent souvent sur la tactique, alors que les langages actuels permettent d'en faire abstraction assez fréquemment. Par exemple, si je dois trier un tableau par ordre croissant, nous avons, dans tous les langages évolués, des fonctions pour le faire sans faire la moindre boucle.

La **stratégie**, est utile pour programmer mais aussi pour la coordination de n'importe quel projet que vous aurez à réaliser : vous aller choisir d'enchainer des actions, certaines requérant des résultats obtenus par des actions précédentes...

Ce cours a pour objectif de vous apprendre un peu de **tactique** (les variables, les boucles, les fonctions...) et beaucoup de **stratégie**.

Voyons donc le minimum de tactique à savoir pour commencer

### Les variables
Comprenons une chose tout d'abord : un programme informatique ne fait qu'une chose : il manipule des variables. Toutes les informations que doit gérer votre programme doivent donc se retrouver dans des variables. Vous en connaissez vraisemblablement quelques types simples de variables :
- les entiers (int)
- les nombres à virgules (float)
- les vrais ou faux (booleen)
- les chaînes de caractères (string)

Dans les variables, je stocke des valeurs.

```python
  a=5
  b=7
  print(a+b)
```
j'ai créé une variable *a*, lui ai donné la valeur 5, puis crée une variable *b*, lui ai donné la valeur 7,
puis affiché le résultat de la somme des valeurs des deux variables.

### Les tests conditionnel (*if*)
Une grande partie de l'algorithmique consiste a dire ce que l'on fait dans tel ou tel cas. Au coeur de tout ceci se trouve le test conditionnel.
Ici, on fait un programme qui compare la valeur de *a* avec celle de *b*. Si *a* est plus petit, on écrit qu'il est plus petit, sinon, on écrit qu'il est plus grand. Enfin, notre programme continuera à écrire des inepties. Voici la syntaxe en python :

```python
if a < b :
    print ("a est plus petit")
    print ("mais il est vaillant")
else :
    print ("a est plus grand ou égal")

print ("la taille importe peu")
```
Notez le décalage horizontal qui signale ce qui est dans le if, et ce qui ne l'est pas. "Ce qui est dans le if" est appelé **un bloc d'instructions**.

En python, il est décalé (on dit **indenté**) et il y a deux points avant...

Eventuellement, il pourrait être intéressant d'avoir 3 cas :
- *a* < *b*
- *a* > *b*
- *a* = *b*

La solution consisterait à imbriquer des *if* ou a utiliser *elif* (cherchez sur le net, on le verra en cours mais je ne vais pas surcharger ce support)

### Les boucles *Tant que* (while)
Imaginons que je veuille écrire "bonjour à tous" 10 fois. Nous pouvons le faire en répétant 10 fois la ligne suivante :
```python
print ("bonjour à tous")
```
Mais c'est laid et peu efficace (si je veux changer le message en "au revoir à tous", il faudra que je fasse 10 modifications)

L'idée est de répéter une série d'instructions plusieurs fois. On parle d'une boucle (ici, une boucle Tant que ou **while**)

#### une premiere boucle infinie
Voici ce que l'on pourrait faire :
```python
a = 0
while (a == 0)
  print ("bonjour à tous")
  print ("Appuyez sur Ctrl C pour quitter")
```

Le déroulement est le suivant :
1. on initialise *a* à 0
2. on arrive sur la ligne du *while*. On teste si *a* est égal à 0. Si oui, on execute le code du bloc en dessous. Dans notre cas, *a* vaut bien 0.
3. on affiche "bonjour a tous"
4. on affiche "Appuyez"
5. le bloc d'instruction est terminé. On remonte à la ligne du while (comme en 2.) et on recommence (on boucle)

Dit autrement, on effectue des tous de boucle. Avant chaque nouveau tour, on vérifie si la condition est vraie (**True**) ou fausse (**False**)

Dans le cas de notre programme, vu que *a* ne change pas de valeur dans la boucle, nous allons boucler indéfiniment. Pour quitter une boucle infinie, suivez les instructions affichées par notre programme (Ctrl + c)

#### Une boucle qui compte les tours.
En modifiant un peu notre programme, on va se servir de *a* pour compter le nombre de tours que l'on fait...

```python
a = 0
while (a < 3):
  print ("bonjour à tous")
  print ("j'ai fait", a, "tours")
  a = a+1

print ("fin de la boucle")
```
Ici, à chaque tour de boucle, *a*, qui avait commencé à 0, est augmenté de 1. au bout de 3 tours, la condition *a<3* ne sera plus respectée et nous sortirons de la boucle pour afficher "fin de la boucle"

Nous verrons plus tard (ou vous chercherez) un autre célèbre type de boucle, la boucle **for** qui marche bien aussi, mais je n'en n'ai pas besoin pour le moment.

### Les fonctions.
Le code que j'ai présenté juste avant est le programme principal. C'est ce que fait mon programme.

Un vrai bon programme découpe le code en petites actions que le programme principal organise. Si je veux programmer

TODO

### Les fichiers de ce Cours
Les sources de tout ce que nous avons fait dans ce cours sont dans le répertoire [Sources](../Sources/).
On y trouvera en particulier :
- [Les variables, tests, boucles](../Sources/01_intro.py)

___
Vous pouvez repartir vers le [Sommaire](99_sommaire.md)
___
