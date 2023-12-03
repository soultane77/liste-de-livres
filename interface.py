import tkinter as tk

def ajouter_livre():
    # Récupérez les valeurs des champs de texte
    titre = titre_entry.get()
    auteur = auteur_entry.get()
    emplacement = emplacement_entry.get()

    # Affichez les valeurs (vous pouvez les ajouter à la base de données ici)
    print("Titre:", titre)
    print("Auteur:", auteur)
    print("Emplacement:", emplacement)

# Créez la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Ajouter un livre")

# Créez des étiquettes
titre_label = tk.Label(fenetre, text="Titre:")
auteur_label = tk.Label(fenetre, text="Auteur:")
emplacement_label = tk.Label(fenetre, text="Emplacement:")

# Créez des champs de texte
titre_entry = tk.Entry(fenetre)
auteur_entry = tk.Entry(fenetre)
emplacement_entry = tk.Entry(fenetre)

# Créez un bouton pour ajouter le livre
ajouter_bouton = tk.Button(fenetre, text="Ajouter le livre", command=ajouter_livre)

# Organisez les éléments dans la fenêtre
titre_label.pack()
titre_entry.pack()
auteur_label.pack()
auteur_entry.pack()
emplacement_label.pack()
emplacement_entry.pack()
ajouter_bouton.pack()

fenetre.mainloop()

