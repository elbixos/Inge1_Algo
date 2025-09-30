---
title:  Algorithmique 
subtitle: CC 1 2025 / 2026
author: v.pagé
geometry: margin=2cm
lancer : pandoc --highlight-style zenburn
---

## Exo 1 (8 pts)

Calcul d'une moyenne pondérée.

On dispose des notes d'un étudiant dans un tableau nommé **notes**.
On dispose par ailleurs des coefficients de chaque matiere dans un autre tableau nommé **coeffs**.

On cherche à calculer la moyenne de cet etudiant, chaque matière étant pondérée par son coefficient. *(Le coefficient d'une matière dans la ième case du tableau de note est indiqué dans la ieme case du tableau de coefficient)*

- Question 1 (2 pts) Ecrire une fonction *somme* permettant de calculer la somme des éléments d'un tableau.

- Question 2 (2 pts) Donner le code du programme principal permettant de calculer la somme des coefficients des matières (en utilisant la fonction somme).

Votre code commencera, par exemple, par :
```python
notes = [12, 14, 8, 17]
coeffs = [2, 1, 6, 1]
```

- Question 3 (3 pts) Donner le code permettant de calculer la moyenne **pondérée** des notes. *Ici encore, n'utilisez pas la constante 4 comme nombre de cases du tableau, utilisez la fonction len pour la calculer*

## Exo 2 (7 pts)

Le prix d'un bien immobilier évolue, d'une année sur l'autre comme suit :

- il gagne 10% de sa valeur courante (s'il valait 10000 euros, il en vaudrait 11000 la premiere année, puis 12100 la seconde) du fait de l'évolution des prix du marché
- Il se déprécie de 800 euros par an à cause de sa vétusté.

Au total, s'il valait 10000 euros au départ, il vaudrait donc 10200 euros l'année suivante

- (2 pts) Donner le code d'une fonction *prochain_prix* permettant de calculer le prix du bien l'an prochain, connaissant son prix actuel.
- (3 pts) Donner le code du programme principal permettant de fixer le prix initial d'un bien (10 000 euros), fixer un nombre d'années (10), puis de stocker dans un tableau les prix successifs du bien. Afficher le tableau
- (3 pts) Donner le code permettant de fixer le prix initial d'un bien (10 000 euros) et de calculer le nombre d'années nécessaires pour que ce prix double. On n'affichera uniquement ce nombre d'années
