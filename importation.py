import sqlite3
import csv

# Chemin vers votre base de données SQLite locale
chemin_base_de_donnees = '/Users/mehdiayachia/Downloads/base/ma_collection_de_livres.db'

def creer_connexion():
    conn = sqlite3.connect(chemin_base_de_donnees)
    return conn

def ajouter_livre(conn, titre, auteur, emplacement):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO livres (titre, auteur, emplacement) VALUES (?, ?, ?)", (titre, auteur, emplacement))
    conn.commit()

def importer_csv(chemin_fichier_csv):
    conn = creer_connexion()
    with open(chemin_fichier_csv, newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            titre = row['Titre']
            auteur = row['auteur']
            emplacement = row['emplacement']
            ajouter_livre(conn, titre, auteur, emplacement)
    conn.close()

if __name__ == '__main__':
    chemin_fichier_csv = '/Users/mehdiayachia/Downloads/base/livres.csv'  # Chemin complet vers votre fichier CSV
    importer_csv(chemin_fichier_csv)


