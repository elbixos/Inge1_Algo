---
title:  Algorithmique 
subtitle: correction CC 1 2026 / 2027
author: v.pagé
geometry: margin=2cm
lancer : pandoc --number-sections --shift-heading-level-by=-1 --syntax-highlighting zenburn 
---

## Exercice 1 (4 pt)

**Question 1** : Sur un compte en banque, on peut effectuer des dépots.

Donner le code d'une fonction **deposer** permettant d'obtenir le nouveau solde après un dépot en fonction de l'ancien solde et de la somme déposée.

```python
# la fonction doit connaitre l'ancien solde et la somme déposée. ce seront les parametres de la fonction
def deposer(solde, montant):
    # on calcule le nouveau solde
    nouveau_solde = solde + montant

    # on renvoie le nouveau solde
    return nouveau_solde
```

**Question 2** : Si l'on souhaite effectuer un retrait, c'est un peu comme pour un dépot, à ceci près que si la somme que l'on veut retirer est supérieure au solde du compte, le pg doit afficher un message d'erreur ("decouvert autorisé dépassé"). Dans ce cas, le retrait n'a pas lieu et le nouveau solde est identique à l'ancien.

Donner le code d'une fonction **retirer** permettant d'obtenir le nouveau solde après un retrait en fonction de l'ancien solde et de la somme retirée.

```python
# la fonction doit connaitre l'ancien solde et la somme retirée. ce seront les parametres de la fonction
def retirer(solde, montant):
    # on commence par regarder si on peut retirer ce montant

    if montant < solde :
        nouveau_solde = solde - montant
    else :
        # s'il n'y a pas assez de sous
        
        # on affiche un message d'erreur
        print("Solde insuffisant")

        # on calcule le nouveau solde
        nouveau_solde = solde
    
    # qu'on ait fait le retrait ou pas, on renvoie le nouveau solde
    return nouveau_solde

```

## Exercice 2 (8 pts)

Sur un compte en banque rémunéré, chaque année, la banque fait le bilan du compte : Elle ajoute les intérêts (un certain pourcentage du solde du compte), et retire des frais de dossiers fixes.

**Attention**, si le solde est négatif, les intérêts sont nuls  

*Exemple :*, si le solde est $S$, que le taux d'intéret est 5% et les frais de dossiers sont de 100 euros, le solde après
prise en compte des intérets est :

- Si $S>= 0$ : $S_{new} = S+ 5/100 \times S - 100$
- Sinon : $S_{new} = S - 100$

Donner le code d'une fonction qui calcule (et renvoie) le nouveau solde à partir de l'ancien solde, des frais de dossiers et du taux d'intérêts.

```python

# la fonction doit connaitre l'ancien solde, le taux d'intérêt et les frais de dossiers. ce seront les parametres de la fonction

def bilan(solde, taux, frais):

    # on regarde s'il y a des intérêts
    if solde >=0:
        # si oui, on ajoute les intérêts
        nouveau_solde = solde + taux/100*solde

    # dans tous les cas, on retire les frais de dossiers
    nouveau_solde = nouveau_solde - frais

    # on renvoie le nouveau solde
    return nouveau_solde
```

## Exercice 3 (8 pts)

Faire un programme qui permette à l'utilisateur de saisir le solde initial de son compte.

Puis le programme devra afficher le menu suivant

```
1. Dépot
2. Retrait
3. Bilan annuel
4. Sortie
```

L'utilisateur devra saisir son choix. Dans le cas 1, on lui demandera combien il veut déposer et on effectuera le dépot. Dans le cas 2, il pourra de même effectuer un retrait. Dans le cas 3, la banque fera le bilan de son compte (comme expliqué dans l'exercice 2).

**Oublié dans l'énoncé : le taux d'intéret est de 2.2%, les frais de dossiers de 150 euros**

Dans tous ces cas, on affichera le nouveau solde de son compte, puis on lui ré-affichera ce menu pour qu'il puisse continuer a faire des opérations. 

S'il choisit l'option 4, le programme s'arretera en affichant son nouveau solde.

```python
# on commence par saisir le solde initial
print("Entrez votre solde initial")
solde = float(input())

# Puis, on va, en boucle,
#  1. afficher le menu
#  2. saisir le choix de l'utilisateur
#  3. faire ses opérations

# la boucle est un tant qu'il n'aura pas saisi 4 comme choix.

# Pour être sûrs de rentrer une fois dans le while, on définit un choix bidon au départ
choix = 0

while choix != 4:
    # affichage menu
    print("choisissez une option :")
    print("1 : dépot")
    print("2 : retrait")
    print("3 : bilan")
    print("4 : sortir du programme")

    # saisie du choix
    choix = int(input())

    # traitement du choix
    if choix == 1:
        # on doit faire un dépot, on connait le solde initial (solde), mais pas le montant.

        print("Entrez le montant du dépot")
        montant = int(input())

        # on appelle la fonction deposer, en lui donnant l'ancien solde et le montant du dépot.
        # la fonction renvoie le nouveau solde, qui devient le solde actuel.

        solde = deposer(solde, montant)
    elif choix == 2:
        # on doit faire un retrait, on connait le solde initial (solde), mais pas le montant.

        print("Entrez le montant du retrait")
        montant = int(input())

        # on appelle la fonction retirer, en lui donnant l'ancien solde et le montant du retrait.
        # la fonction renvoie le nouveau solde, qui devient le solde actuel.

        solde = retirer(solde, montant)
    elif choix == 3:
        # on doit faire le bila,n, on connait le solde initial (solde), il faut fixer le taux d'intérêt et les frais.
        # Ce n'est pas l'utilisateur qui les fixe
        t = 2.2
        f = 150

        # on appelle la fonction  bilan, en lui donnant l'ancien solde, le taux et les frais
        # la fonction renvoie le nouveau solde, qui devient le solde actuel.

        solde = bilan(solde, t, f)
    elif choix == 4:
        print("ok, va sortir")
    else :
        print("ce choix n'est pas valide")

    # dans tous les cas, on affiche le solde
    print("votre solde est",solde)


```


