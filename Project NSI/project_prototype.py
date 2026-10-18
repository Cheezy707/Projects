def main():
    #parametres initiaux
    hauteur = 100000 
    vitesse_initiale = 1580
    mass_module_initiale = 15000 
    mass_fuel_initiale = 8000
    mass = mass_module_initiale + mass_fuel_initiale 
    temps_entre_commande = 10
    x = 0
    #####################################################################
    #atterisage
    while hauteur != 0:
        print(f"hauteur: {hauteur}")
        print(f"vitesse: {vitesse}")
        fuel = int(input("quantité de fuel à utiliser: "))
        mass -= fuel
        vitesse = calcul_vitesse(mass, hauteur, fuel)
        hauteur = calcul_hauteur(vitesse)
    #####################################################################
    # vitesse impact    
    print(f"vitesse au moment de l'impact: {vitesse}")
    #####################################################################
    # résultat
    if vitesse > x:
        print("mission échouée ! :(")
    else:
        print("mission accomplie ! :)")
    #####################################################################

def calcul_vitesse(vitesse_initiale, mass, hauteur, fuel):
    # acceleration
    G = 6.67*(10**-11)
    M = 7.347*(10**22)
    R = hauteur
    g = (G*M)/(R**2)
    #####################################################################
    # freinage
    frein = fuel * 0
    #####################################################################
    #vitesse
    vitesse += g - frein
    return vitesse
    #####################################################################

def calcul_hauteur(hauteur, vitesse):
    #hauteur 
    hauteur -= vitesse
    return hauteur
    #####################################################################
    
# execution du code
main()
    


