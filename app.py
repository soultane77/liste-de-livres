from flask import Flask, render_template

app = Flask(__name__)

# Définissez vos routes Flask ici
import subprocess

# Ajoutez cette route à votre fichier "app.py"
@app.route('/tkinter_app')
def tkinter_app():
    subprocess.Popen(['python', '/Users/mehdiayachia/Downloads/base/gestion_livres.py'])  # Remplacez par le nom de votre fichier tkinter
    return ''

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()

