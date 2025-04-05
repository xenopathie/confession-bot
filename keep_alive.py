from flask import Flask
from threading import Thread

print("Démarrage du fichier keep_alive.py...")

app = Flask('')

@app.route('/')
def home():
    return "Le bot est en ligne !"

def run():
    print("Lancement du serveur Flask...")
app.run(host='0.0.0.0', port=8081)

def keep_alive():
    print("Lancement du serveur Flask sans thread...")
    run()
