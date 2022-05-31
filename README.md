### le projet:  
le projet est script python qui enregistre les tap de clavier (keylogger), fait des captures d'ecran, prend le contenue de clipboard, et prend des information de l'ordinateur (address IP public et prive, l'OS, le nom de la machine, ...). et envoi toutes ces donnés à un serveur wev.
le serveur est en local (localhost:8000) est une api laravel qui reçoit la data et la storer dans la BD.
le script python: https://github.com/riad-999/keylogger/blob/main/keylogger.py
le serveur: https://github.com/riad-999/keylogger-server/blob/main/routes/api.php
