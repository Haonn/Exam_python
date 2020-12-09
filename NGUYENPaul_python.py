motAleat = ["C", "R", "A", "Y", "O", "N"]
lettre = ["X","X","X","X","X","X"]
lettreCorrecte = [0,0,0,0,0,0]
lettrePresente = [0,0,0,0,0,0]
def choix (lettre):
    for i in range (0,6) :
        if i == 0 :
            terminaison= "ère"
        else :
            terminaison = "ème"
        print("Quelle est votre", i + 1, terminaison, "lettre ?")
        lettre[i] = input()
    return lettre
    
def correcte (lettre,motAleat,lettreCorrecte):
	for i in range (0,6) :
		if (lettre[i] == motAleat[i]) :
			lettreCorrecte[i]=+1
	return lettreCorrecte

choix(lettre)
print (lettre)
correcte (lettre, motAleat, lettreCorrecte)
print(lettreCorrecte)
input()