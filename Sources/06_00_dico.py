

def moyenne(notes, coeffs):
    totalCoeff = 0
    for matiere in coeffs:
        totalCoeff += coeffs[matiere]

    somme = 0
    for matiere in notes:
        somme += notes[matiere] * coeffs[matiere]

    somme = somme/totalCoeff
    return somme


toutEn1 =[]

toutEn1.append(["vpage", "toto0007"])
toutEn1.append(["Astasie", "unTruc"])
toutEn1.append(["Defoe", "unAutreTruc"])


nom = "Safri"
for ligne in toutEn1:
    if ligne[0]== nom:
        print ("TROUVE", "password", ligne[1])


passwords = {}

passwords["vpage"] = "toto0007"
passwords["Defoe"] = "unAutreTruc"
passwords["Safri"] = "encoreAutreChose"
print(passwords["Safri"])

print(passwords["Defoe"])
passwords["Safri"]= "biten"
print(passwords["Safri"])

for machin in passwords:
    print("login ", machin, "password", passwords[machin])

nom = "Astasie"
if not nom in passwords:
    print(nom, "n'est pas la")


notes = {}

notes["Mayeko"]=[9,18,14]
notes["Apatout"]=[8,15,10]

print (notes)



notes2 = {}

notes2["Mayeko"]={}
notes2["Mayeko"]["maths"]= 9
notes2["Mayeko"]["anglais"]= 18
notes2["Mayeko"]["info"]= 14

notes2["Apatout"] = {"maths":8, "anglais": 15, "info":10}

print(notes2)

coeffs = {"maths":3, "anglais":1, "info":2}


somme = 0
for nom in notes2:
    m = moyenne(notes2[nom], coeffs)
    print ("moyenne de ", nom, ":", m)
    somme+= m


print ("moyenne generale ", somme/len(notes2))


