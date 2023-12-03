import sqlite3
import tkinter as tk
from tkinter import messagebox

# Chemin vers votre base de données SQLite locale
chemin_base_de_donnees = '/Users/mehdiayachia/Downloads/base/ma_collection_de_livres.db'

def creer_connexion():
    conn = sqlite3.connect(chemin_base_de_donnees)
    return conn

def creer_table_livres(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS livres (
        id INTEGER PRIMARY KEY,
        titre TEXT NOT NULL,
        auteur TEXT,
        emplacement TEXT
    )''')
    conn.commit()

def ajouter_livre(conn, titre, auteur, emplacement):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO livres (titre, auteur, emplacement) VALUES (?, ?, ?)", (titre, auteur, emplacement))
    conn.commit()

def lister_livres(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM livres")
    rows = cursor.fetchall()
    return rows

def rechercher_livres(conn, recherche):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM livres WHERE titre LIKE ? OR auteur LIKE ? OR emplacement LIKE ?", 
                   (f'%{recherche}%', f'%{recherche}%', f'%{recherche}%'))
    rows = cursor.fetchall()
    return rows

def supprimer_livre(conn, livre_id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM livres WHERE id=?", (livre_id,))
    conn.commit()

def ajouter_livre_button_click():
    titre = titre_entry.get()
    auteur = auteur_entry.get()
    emplacement = emplacement_entry.get()
    if titre and auteur and emplacement:
        ajouter_livre(conn, titre, auteur, emplacement)
        messagebox.showinfo("Succès", "Livre ajouté avec succès !")
        titre_entry.delete(0, tk.END)
        auteur_entry.delete(0, tk.END)
        emplacement_entry.delete(0, tk.END)
        actualiser_liste()
    else:
        messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")

def lister_livres_button_click():
    actualiser_liste()

def rechercher_livres_button_click():
    recherche = recherche_entry.get()
    if recherche:
        resultats = rechercher_livres(conn, recherche)
        if resultats:
            listbox.delete(0, tk.END)
            for resultat in resultats:
                listbox.insert(tk.END, resultat)
        else:
            messagebox.showinfo("Info", "Aucun résultat trouvé pour la recherche.")
    else:
        messagebox.showerror("Erreur", "Veuillez entrer un terme de recherche.")

def supprimer_livre_button_click():
    selection = listbox.curselection()
    if selection:
        livre_id = listbox.get(selection[0])[0]
        supprimer_livre(conn, livre_id)
        messagebox.showinfo("Succès", "Livre supprimé avec succès !")
        actualiser_liste()
    else:
        messagebox.showerror("Erreur", "Veuillez sélectionner un livre à supprimer.")

def actualiser_liste():
    livres = lister_livres(conn)
    listbox.delete(0, tk.END)
    for livre in livres:
        listbox.insert(tk.END, livre)

if __name__ == '__main__':
    conn = creer_connexion()
    creer_table_livres(conn)

    app = tk.Tk()
    app.title("Gestion de la collection de livres")

    titre_label = tk.Label(app, text="Titre du livre:")
    titre_label.pack()
    titre_entry = tk.Entry(app)
    titre_entry.pack()

    auteur_label = tk.Label(app, text="Auteur du livre:")
    auteur_label.pack()
    auteur_entry = tk.Entry(app)
    auteur_entry.pack()

    emplacement_label = tk.Label(app, text="Emplacement du livre:")
    emplacement_label.pack()
    emplacement_entry = tk.Entry(app)
    emplacement_entry.pack()

    ajouter_button = tk.Button(app, text="Ajouter un livre", command=ajouter_livre_button_click)
    ajouter_button.pack()

    lister_button = tk.Button(app, text="Lister les livres", command=lister_livres_button_click)
    lister_button.pack()

    recherche_label = tk.Label(app, text="Rechercher un livre:")
    recherche_label.pack()
    recherche_entry = tk.Entry(app)
    recherche_entry.pack()

    rechercher_button = tk.Button(app, text="Rechercher", command=rechercher_livres_button_click)
    rechercher_button.pack()

    listbox = tk.Listbox(app, width=60)
    listbox.pack()

    supprimer_button = tk.Button(app, text="Supprimer un livre", command=supprimer_livre_button_click)
    supprimer_button.pack()

    quitter_button = tk.Button(app, text="Quitter", command=app.quit)
    quitter_button.pack()

    actualiser_liste()

    app.mainloop()

    conn.close()
