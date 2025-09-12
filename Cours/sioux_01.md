# Les feintes de sioux 1

un petit code qui affecte 32 à la variable a
```python
a = 32
```
C'est juste nécessaire pour que le code suivant fonctionne

## Incrémenter une valeur
```python
a = a + 1
print(a)
```
Ce qui précède augmente la variable a de 1
IL FAUT que a ait déja une valeur AVANT...)

## Opérateur Modulo

```python
b = 23 % 4
print(b)
```
Ce qui précède calcule le reste de la division entière de 23 par 4
(et met le resultat dans a)

Cela permet (entre autres) de tester si un nombre est divisible par un autre (parité, ...), comme ici :

```python
if 23 % 2 == 0 :
    print ("pair")
else :
    print ("impair")
```
