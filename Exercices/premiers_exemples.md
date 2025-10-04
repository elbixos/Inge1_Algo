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
    
