import numpy as np

lignes = 6
colonnes = 7
 
def creer_plateau(lignes, colonnes):
    return np.zeros((lignes, colonnes), dtype=int)
 
def afficher_plateau(plateau):
    print(plateau)
 
def placer_jeton(plateau, colonne, joueur):
    for ligne in range(len(plateau)-1, -1, -1):
        if plateau[ligne][colonne] == 0:
            plateau[ligne][colonne] = joueur
            return True
    return False
 
def victoire(plateau, joueur):
    for ligne in range(len(plateau)):
        for colonne in range(len(plateau[0]) - 3):
            if all(plateau[ligne][colonne + i] == joueur for i in range(4)):
                return True
 
    for colonne in range(len(plateau[0])):
        for ligne in range(len(plateau) - 3):
            if all(plateau[ligne + i][colonne] == joueur for i in range(4)):
                return True
 
    for ligne in range(len(plateau) - 3):
        for colonne in range(len(plateau[0]) - 3):
            if all(plateau[ligne + i][colonne + i] == joueur for i in range(4)):
                return True
 
    for ligne in range(len(plateau) - 3):
        for colonne in range(3, len(plateau[0])):
            if all(plateau[ligne + i][colonne - i] == joueur for i in range(4)):
                return True
 
    return False
 
def jouer_partie():
    plateau = creer_plateau(lignes, colonnes)
    tour_joueur = 1
 
    while True:
        afficher_plateau(plateau)
 
        colonne = int(input(f"Joueur {tour_joueur}, choisissez une colonne (0-{colonnes-1}): "))
        if colonne < 0 or colonne >= colonnes:
            print("Colonne invalide, veuillez choisir une colonne entre 0 et", colonnes-1)
            continue
 
        if not placer_jeton(plateau, colonne, tour_joueur):
            print("Colonne pleine, veuillez choisir une autre colonne.")
            continue
 
        if victoire(plateau, tour_joueur):
            afficher_plateau(plateau)
            print(f"Le joueur {tour_joueur} remporte la partie !")
            break
 
        if np.all(plateau != 0):
            afficher_plateau(plateau)
            print("Égalité ! La partie est terminée.")
            break
 
        tour_joueur = 2 if tour_joueur == 1 else 1
 
jouer_partie()