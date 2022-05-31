### le projet:  
le projet est un script python qui enregistre les tapes de clavier (keylogger), fait des captures d'ecran, prend le contenue de clipboard, et prend des information de l'ordinateur (address IP public et prive, l'OS, le nom de la machine, ...). et envoi toutes ces donnés à un serveur web.
le serveur est en local (localhost:8000) est une api laravel qui reçoit la data et la storer dans la BD.


le script python: https://github.com/riad-999/keylogger/blob/main/keylogger.py

le serveur: https://github.com/riad-999/keylogger-server/blob/main/routes/api.php

la BD: https://github.com/riad-999/keylogger/blob/main/database.sql

### des remarques:
. il fault désactiver l'entivirus

. il est recomandé de faire l'execution en python3

. aprés l'exécution vous trouver les fichier de la data récuperer dans le répetoire actuele

. vous trouvez les exigances dans requirments.txt : https://github.com/riad-999/keylogger/blob/main/requirements.txt . exécuter pip install -r requirements.txt pour les installer.
 
