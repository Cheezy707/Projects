#import des fonctions de l'autre fichier python 
from module_alu import *
#import de la fonction racine carrée
from math import sqrt
from sys import exit

#fonction principale
def main():
    #initialisation des données
    Z0, V0, M0, Me, dt = info() 
    #affichage du message de départ
    print("\n\n\n")
    print("Bonjour Elon Musk! \nDû à des restricitons techniques, c'est à toi de contrôler le freinage du module lunaire. \nQuand le système te demande d'inserer une donnée, tapes un numéro entre 0 et 9 inclus(0 étant la valeur la moins grande et 9 la plus grande). \nN'aie pas peur! Le programme t'affichera ta vitesse, ton hauteur et la masse de carburant restante après chaque commande.\nBonne Chance! :)")
    print("\n")
    ascii(Z0,V0,0)
    #tant que le module n'a pas aluni
    while abs(Z0) > 1.e-2:
        #affichage des données(vitesse,position et masse de carburant actuelles)
        print(f"Vitesse:{round(V0)} m/s Prochaine commande dans: {round(V0)*dt} m\nPosition: {round(Z0)} m \nMasse de carburant restante: {round(Me)} kg \n")
        #calcul de la poussée, le temps d'application et la masse de carburant restante
        #(la commande de la quantité de carburant à utiliser ch est prise de l'utilisateur et utilisé comme variable au même temps)
        while True:
            try:
                ch = input("Quantitée de carburant à utiliser: ")
                if ch == "":
                        ch = "0"
                if ch == "0" or ch == "1" or ch == "2" or ch == "3" or ch == "4" or ch == "5" or ch == "6" or ch == "7" or ch == "8" or ch =="9":
                    break
                print("Entrez une valeur entre 0 et 9 inclus")
            except KeyboardInterrupt:
                exit()
        Qe,T, Me = Lecture_Cde(V0, Z0, Me, dt, ch)
        #mise à jour de la masse du module
        M0 = M0 - Qe*T
        #calcul de la vitesse et de la position du module (le débit sans dimension de carburant X est calculé et utilisé comme variable au même temps)
        V1,Z1 = VitesseAltitude(V0,Z0,X := Qe*T/M0, T)
        #si le module alunira avec cette nouvelle hauteur
        if Z1 < 1.e-2:
        #-> calcul du temps restant pour l'alunissage
        #-> nouvelles valeurs de la vitesse et la position sont celles lors de l'alunissage
            V1,Z1,T = Alunissage(V0,Z0, M0, Qe)
        #mise à jour de la vitesse
        V0 = V1
        #mise à jour de la position
        Z0 = Z1
        ascii(Z0, V0, ch)
    #affichage du bilan (résultat et vitesse lors de l'alunissage)
    print(bilan(V0))
#appel de la fonction principale(le programme)
main()
