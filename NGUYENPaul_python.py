'''Définition des variables'''
motAleat = ["C", "R", "A", "Y", "O", "N"]
lettre = ["X","X","X","X","X","X"]
lettreCorrecte = [0,0,0,0,0,0]
lettrePresente = [0,0,0,0,0,0]
gameOn = 1
compteur = 0
'''Définition des fonctions'''

'''Fonction de choix des lettres par l'utilisateur '''
def choix (lettre):
    for i in range (0,6) :
        if i == 0 :
            terminaison= "ère"
        else :
            terminaison = "ème"
        print("Quelle est votre", i + 1, terminaison, "lettre ?")
        lettre[i] = input()
    return lettre

'''Fonction vérifiant quelles lettres sont correctement placées'''
def correcte (lettre,motAleat,lettreCorrecte):
	for i in range (0,6) :
		if (lettre[i] == motAleat[i]) :
			lettreCorrecte[i]=+1
	return lettreCorrecte

def presence (lettre,motAleat, lettrePresente):
    for i in range (0,6):
        for j in range (0,6):
            if (lettre[i]==motAleat[j]) : 
                lettrePresente[i] =+ 1
                
'''Fonction permettant de détecter si une lettre proposée fait partie du mot'''
def affichage (lettre, lettreCorrecte, lettrePresente):
	for i in range (0,6) : 
		if (lettreCorrecte[i] == 1) : 
			print(Back.RED + lettre[i], end=" ") 
		elif (lettrePresente[i] > 0) :
			print(Back.YELLOW + lettre[i], end = " " )
		else :
			print(Back.BLUE + lettre [i], end = " ")
	return ()

'''Programme princpial'''

'''Initialisation'''
import random 
from colorama import init
init()
from colorama import Fore, Back, Style 

numero = random.randint(1,10)
if (numero == 1):
	motAleat = ["C","R","A","Y","O","N"]
if (numero == 2):
	motAleat = ["P","A","P","I","E","R"]
if (numero == 3):
	motAleat = ["O","I","S","E","A","U"]
if (numero == 4):
	motAleat = ["J","U","L","I","E","N"]
if (numero == 5):
	motAleat = ["L","E","P","E","R","S"]
if (numero == 6):
	motAleat = ["C","I","S","E","A","U"]
if (numero == 7):
	motAleat = ["F","L","A","V","I","E"]
if (numero == 8):
	motAleat = ["C","H","A","U","V","E"]
if (numero == 9):
	motAleat = ["N","A","R","V","A","L"]
if (numero == 10):
	motAleat = ["N","A","V","I","R","E"]
while gameOn == 1 :
	if (compteur < 9):
		choix(lettre)
		presence(lettre, motAleat, lettrePresente)
		correcte(lettre, motAleat, lettreCorrecte)
		affichage(lettre, lettreCorrecte, lettrePresente)
		if (lettreCorrecte[0] == 1 and lettreCorrecte[1] == 1 and lettreCorrecte[2] == 1 and lettreCorrecte[3] == 1 and lettreCorrecte[4] == 1 and lettreCorrecte[5] == 1) :
			print("GAGNE!!! Félicitations")
			gameOn = 0
		print(Style.RESET_ALL)
		lettreCorrecte = [0,0,0,0,0,0]
		lettrePresente = [0,0,0,0,0,0]
	elif (compteur == 9) : 
		print("Vous n'avez plus d'éssais ! C'est perdu ! Le mot était", motAleat," , dommage !")
		gameOn = 0
input()


