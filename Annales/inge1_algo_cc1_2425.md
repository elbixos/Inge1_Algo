---
title:  Algorithmique 
subtitle: CC 1 2024 / 2025
author: v.pagé
geometry: margin=2cm
---

## Exo 1 (6pts)

Calcul d'une moyenne pondérée.
On dispose des notes d'un étudiants dans un tableau nommé **notes**.
On dispose par ailleurs des coefficients de chaque matiere dans un autre tableau nommé **coeff**.

On cherche à calculer la moyenne de cet etudiant, chaque matière étant pondérée par son coefficient. *(Le coefficient d'une matière dans la ième case du tableau de note est indiqué dans la ieme case du tableau de coefficient)*

On pourra prendre par exemple :
```python
notes = [12, 14, 8, 17]
coeff = [2, 1, 6, 1]
```

- (2 pts) Donner le code permettant de calculer la somme des coefficients (dans l'exemple : 10).
*N'utilisez pas la constante 4 comme nombre de cases du tableau, utilisez la fonction len pour la calculer* 
- (4 pts) Donner le code permettant de calculer la moyenne **pondérée** des notes. *Ici encore, n'utilisez pas la constante 4 comme nombre de cases du tableau, utilisez la fonction len pour la calculer*


## Exo 2 (9 pts)

Le prix d'un bien immobilier évolue, d'une année sur l'autre comme suit :

- il gagne 10% de sa valeur courante (s'il valait 10000 euros, il en vaudrait 11000 la premiere année, puis 12100 la seconde) du fait de l'évolution des prix du marché
- Il se déprécie de 800 euros par an à cause de sa vétusté.

Au total, s'il valait 10000 euros au départ, il vaudrait donc 10200 euros l'année suivante

- (3 pts) donner le code qui permet de calculer son prix l'an prochain
du bien, connaissant son prix actuel
- (3 pts) Donner le code permettant de fixer le prix initial d'un bien (10 000 euros), fixer un nombre d'années (10), puis calculer le prix du bien au bout de ces années. On n'affichera que le prix final.
- (3 pts) Donner le code permettant de fixer le prix initial d'un bien (10 000 euros) et de calculer le nombre d'années nécessaires pour que ce prix double. On n'affichera uniquement ce nombre d'années

## Exo 3 (5 pts)
Donner le code qui effectue les opérations suivantes :
- Demander à l'utilisateur combien de nombres il veut saisir
- saisir ces nombres dans un tableau
- demander quelle valeur de **seuil** (nombre décimal) l'utilisateur veut utiliser.
- calculer puis afficher le nombre de chiffres négatifs dont le carré est supérieur au **seuil**.