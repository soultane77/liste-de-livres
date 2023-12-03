from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Chemin vers la base de données
chemin_base_de_donnees = '/Users/mehdiayachia/Downloads/base/ma_collection_de_livres.db'

def creer_connexion():
    conn = sqlite3.connect(chemin_base_de_donnees)
    return conn

def lister_livres(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT id, titre, auteur, emplacement FROM livres")
    rows = cursor.fetchall()
    return rows


def ajouter_livre(conn, titre, auteur, emplacement):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO livres (titre, auteur, emplacement) VALUES (?, ?, ?)", (titre, auteur, emplacement))
    conn.commit()

def supprimer_livre(conn, livre_id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM livres WHERE id = ?", (livre_id,))
    conn.commit()

def rechercher_livres(conn, recherche):
    cursor = conn.cursor()
    query = f"SELECT * FROM livres WHERE titre LIKE '%{recherche}%' OR auteur LIKE '%{recherche}%'"
    cursor.execute(query)
    rows = cursor.fetchall()
    return rows

@app.route('/')
def index():
    conn = creer_connexion()
    livres = lister_livres(conn)
    conn.close()
    return render_template('index.html', livres=livres)

@app.route('/ajouter', methods=['GET', 'POST'])
def ajouter():
    if request.method == 'POST':
        titre = request.form['titre']
        auteur = request.form['auteur']
        emplacement = request.form['emplacement']

        conn = creer_connexion()
        ajouter_livre(conn, titre, auteur, emplacement)
        conn.close()
        return redirect(url_for('index'))
    return render_template('ajouter.html')

@app.route('/supprimer/<int:livre_id>')
def supprimer(livre_id):
    conn = creer_connexion()
    supprimer_livre(conn, livre_id)
    conn.close()
    return redirect(url_for('index'))

@app.route('/rechercher', methods=['GET'])
def rechercher():
    recherche = request.args.get('recherche')
    conn = creer_connexion()
    livres = rechercher_livres(conn, recherche)
    conn.close()
    return render_template('index.html', livres=livres)

if __name__ == '__main__':
    app.run(debug=True)
