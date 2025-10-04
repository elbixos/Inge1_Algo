# Quelques exos et leur correction

## Exercice 1

le calcul de l'indice masse corporelle est le suivant :

$$ imc = masse / (taille^2)$$

donner le code d'un programme qui demande à l'utilisateur son poids et sa taille
et affiche son IMC

```Python
print("entrez votre poids (en kg)")
poids = float(input())
taille = float(input())
imc = poids / (taille * taille)
print ("votre imc est :",imc)

```