
""" programme de simulation d'alunissage basé sur le programme BASIC LUNAR
    de Jim Storer sur PDP-8 en 1969
"""
#import de la librairie numpy sous le nom "np"
import numpy as np
from random import randint

#initialisation des constantes en unité SI (kg/m/s)
g  = 1.6     #gravité
Ue = 2900    #vitesse d'ejection

def Lecture_Cde(V0: float,Z0: float,Me: int,dt: float,ch: int) -> tuple:
    #Cette fonction prend en paramètre:
    #   -la vitesse actuelle du module V0
    #   -la position actuelle du module Z0
    #   -la masse restante de carburant Me
    #   -le temps entre chaque commande dt
    #   -la quantité de carburant à utiliser ch (comprise entre 1 et 9 inclus)
    #Elle renvoie la poussée Qe, son temps d'application T ainsi que la masse restante de carburant Me sous forme de tuple .

    #permet d'utiliser la gravité qui est une variable globale
    global g
    #calibration du temps
    T=dt
    #s'il reste du carburant
    if Me>0 :
        #calcul de la poussée Qe
        Qe = int(ch)*10
        #si la réserve  de carburant est insuffisante
        if (Me-Qe*T)<0 :
            #calcule le temps restant d’utilisation du carburant
            T = Me/Qe
    #s'il ne reste plus de carburant
    else:
        #afficher qu'il ne reste plus de carburant
        print("Plus de carburant\nTu ne peux donc plus freiner\n")
        #la poussé est donc nulle
        Qe = 0
        #calcul du temps restant d’utilisation du carburant (ici = temps restant jusqu'à l'alunissage)
        T = (-V0 + np.sqrt(V0*V0 + 2*g*Z0)) / g
    #mise à jour de la masse restante de carburant
    Me = Me - Qe*T
    #renvoie la poussée Qe, son temps d'application T et la masse restante de carburant Me
    return Qe,T,Me

def VitesseAltitude(V0: float,Z0: float,X: float,T: int) -> tuple:
    #Cette fonction prend en paramètre:
    #   -la dernière vitesse du module V0
    #   -la dernière position du module Z0
    #   -le débit sans dimension de carburant X(Qe*T/M0)
    #   -le temps d'application de la poussée T
    #Elle renvoie la vitesse actuelle du module V et la position actuelle du module Z sous forme de tuple .

    #permet d'utiliser la gravité et la vitesse d'ejection qui sont des variables globales
    global g,Ue
    #calcul de la nouvelle vitesse
    V = V0 + g*T - Ue*(X + X*X/2. + X**3/3. + X**4/4. + X**5/5.)
    #calcul de la nouvelle position
    Z = Z0 - V0*T - g*T*T/2. + Ue*T*(X/2. + X*X/6. + X**3/12. + X**4/20. + X**5/30.)
    #renvoie la vitesse actuelle du module V et l'altitude actuelle du module Z
    return V,Z

def Alunissage(V0: float,Z0: float,M0: float,Qe: float) -> tuple:
    #Cette fonction prend en paramètre:
    #   -la vitesse actuelle du module V0
    #   -la position actuelle du module Z0
    #   -la masse actuelle du module M0
    #   -la valeur de la poussée Qe
    #Elle renvoie la vitesse du module V0 et la position actuelle du module Z0 lors de l'alunissage ainsi que le temps restant jusqu'à l'alunissage T0 sous forme de tuple .
    
    #permet d'utiliser la gravité et la vitesse d'ejection qui sont des variables globales
    global g,Ue
    #création de la variable T0 qui correspond au temps restant jusqu'à l'alunissage 
    T0 = 0
    #tant que le module n'a pas aluni:
    while np.abs(Z0) > 1.e-2:
            #caclul du temps d'application de la poussée
            T= (-V0 + np.sqrt(V0*V0 + 2*(g-Ue*Qe/M0)*Z0)) / (g-Ue*Qe/M0)
            #calcul de la nouvelle vitesse et de la nouvelle altitude 
            V0,Z0 = VitesseAltitude(V0,Z0,Qe*T/M0,T)
            #calcul du temps restant jusqu'à l'alunissage
            T0 += T
    #renvoie la vitesse V0 et l'altitude Z0 lors de l'alunissage ainsi que le temps restant jusqu'à l'alunissage T0 
    return V0,Z0,T0

def bilan(V0):
    #cette fonction prend la vitesse lors de l'impact V0 en paramètre et en déduit le résultat de la mission 
    #pour ensuite en faire un bilan sous forme de str.

    #la mission a échoué par défaut
    resulat = False
    #si la vitesse était quasi nulle lors de l'impact
    if V0 < 1:
        #la mission a été accomplie avec succès
        resultat = True
    #selon le resultat de la mission,choisir la bonne réponse attendue avec la vitesse lors de l'impact
    match resulat:
     case False:
          message = f"La mission a échoué !\nTa vitesse lors de l'impact était de {round(V0)} m/s ou {round(V0*3.6)} km/h ! \nJe parle à personne là. T'es mort :("
     case True:
          message = f"La mission a été accomplie avec succès !\nTa vitesse lors de l'impact était de {round(V0)} m/s ou {round(V0*3.6)} km/h !\nN'oublies pas de porter ta combinaison spatiale avant de sortir sinon..."
    #renvoie le bilan sous forme de str
    return message

def draw(Z0):
    pass

def info():
    #initialisation des données
    Z0 = 100000  # position en m
    V0 = 1580    # vitesse en m/s
    M0 = 15000   # masse initiale du module en kg
    Me = 8000    # dont une masse de carburant en kg
    dt = 10      # temps entre chaque commande en s
    toggle = input("Veux-tu modifier données de base? [y/n] ")
    if toggle == "y":
        # togggle = input("Veux-tu que le programme utilise des donnees aleatoires? [y/n] ")
        # if togggle == "y":
        #     Z0 = randint(1000,10000000000)
        #     V0 = randint(1000,10000000000)
        #     M0 = randint(10000,10000000)
        #     Me = randint(5000,M0 - 1)
        #     dt = randint(1, 100)
        # else:
        Z0 = int(input("position en m: "))
        V0 = int(input("vitesse en m/s: "))
        M0 = int(input("masse initiale du module en kg: "))
        Me = int(input("dont une masse de carburant en kg: "))
        dt = int(input("temps entre chaque commande en s: "))
    return Z0, V0, M0, Me, dt

def ascii(Z0, V0, ch):
  modules = {
          -2:"""
                       ____
                      /    \\\n____________         |  RIP |         _____________
            \\___     |      |     ___/
                \\____|______|____/""",
          -1:"""
                     |_______|
                    /$$$$$$$$$\\
                   |$$$$$$$$$$$|
                   |$$$$$$$$$$$|
                    \\$$$$$$$$$/
                     \\$$$$$$$/
                    / |$$$$$| \\
                   /   \\$$$/   \\
                  /     |$|     \\\n_________________/_______________\\_________________ """,
          0:"""
                     |_______|
                    /$$$$$$$$$\\
                   |$$$$$$$$$$$|
                   |$$$$$$$$$$$|
                    \\$$$$$$$$$/
                     \\$$$$$$$/
                    / |$$$$$| \\
                   /   \\$$$/   \\
                  /     |$|     \\
                _/               \\_""",
          1:"""
                     |_______|
                    /$$$$$$$$$\\
                   |$$$$$$$$$$$|
                   |$$$$$$$$$$$|
                    \\$$$$$$$$$/
                     \\$$$$$$$/
                    / |$$$$$| \\
                   /   \\$$$/   \\
                  /     |$|     \\ 
                _/       @       \\_""", 
          2:"""
                     |_______|
                    /$$$$$$$$$\\
                   |$$$$$$$$$$$|
                   |$$$$$$$$$$$|
                    \\$$$$$$$$$/
                     \\$$$$$$$/
                    / |$$$$$| \\
                   /   \\$$$/   \\
                  /     |$|     \\ 
                _/       @       \\_
                        @@@""", 
          3:"""
                     |_______|
                    /$$$$$$$$$\\
                   |$$$$$$$$$$$|
                   |$$$$$$$$$$$|
                    \\$$$$$$$$$/
                     \\$$$$$$$/
                    / |$$$$$| \\
                   /   \\$$$/   \\
                  /     |$|     \\ 
                _/       @       \\_
                        @@@       
                       @@@@@""", 
          4:"""
                     |_______|
                    /$$$$$$$$$\\
                   |$$$$$$$$$$$|
                   |$$$$$$$$$$$|
                    \\$$$$$$$$$/
                     \\$$$$$$$/
                    / |$$$$$| \\
                   /   \\$$$/   \\
                  /     |$|     \\ 
                _/       @       \\_
                        @@@       
                       @@@@@
                      @@@@@@@""", 
          5:"""
                     |_______|
                    /$$$$$$$$$\\
                   |$$$$$$$$$$$|
                   |$$$$$$$$$$$|
                    \\$$$$$$$$$/
                     \\$$$$$$$/
                    / |$$$$$| \\
                   /   \\$$$/   \\
                  /     |$|     \\ 
                _/       @       \\_
                        @@@       
                       @@@@@
                      @@@@@@@
                     @@@@@@@@@""",
          6:"""
                     |_______|
                    /$$$$$$$$$\\
                   |$$$$$$$$$$$|
                   |$$$$$$$$$$$|
                    \\$$$$$$$$$/
                     \\$$$$$$$/
                    / |$$$$$| \\
                   /   \\$$$/   \\
                  /     |$|     \\ 
                _/       @       \\_
                        @@@       
                       @@@@@
                      @@@@@@@
                     @@@@@@@@@
                    @@@@@@@@@@@""",
          7:"""
                     |_______|
                    /$$$$$$$$$\\
                   |$$$$$$$$$$$|
                   |$$$$$$$$$$$|
                    \\$$$$$$$$$/
                     \\$$$$$$$/
                    / |$$$$$| \\
                   /   \\$$$/   \\
                  /     |$|     \\ 
                _/       @       \\_
                       @@@@@
                      @@@@@@@
                     @@@@@@@@@
                    @@@@@@@@@@@
                   @@@@@@@@@@@@@""",
          8:"""
                     |_______|
                    /$$$$$$$$$\\
                   |$$$$$$$$$$$|
                   |$$$$$$$$$$$|
                    \\$$$$$$$$$/
                     \\$$$$$$$/
                    / |$$$$$| \\
                   /   \\$$$/   \\
                  /     |$|     \\ 
                _/       @       \\_
                        @@@       
                       @@@@@
                      @@@@@@@
                     @@@@@@@@@
                    @@@@@@@@@@@
                   @@@@@@@@@@@@@
                  @@@@@@@@@@@@@@@""",
          9:"""
                     |_______|
                    /$$$$$$$$$\\
                   |$$$$$$$$$$$|
                   |$$$$$$$$$$$|
                    \\$$$$$$$$$/
                     \\$$$$$$$/
                    / |$$$$$| \\
                   /   \\$$$/   \\
                  /     |$|     \\ 
                _/       @       \\_
                        @@@       
                       @@@@@
                      @@@@@@@
                     @@@@@@@@@
                    @@@@@@@@@@@
                   @@@@@@@@@@@@@
                  @@@@@@@@@@@@@@@
                 @@@@@@@@@@@@@@@@@""",
          11:"""_______________________@@@@@_______________________""",
          12:"""______________________@@@@@@@______________________""",
          13:"""_____________________@@@@@@@@@_____________________""",
          14:"""____________________@@@@@@@@@@@____________________""",
          15:"""___________________@@@@@@@@@@@@@___________________""",
          16:"""__________________@@@@@@@@@@@@@@@__________________""",
          17:"""_________________@@@@@@@@@@@@@@@@@_________________""",
          18:"""________________@@@@@@@@@@@@@@@@@@@________________""",
          19:"""_______________@@@@@@@@@@@@@@@@@@@@@_______________"""}
  Z0 = round(Z0, -3)/1000
  z = 100
  pop = False
  match Z0:
    case 0 : z = 0
    case x if 0 < x <= 10 : z = 1
    case x if x < 1000 : z = round(Z0/10)
    case _: pop = True
  match int(ch):
    case 0 : b = 0
    case 1 : b = 0
    case _: b =  int(ch) - 1
  match b:
    case x if x < z: c = round(z - b - 1)
    case _: c = 0
  if z == 100:
    c = 0
  if z == 0:
    if V0 < 1:
        print(modules[-1])
    else:
        print(modules[-2])
  elif b > z:
    print(modules[z])
    print(modules[b - z + 10])
  else:
    print(modules[int(ch)])
    for n in range(c):
      print("                                                   ")
    if pop == False:
      print("___________________________________________________")
