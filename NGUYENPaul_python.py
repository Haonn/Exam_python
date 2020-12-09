motAleat = ["C", "R", "A", "Y", "O", "N"]
lettre = ["X","X","X","X","X","X"]
def choix (lettre):
    for i in range (0,6) :
        if i == 0 :
            terminaison= "ère"
        else :
            terminaison = "ème"
        print("Quelle est votre", i + 1, terminaison, "lettre ?")
        lettre[i] = input()
    return lettre
    
choix(lettre)
print (lettre)