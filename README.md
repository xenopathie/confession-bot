Confession Bot
Un bot Discord simple et interactif permettant aux utilisateurs de soumettre des confessions anonymes et de signaler celles qui sont inappropriées. Ce bot utilise discord.py pour l'intégration avec Discord et Flask pour maintenir le bot actif en ligne.

Fonctionnalités principales
Confessions anonymes : Les utilisateurs peuvent envoyer des confessions anonymes via un panel interactif de boutons.

Gestion des signalements : Chaque confession peut être signalée en cas de contenu inapproprié via un bouton dédié. Les signalements sont envoyés à un salon privé réservé aux administrateurs.

Suivi des utilisateurs : Le bot garde une trace des utilisateurs qui envoient des confessions, afin de prévenir les abus ou les signalements répétitifs.

Interface simple : Un panel de confession interactif est disponible dans les salons publics pour encourager les utilisateurs à partager de manière anonyme.

Mise en ligne automatique avec Flask : Le bot est hébergé sur Render, avec Flask permettant de le maintenir en ligne en arrière-plan via un serveur web léger.

Prérequis
Python 3.8+

discord.py - Pour l'interaction avec l'API Discord.

Flask - Pour maintenir le bot en ligne.

python-dotenv - Pour la gestion sécurisée des variables d'environnement.

Installation
Clonez ce dépôt :

git clone https://github.com/xenopathie/confession-bot.git
cd confession-bot
Installez les dépendances :

pip install -r requirements.txt
Créez un fichier .env à la racine du projet et ajoutez votre token Discord :

DISCORD_TOKEN=Votre_Token_Discord
Exécutez le bot :

python confession.py
Si vous souhaitez le maintenir en ligne 24/7, vous pouvez utiliser des services comme Render ou Heroku pour déployer l'application.

Commandes
!setup_confession : Affiche le panel de confession dans le salon actuel où les utilisateurs peuvent envoyer une confession anonyme.

Contribuer
Si vous souhaitez contribuer à ce projet, n'hésitez pas à soumettre une pull request. Toutes les contributions sont les bienvenues !

Remarque : Assurez-vous d'ajouter le fichier requirements.txt pour que les dépendances puissent être installées facilement sur des plateformes comme Render.
