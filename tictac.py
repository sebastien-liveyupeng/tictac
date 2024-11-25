#langue choisie ANGLAIS

#BOARD
#PLAYER INPUT 
#VERIFY IF ITS A WIN OR TIE
#SWITCH PLAYER

def afficher_plateau(plateau):
    for ligne in plateau:
        print(" | ".join(ligne))
        print("-" * 9)

def verifier_victoire(plateau):

    for ligne in plateau:
        if ligne.count(ligne[0]) == 3 and ligne[0] != ' ':
            return True

    for col in range(3):
        if plateau[0][col] == plateau[1][col] == plateau[2][col] != ' ':
            return True

    if plateau[0][0] == plateau[1][1] == plateau[2][2] != ' ':
        return True

    if plateau[0][2] == plateau[1][1] == plateau[2][0] != ' ':
        return True

    return False

def plateau_rempli(plateau):
    return all(cell != ' ' for row in plateau for cell in row)

def tic_tac_toe():
    plateau = [[' ' for _ in range(3)] for _ in range(3)]
    joueurs = ['X', 'O']
    tour = 0

    while True:
        afficher_plateau(plateau)
        joueur = joueurs[tour % 2]
        print(f"Joueur {joueur}, entrez votre choix (ligne et colonne) : ")
        
        try:
            ligne, col = map(int, input().split())
            if plateau[ligne][col] != ' ':
                print("Case déjà prise, essayez à nouveau.")
                continue
            plateau[ligne][col] = joueur
        except (ValueError, IndexError):
            print("Entrée invalide. Utilisez deux nombres entre 0 et 2 (ligne et colonne).")
            continue

        if verifier_victoire(plateau):
            afficher_plateau(plateau)
            print(f"Félicitations, joueur {joueur} ! Vous avez gagné !")
            break

        if plateau_rempli(plateau):
            afficher_plateau(plateau)
            print("Match nul !")
            break

        tour += 1

if __name__ == "__main__":
    tic_tac_toe()