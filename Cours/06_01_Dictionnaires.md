### Structures de données plus complexes

Au dela des variables primitives et des tableaux, on peut avoir besoin de choses plus spécifiques.
Nous traiterons ici des **tableaux associatifs** et des **classes**

#### Tableaux associatifs

```python
notes={}

notes["Moutoussamy"]=13

notes["Madasaib"]=17

notes["Naejus"] = 21

notes["Naejus"] = 7

print (notes)

for clef in notes :
    print (notes[clef])


for clef in notes :
    print (clef, notes[clef])




images= {}
images["haut"] = "je vais vers le haut"
images["bas"] = "je vais vers le bas"
images["gauche"] = "je cours a gauche"
images["droite"] = "je rampe vers la droite"

direction = "droite"

print (images[direction])

notes2={}

notes2["Moutoussamy"]=[13, 8, 18]

notes2["Madasaib"]=[17, 9, 5]

notes2["Naejus"] = [12, 9, 14]

print (notes2["Naejus"])

print (notes2["Naejus"][1])
```
