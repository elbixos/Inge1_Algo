
'''
print("Entrez le nombre de notes")
nb = int(input())

somme = 0
for i in range(nb):
    print("Entrez une note")
    note = float(input())
    somme = somme + note

print ("la somme vaut",somme)

moyenne = somme / nb
print("la moyenne vaut :",moyenne)
'''

nb = 0
note = 0
somme = 0
while note >= 0 :
    print("Entrez une note")
    note = float(input())
    
    if note >= 0 :
        somme = somme + note
        nb = nb + 1


print ("la somme vaut",somme)

print("nombre de notes ",nb)
moyenne = somme / nb
print("la moyenne vaut :",moyenne)


