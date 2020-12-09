'''Définition des variables'''
motAleat = ["C", "R", "A", "Y", "O", "N"]
lettre = ["X","X","X","X","X","X"]
lettreCorrecte = [0,0,0,0,0,0]
lettrePresente = [0,0,0,0,0,0]

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

'''Programme princpial'''
import random 
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
print (motAleat)
input()
