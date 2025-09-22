def produit_v_moisie():
    print("entrez un nombre")
    n=int(input())

    prod = 1
    for i in range(1,n+1):
        prod = prod*i
    #print("la fonction sait que ton resu vaut",prod)
    return prod

def produit(n):
    prod = 1
    for i in range(1,n+1):
        prod = prod*i
    #print("la fonction sait que ton resu vaut",prod)
    return prod

print("la version moisie")
resu = produit_v_moisie()
print("le resu vaut",resu)

print("la bonne version")
for val in [2,5,3]:
    resu = produit(val)
    print("\t le resu vaut",resu)
