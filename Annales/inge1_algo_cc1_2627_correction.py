# la fonction doit connaitre l'ancien solde et la somme déposée. ce seront les parametres de la fonction
def deposer(solde, montant):
    # on calcule le nouveau solde
    nouveau_solde = solde + montant

    # on renvoie le nouveau solde
    return nouveau_solde


# la fonction doit connaitre l'ancien solde et la somme retirée. ce seront les parametres de la fonction
def retirer(solde, montant):
    # on commence par regarder si on peut retirer ce montant

    if montant < solde :
        nouveau_solde = solde - montant
    else :
        # s'il n'y a pas assez de sous
        
        # on affiche un message d'erreur
        print("Solde insuffisant")

        # on calcule le nouveau solde
        nouveau_solde = solde
    
    # qu'on ait fait le retrait ou pas, on renvoie le nouveau solde
    return nouveau_solde


# la fonction doit connaitre l'ancien solde, le taux d'intérêt et les frais de dossiers. ce seront les parametres de la fonction

def bilan(solde, taux, frais):

    # on regarde s'il y a des intérêts
    if solde >=0:
        # si oui, on ajoute les intérêts
        nouveau_solde = solde + taux/100*solde

    # dans tous les cas, on retire les frais de dossiers
    nouveau_solde = nouveau_solde - frais

    # on renvoie le nouveau solde
    return nouveau_solde

# LE PROGRAMME PRINCIPAL

# on commence par saisir le solde initial
print("Entrez votre solde initial")
solde = float(input())

# Puis, on va, en boucle,
#  1. afficher le menu
#  2. saisir le choix de l'utilisateur
#  3. faire ses opérations

# la boucle est un tant qu'il n'aura pas saisi 4 comme choix.

# Pour être sûrs de rentrer une fois dans le while, on définit un choix bidon au départ
choix = 0

while choix != 4:
    # affichage menu
    print("choisissez une option :")
    print("1 : dépot")
    print("2 : retrait")
    print("3 : bilan")
    print("4 : sortir du programme")

    # saisie du choix
    choix = int(input())

    # traitement du choix
    if choix == 1:
        # on doit faire un dépot, on connait le solde initial (solde), mais pas le montant.

        print("Entrez le montant du dépot")
        montant = int(input())

        # on appelle la fonction deposer, en lui donnant l'ancien solde et le montant du dépot.
        # la fonction renvoie le nouveau solde, qui devient le solde actuel.

        solde = deposer(solde, montant)
    elif choix == 2:
        # on doit faire un retrait, on connait le solde initial (solde), mais pas le montant.

        print("Entrez le montant du retrait")
        montant = int(input())

        # on appelle la fonction retirer, en lui donnant l'ancien solde et le montant du retrait.
        # la fonction renvoie le nouveau solde, qui devient le solde actuel.

        solde = retirer(solde, montant)
    elif choix == 3:
        # on doit faire le bila,n, on connait le solde initial (solde), il faut fixer le taux d'intérêt et les frais.
        # Ce n'est pas l'utilisateur qui les fixe
        t = 2.2
        f = 150

        # on appelle la fonction  bilan, en lui donnant l'ancien solde, le taux et les frais
        # la fonction renvoie le nouveau solde, qui devient le solde actuel.

        solde = bilan(solde, t, f)
    elif choix == 4:
        print("ok, va sortir")
    else :
        print("ce choix n'est pas valide")

    # dans tous les cas, on affiche le solde
    print("votre solde est",solde)

