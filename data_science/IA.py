import numpy as np
import random
import os
import pandas as pd

def jouer(plateau):
    if not os.path.exists("dataParties.csv"):
        return random.choice([col for col in range(plateau.shape[1]) if plateau[0][col] == 0])

    df = pd.read_csv("dataParties.csv")

    if 'etat' not in df.columns:
        return random.choice([col for col in range(plateau.shape[1]) if plateau[0][col] == 0])

    etat_str = np.array_str(plateau)

    if etat_str in df["etat"].values:
        actions_possibles = df[df["etat"] == etat_str]["action"].values
        action_counts = {action: 0 for action in actions_possibles}
        for action in actions_possibles:
            action_counts[action] += 1
        action = max(action_counts, key=action_counts.get)
    else:
        action = random.choice([col for col in range(plateau.shape[1]) if plateau[0][col] == 0])

    return action
