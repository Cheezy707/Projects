lazy import math
lazy from os import system
lazy from time import sleep
#import sounddevice as sd
lazy import numpy as np
# TP 1 ###############################################################################################

def multiple(x,y):
    if y==0:
        return x==0
    return x%y==0

def triangle(x,y,z):
    if x+y > z and z+y > x and x+z > y:
        return True
    return False

def triangleEqui(x,y,z):
    if x==y==z:
        return True
    return False


def triangleIso(x,y,z):
    if x==y or x==z or y==z:
        return triangle(x,y,z)
    return False

def triangelRect(x,y,z):
    x,y,z = sorted([x,y,z])
    if z**2 == y**2 + x**2:
        return triangle(x,y,z)
    return False

def memeDizaine(x,y):
    if x//10 == y//10:
        return True
    return False

def memeParite(x,y):
    if x%2==y%2:
        return True
    return False

def rectangle(H,L):
    for i in range(H):
        if i==0 or i==H-1:
            for p in range(L):
                print("-", end="")
            print()
        else:
            print("|", end="")
            for p in range(L-2):
                print(" ",end="")
            print("|")

def disque(R):
    for i in range(2*R+1):
        for j in range(2*R):
            if sqrt((R-i)**2 + (R-j)**2) <= R:
                print("*", end="")
            else:
                print(" ", end="")
        print()

# TP 2 ##############################################################################################
def estPair(x):
    match  x:
        case 1:
             return False
        case 0:
             return True
        case _:
             return estPair(x-2)

def existeMul11(x,y):
    if x%11==0:return True
    elif x==y:return False
    return existeMul11(x+1,y)

def maxMul11(x,y):
    if x%11==0:return True
    elif x==y:return False
    return existeMul11(x,y-1)

def nbMul11(x,y):
    if y%11==0:return 1 + nbMul11(x,y-1)
    elif x==y: return 0
    else: return 0 + nbMul11(x,y-1)

def somMul11(x,y):
    if y%11==0:return y + somMul11(x,y-1)
    elif x==y: return 0
    else: return 0 + somMul11(x,y-1)

def nbChifDec(x):
    return len(str(n))

def chifRang(x,y):
    return(str(x)[-y])

def somChif(x):
    if len(str(x))==1: return x
    return int(str(x)[-1]) + somChif(x//10)
    
def binaire(x):
    return binaire(x//2) + str(x%2) if x > 1 else str(x)

def dicho(a, b, E, f):
    M = (a+b)/2
    return M if b-a<E else dicho(M, b, E, f) if f(M)*f(a)>0 else dicho(a, M, E, f)    

#TP 3 ##############################################################################################

def uneEtape(inputlist):
    outputlist = []
    for index in range(len(inputlist)):
        if index == 0 or index== len(inputlist)-1:
            outputlist.append(inputlist[index-1] if index==len(inputlist)-1 else inputlist[index+1])
        else:
            outputlist.append(inputlist[index-1] if inputlist[index-1]==inputlist[index+1] else inputlist[index])

    return outputlist

def afficheLigne(table):
    #system("clear")
    for i in table:
        system("echo -n \u2588" if i==1 else "echo -n ' '")
        sleep(0.1)
    print()

def simulation(table):
    while uneEtape(table) != table:
        afficheLigne(table)
        table = uneEtape(table)


def pendu():
    m = "boat"
    M = [c for c in m]
    N = ["-" for c in m]
    while M != N:
        n = input("Guess: ")
        if n in M:
            for i in range(len(M)):
                if n == M[i]:
                    N[i] = n
        print("".join(N))

def Eratosthene(n):
    N = [x for x in range(2,n+1)]
    for i in N:
        for j in N:
            if i != j and j%i == 0:
                N.remove(j)
    return(N)

def hauteurVersFreq(h):
    return 440 * (2 ** (h/12))

def signalNote(h, d, v, A, D, S, R, timbre):
    output=[]
    for i in range(int(d * int(44100))):
        output.append(32767 * v * timbre(2 * pi * hauteurVersFreq(h) * i / int(44100)))
    return enveloppe(output, A, D, S, R)

def joueSignal(T):
    U = np.array(T, dtype=np.float32)  # sounddevice prefers float32 in [-1, 1]
    sd.play(U, samplerate=int(44100))
    sd.wait()

def joueMelodie(liH, liD, liV):
    for i in range(len(liH)):
        joueSignal(signalNote(liH[i], liD[i], liV[i], 0.02, 0.02, 0.7, 0.15, foncTimbre))

def enveloppe(T, A, D, S, R):
    C = 0
    for i in range(int(44100*A)):
        C += 1/int(44100*A)
        T[i] = T[i]*C
    for i in range(int(44100*D)):
        C -= (1-S)/int(44100*D)
        T[i+int(44100*A)] = T[i+int(44100*A)]*C
    for i in range(int(44100*R)):
        C -= C/int(44100*R)
        T[-(int(44100*R)-i)] = T[-(int(44100*R)-i)]*C
    return T
    
def foncTimbre(x):
    return 0.5*sin(x)+0.3*sin(2*x)+0.2*sin(3*x)


def ballons(cords):
    pass


# Pass over balloons until there's a gap
# Look at the balloons before the gap
# 
    

####################################################################################################
def main():
#    print(dicho(3,4,0.0001, sin)) / 3.141571044921875
#    simulation([1,1,1,0,0,0,1,1,1,0,0,0])
#    liH = [ 4, -1, 0, 2, 0, -1, -3, 0, -3, 0, 4, 2, 0, -1, 0, -1, 0, 2, 4, 0, -3, 0, -3]
#    liD = [.4, .2, .2, .4, .2, .2, .38, .02, .2, .2, .4, .2, .2, .38, .02, .2, .2, .4, .4, .4, .38, .02, .4]
#    liV = [ 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1]
#    joueMelodie(liH, liD, liV)
    ballonslist = [10,16,2,8,1,6,7,12] # 3 
    ballons(ballonslist)
    pass

main()


# Dans une fête foraine, des ballons sont suspendus à différents endroit d'un grand mur. Pour chaque ballon, si on appelle M le bord gauche du mur, 
# G le bord gauche du ballon et D le bord droit du ballon, on a mesuré les distances horizontales MG et MD. 
# Ces distances sont mémorisées dans un tableau de nombres [MG1, MD1, MG2, MD2, ... ].
# Le joueur tire verticalement des flèches qui éclatent tous les ballons qu'elles rencontent.
# Ecrire en Python une fonction qui, étant donné le tableau des distances, 
# calcule et renvoie le nombre minimal de flèches nécessaire pour éclater tous les ballons.