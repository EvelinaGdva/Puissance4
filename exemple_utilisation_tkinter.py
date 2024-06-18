import tkinter as tk
import numpy as np

class MonCanvas(tk.Canvas):
    def __init__(self, master, l=None, h=None):
        super().__init__(master, width=l, height=h)
        self.configure(bg='#5080FF')
        self.lignes = 6
        self.colonnes = 7
        self.taille_case = min(l // self.colonnes, h // self.lignes)
        self.dessiner_grille()
        self.bind("<Button-1>", self.cliquer_case)
        self.tour = 'red'
        self.etat_jeu = False  # Ajout d'un état de jeu pour démarrer et arrêter le jeu

    def dessiner_grille(self):
        self.cases = {}
        for ligne in range(self.lignes):
            for colonne in range(self.colonnes):
                x1 = colonne * self.taille_case
                y1 = ligne * self.taille_case
                x2 = x1 + self.taille_case
                y2 = y1 + self.taille_case
                r = 5
                self.cases[(ligne, colonne)] = self.create_oval(x1+r, y1+r, x2-r, y2-r, fill='white')

    def cliquer_case(self, event):
        if not self.etat_jeu:
            return 

        colonne = event.x // self.taille_case
        for ligne in range(self.lignes-1, -1, -1):
            if self.itemcget(self.cases[(ligne, colonne)], 'fill') == 'white':
                self.itemconfig(self.cases[(ligne, colonne)], fill=self.tour)
                self.tour = 'yellow' if self.tour == 'red' else 'red'
                break

    def demarrer_jeu(self):
        self.etat_jeu = True

class MonBouton(tk.Button):
    def __init__(self, master, id, canvas):
        self.id = id
        self.canvas = canvas
        super().__init__(master, text=self.id)
        self.configure(width=20, height=2)
        self.configure(bg='green', fg='white')
        self.configure(font=('Times New Roman', 20, 'italic'))
        self.configure(command=self.fonction)

    def fonction(self):
        if self.id == 'Joueur - Joueur':
            print(f'Vous avez appuyé sur le bouton {self.id}.')
            self.canvas.demarrer_jeu()

class MonCadre(tk.Frame):
    def __init__(self, master, canvas):
        super().__init__(master, width=100, height=100)
        self.configure(bg='pink')
        self.liste_boutons = [MonBouton(self, id, canvas) for id in ('Joueur - Joueur', 'Joueur - IA', 'IA - IA')]
        
        for k, bouton in enumerate(self.liste_boutons):
            bouton.grid(row=k, column=0, padx=20, pady=20)

class MonLabel(tk.Label):
    def __init__(self, master, t=None):
        super().__init__(master, width=30, height=2)
        self.configure(text=t)
        self.configure(bg='red', fg='brown')
        self.configure(font=('Arial', 40))

class MonTk(tk.Tk):
    def __init__(self):
        super().__init__()
        self.configure(bg='light blue')
        self.geometry('1400x800+400+0')
        self.titre_label = MonLabel(self, t="Puissance 4")
        self.titre_label.grid(row=0, column=0, columnspan=2, padx=20, pady=20)
        self.cnv = MonCanvas(self, l=700, h=600)
        self.menu = MonCadre(self, self.cnv)
        self.menu.grid(row=1, column=0, padx=20, pady=20)
        self.cnv.grid(row=1, column=1, padx=20, pady=20)

if __name__ == '__main__':
    app = MonTk()
    app.mainloop()