# Quelques exos et leur correction

## Exercice 1 : quelques variables simples

le calcul de l'indice masse corporelle est le suivant :

$$ imc = masse / (taille^2)$$

donner le code d'un programme qui demande à l'utilisateur son poids et sa taille
et affiche son IMC



```python
print("entrez votre poids (en kg)")
poids = float(input())
print("entrez votre taille (en m)")
taille = float(input())
imc = poids / (taille * taille)
print ("votre imc est :",imc)
```

    entrez votre poids (en kg)
    votre imc est : 23.671253629592222
    

## Exercice 2 : une fonction

Faire une fonction qui calcule l'IMC d'une personne
ainsi que le programme qui demande à l'utilisateur son poids, sa taille,
puis utilise la fonction pour afficher l'imc


```python
def calcul_imc(p,t):
    IMC = p/(t*t)
    return IMC

print("entrez votre poids (en kg)")
poids = float(input())
print("entrez votre taille (en m)")
taille = float(input())

imc = calcul_imc(poids, taille)
print ("votre imc est :",imc)

```

    entrez votre poids (en kg)
    entrez votre taille (en m)
    votre imc est : 23.671253629592222
    

## Exercice 3 : un tableau

Faire un programme qui, dans le tableau suivant [3,-1,5,7,-6, 2],
compte les éléments dont le carré est inférieur à 5


```python
tab = [3,-1,5,7,-6, 2]

compteur = 0

# un parcours par valeurs
for val in tab :
    if (val*val < 5):
        compteur = compteur + 1

print("le nombre de valeurs correspondant est :",compteur)


```

    le nombre de valeurs correspondant est : 2
    

## Exercice 4 : un tableau et une fonction

Meme exercice que précédement, mais avec une fonction qui compte les élements

Dans la correction, j'utilise un parcours du tableau par indices.


```python
def compte_trucs(tableau):
    compteur = 0

    # Ici, un parcours par indices
    for i in range(len(tableau)) :
        if (tableau[i]*tableau[i] < 5):
            compteur = compteur + 1
    
    return compteur


tab = [3,-1,5,7,-6, 2]

n = compte_trucs(tab)
print("le nombre de valeurs correspondant est :",n)
```

## Exercice 5 : ajouts dans un tableau

faire un programme qui :

- demande à l'utilisateur combien il veut saisir de notes,
- fasse la saisie
- calcule et affiche la moyenne.

Créez les fonctions de saisie et de moyenne


```python
def saisir(n):
    tab = []
    for i in range(n):
        print("saisissez une note")
        note = float(input())
        tab.append(note)

    return tab

def calcul_moyenne(tab):
    somme = 0
    for val in tab:
        somme += val

    moy = somme / len(tab)
    return moy

print("combien de notes voulez vous saisir ?")
nb = int(input())

notes = saisir(nb)
moyenne = calcul_moyenne(notes)
print("la moyenne est :",moyenne)
```

    combien de notes voulez vous saisir ?
    saisissez une note
    saisissez une note
    saisissez une note
    la moyenne est : 11.0
    
