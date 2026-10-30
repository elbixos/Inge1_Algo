---
title:  Algorithmique 
subtitle: CC 1 2026 / 2027
author: v.pagé
geometry: margin=2cm
lancer : pandoc --number-sections --shift-heading-level-by=-1 --syntax-highlighting zenburn 
---

## Exercice 1 (4 pt)

**Question 1** : Sur un compte en banque, on peut effectuer des dépots.

 Donner le code d'une fonction **deposer** permettant d'obtenir le nouveau solde après un dépot en fonction de l'ancien solde et de la somme déposée.

**Question 2** : Si l'on souhaite effectuer un retrait, c'est un peu comme pour un dépot, à ceci près que si la somme que l'on veut retirer est supérieure au solde du compte, le pg doit afficher un message d'erreur ("decouvert autorisé dépassé"). Dans ce cas, le retrait n'a pas lieu et le nouveau solde est identique à l'ancien.

Donner le code d'une fonction **retirer** permettant d'obtenir le nouveau solde après un retrait en fonction de l'ancien solde et de la somme déposée

## Exercice 2 (8 pts)

Sur un compte en banque rémunéré, chaque année, la banque fait le bilan du compte : Elle ajoute les intérêts (un certain pourcentage du solde du compte), et retire des frais de dossiers fixes.

**Attention**, si le solde est négatif, les intérêts sont nuls  

*Exemple :*, si le solde est $S$, que le taux d'intéret est 5% et les frais de dossiers sont de 100 euros, le solde après
prise en compte des intérets est :

- Si $S>= 0$ : $S_{new} = S+ 5/100 \times S - 100$
- Sinon : $S_{new} = S - 100$

Donner le code d'une fonction qui calcule (et renvoie) le nouveau solde à partir de l'ancien solde, des frais de dossiers et du taux d'intérêts.

## Exercice 3 (8 pts)

Faire un programme qui permette à l'utilisateur de saisir le solde initial de son compte.

Puis le programme devra afficher le menu suivant

```
1. Dépot
2. Retrait
3. Bilan annuel
4. Sortie
```

L'utilisateur devra saisir son choix. Dans le cas 1, on lui demandera combien il veut déposer et on effectuera le dépot. Dans le cas 2, il pourra de même effectuer un retrait. Dans le cas 3, la banque fera le bilan de son compte (comme expliqué dans l'exercice 2)

Dans tous ces cas, on affichera le nouveau solde de son compte, puis on lui ré-affichera ce menu pour qu'il puisse continuer a faire des opérations. 

S'il choisit l'option 4, le programme s'arretera en affichant son nouveau solde.



