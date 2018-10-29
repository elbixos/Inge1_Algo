def afficherEtu(e):
    print ("Je m'appelle :", e["nom"])
    print ("vous pouvez m'appeler :", e["prenom"])
    print ("Je suis né en :", e["anneeNaissance"])
    print("voici mes résultats :",e["notes"])


promo = []

etu = {}
etu["nom"]= "Maurice"
etu["prenom"] = "Francis"
etu["anneeNaissance"] = 1996
etu["notes"]=[12,9.5,18]

promo.append(etu)

etu = {}
etu["nom"]= "Obertan"
etu["prenom"] = "Melinda"
etu["anneeNaissance"] = 1998
etu["notes"]=[14,8.5,16]

promo.append(etu)

print(promo)

afficherEtu(promo[0])


for e in promo :
    afficherEtu(e)

for i in range(len(promo)) :
    afficherEtu(promo[i])
