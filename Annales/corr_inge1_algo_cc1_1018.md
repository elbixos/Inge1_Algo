# Correction CC1 2018 2019

L'énoncé est [ici](inge1_algocc1_1018.md).

## Partie 1 Tactique :

1. moyenne de l'étudiant de la premiere ligne

```python
nbNotes = len(tab[i])

moyenne =0
for j in range(nbNotes) :
  moyenne += tab[0][j]

moyenne = moyenne / NbNotes
```

2. fonction pour la moyenne de l'étudiant de la *i* ème ligne

```python
def moyenneEtu(tab, i)
  nbNotes = len(tab[i])
  moyenne =0
  for j in range(nbNotes) :
    moyenne += tab[i][j]

  moyenne = moyenne / NbNotes
  return moyenne
```

3. fonction pour la moyenne sur la matière de la *j* ème colonne

```python
def moyenneMatiere(tab, j)
  nbEtu = len(tab)

  moyenne =0
  for i in range(nbEtu) :
    moyenne += tab[i][j]

  moyenne = moyenne / NbEtu)
  return moyenne
```

4. fonction qui calcule la moyenne générale de toute
la promotion.

```python
def moyenneGen(tab)
  nbNotes = len(tab[0])

  moyenne =0
  for j in range(nbNotes) :
    moyenne += moyenneMatiere(tab, j)

  moyenne = moyenne / NbNotes)
  return moyenne
```

5. (3 pts) Programme principal

```python
print("Entrez le numéro de ligne de l'étudiant")
numEtu = int(input())

mEtu = moyenneEtu(tab, numEtu)

mGen = moyenneGen(tab)

if mEtu > mGen :
  print("Bravo")
```
