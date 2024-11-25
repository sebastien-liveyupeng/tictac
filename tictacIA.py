



# Initialize the Tic-Tac-Toe board


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

def minimax(plateau, depth, is_maximizing):
    if verifier_victoire(plateau):
        return -1 if is_maximizing else 1
    if plateau_rempli(plateau):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if plateau[i][j] == ' ':
                    plateau[i][j] = 'O'  # AI's turn
                    score = minimax(plateau, depth + 1, False)
                    plateau[i][j] = ' '  # Undo move
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if plateau[i][j] == ' ':
                    plateau[i][j] = 'X'  # Player's turn
                    score = minimax(plateau, depth + 1, True)
                    plateau[i][j] = ' '  # Undo move
                    best_score = min(score, best_score)
        return best_score

def meilleur_coup(plateau):
    best_score = -float('inf')
    move = None
    for i in range(3):
        for j in range(3):
            if plateau[i][j] == ' ':
                plateau[i][j] = 'O'  # AI's turn
                score = minimax(plateau, 0, False)
                plateau[i][j] = ' '  # Undo move
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def tic_tac_toe():
    plateau = [[' ' for _ in range(3)] for _ in range(3)]
    joueurs = ['X', 'O']  # X is the player, O is the AI
    tour = 0

    while True:
        afficher_plateau(plateau)
        if tour % 2 == 0:
            joueur = 'X'  # Player's turn
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
        else:
            joueur = 'O'  # AI's turn
            print("C'est le tour de l'IA.")
            ligne, col = meilleur_coup(plateau)
            plateau[ligne][col] = joueur
            print(f"L'IA a choisi la case : ({ligne}, {col})")

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
