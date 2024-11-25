def plateau_rempli(plateau):
    return all(cell != ' ' for row in plateau for cell in row)

def verifier_victoire(plateau):
    for row in plateau:
        if row[0] == row[1] == row[2] != ' ':
            return True
    for col in range(3):
        if plateau[0][col] == plateau[1][col] == plateau[2][col] != ' ':
            return True
    if plateau[0][0] == plateau[1][1] == plateau[2][2] != ' ':
        return True
    if plateau[0][2] == plateau[1][1] == plateau[2][0] != ' ':
        return True
    return False

def afficher_plateau(plateau):
    for row in plateau:
        print('|'.join(row))
        print('-' * 5)

def minimax(plateau, profondeur, est_maximisant):
    if verifier_victoire(plateau):
        return -1 if est_maximisant else 1
    if plateau_rempli(plateau):
        return 0

    if est_maximisant:
        meilleur_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if plateau[i][j] == ' ':
                    plateau[i][j] = 'O'  # Tour de l'IA
                    score = minimax(plateau, profondeur + 1, False)
                    plateau[i][j] = ' '  # Annuler le coup
                    meilleur_score = max(score, meilleur_score)
        return meilleur_score
    else:
        meilleur_score = float('inf')
        for i in range(3):
            for j in range(3):
                if plateau[i][j] == ' ':
                    plateau[i][j] = 'X'  # Tour du joueur
                    score = minimax(plateau, profondeur + 1, True)
                    plateau[i][j] = ' '  # Annuler le coup
                    meilleur_score = min(score, meilleur_score)
        return meilleur_score

def meilleur_coup(plateau):
    meilleur_score = -float('inf')
    coup = None
    for i in range(3):
        for j in range(3):
            if plateau[i][j] == ' ':
                plateau[i][j] = 'O'  # Tour de l'IA
                score = minimax(plateau, 0, False)
                plateau[i][j] = ' '  # Annuler le coup
                if score > meilleur_score:
                    meilleur_score = score
                    coup = (i, j)
    return coup

def tic_tac_toe():
    plateau = [[' ' for _ in range(3)] for _ in range(3)]
    joueurs = ['X', 'O']  # X est le joueur, O est l'IA
    tour = 0

    while True:
        afficher_plateau(plateau)  # Affiche le plateau
        if tour % 2 == 0:
            joueur = 'X'  # Tour du joueur
            print(f"Joueur {joueur}, entrez votre choix (1-9) : ")
            try:
                choix = int(input())  # Demande un nombre entre 1 et 9
                if choix < 1 or choix > 9:
                    print("Veuillez entrer un nombre entre 1 et 9.")
                    continue

                # Convertir le choix en indices de tableau
                ligne = (choix - 1) // 3
                col = (choix - 1) % 3

                if plateau[ligne][col] != ' ':
                    print("Case déjà prise, essayez à nouveau.")
                    continue

                plateau[ligne][col] = joueur
            except ValueError:
                print("Entrée invalide. Veuillez entrer un nombre.")
                continue
        else:
            joueur = 'O'  # Tour de l'IA
            print("C'est le tour de l'IA.")
            ligne, col = meilleur_coup(plateau)
            plateau[ligne][col] = joueur
            print(f"L'IA a choisi la case : ({ligne * 3 + col + 1})")  # Affiche le numéro de case

        # Vérifie si le joueur a gagné
        if verifier_victoire(plateau):
            afficher_plateau(plateau)  # Affiche le plateau final
            print(f"Félicitations, joueur {joueur} ! Vous avez gagné !")
            break

        # Vérifie si le plateau est plein
        if plateau_rempli(plateau):
            afficher_plateau(plateau)  # Affiche le plateau final
            print("Match nul !")
            break

        tour += 1

if __name__ == "__main__":
    tic_tac_toe()
