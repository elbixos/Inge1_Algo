# Algorithmique CC 2

## Tactique (12 pts)

### Exo 1 (6pts)

Une machine outil perd 10% de sa valeur chaque année. Sa valeur initiale est 10 000 euros. 

- (3 pts) Ecrire un programme qui permet de calculer sa valeur n années après son achat (avec n = 5 par exemple).

- (3 pts) Ecrire un autre algorithme qui affiche le nombre d’années nécessaires pour que la valeur soit divisée par deux.

### Exo 2 (6pts)

- (4 pts) Ecrire le code d'une fonction qui calcule le nombre de chiffres négatifs d'un tableau 2d.

- (2 pts) Ecrire le code du programme qui affiche ce nombre pour le tableau 2d déclaré ci dessous :

tableau = [1,-2,13,7],[4,5,-6,19]]

## Stratégie (8 pts)

Soit un fichier (au format *csv*) contenant les pH et la concentration de la solution résultant d'expériences. Certaines de ces experiences ont réussi, d'autres non.
Le fichier est ainsi constitué :
- une ligne par experience.

- La premiere colonne contient 1.0 si l'experience a réussi, 0.0 sinon.

- La seconde colonne contient le pH de la solution résultat.

- La troisième colonne contient la concentration initiale d'un produit de la solution (pourcentage)

Une de vos hypothèses est que, pour une expérience, **ph x concentration > 12000** est la condition nécessaire et suffisante pour que l'expérience soit réussie.

Vous souhaitez faire un programme qui vous dise si cette hypothèse est correcte.

- (3 pts) Décrivez les variables et les fonctions dont vous auriez besoin.

- (2 pt) Donnez le code de la fonction qui pour une ligne donnée indique si l'hypothèse est correcte.

- (3 pts) Donnez le code du programme principal
