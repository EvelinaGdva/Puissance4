import numpy as np
import pandas as pd
import IA  
import os

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

def verifier_victoire(plateau, joueur):
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

def enregistrer_donnees(etats_actions, joueur_gagnant):
    if not os.path.exists("dataParties.csv"):
        df = pd.DataFrame(columns=["etat", "action", "joueur"])
    else:
        df = pd.read_csv("dataParties.csv")

    data_to_append = []
    for etat, action in etats_actions:
        data_to_append.append({"etat": str(etat.tolist()), "action": action, "joueur": joueur_gagnant})

    if df.empty:
        df = pd.DataFrame(data_to_append)
    else:
        df = pd.concat([df, pd.DataFrame(data_to_append)], ignore_index=True)

    df.to_csv("dataParties.csv", index=False)

def puissance4():
    lignes, colonnes = 6, 7
    plateau = creer_plateau(lignes, colonnes)
    tour_joueur = 1
    etats_actions = []

    while True:
        afficher_plateau(plateau)

        if tour_joueur == 1:
            colonne = int(input(f"Joueur {tour_joueur}, choisissez une colonne (0-{colonnes-1}): "))
            if colonne < 0 or colonne >= colonnes:
                print("Erreur. Colonne invalide, veuillez choisir une colonne entre 0 et", colonnes-1)
                continue
        else:
            colonne = IA.jouer(plateau)
            print(f"L'IA joue dans la colonne {colonne}")

        if not placer_jeton(plateau, colonne, tour_joueur):
            print("Colonne pleine, veuillez choisir une autre colonne.")
            continue

        etats_actions.append((plateau.copy(), colonne))

        if verifier_victoire(plateau, tour_joueur):
            afficher_plateau(plateau)
            print(f"Le joueur {tour_joueur} remporte la partie !")
            enregistrer_donnees(etats_actions, tour_joueur)
            break

        if np.all(plateau != 0):
            afficher_plateau(plateau)
            print("Égalité ! La partie est terminée.")
            break

        tour_joueur = 2 if tour_joueur == 1 else 1

    df_export = pd.DataFrame(plateau)
    df_export.to_csv('dataParties.csv', index=False)
    return df_export

puissance4()
