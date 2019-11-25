# Prérequis
 - Python 3.7.3 ;
 - pip 19.1.1.

# TL;DR
1. Cloner le projet ;
1. Aller dans `server` et lancer `python run.py` ;
1. Dans un navigateur `http://localhost:5000/ping` doit répondre *pong* ;
1. Aller dans `web` et lancer `npm run serve` ;
1. Dans le navigateur `http://localhost:8080/datastreamerchart` doit afficher l'appli.

# Installation de chocolatey

## Sous windows 7+
1. ~~Taper `cmd` dans la barre de recherche windows et valider en faisant `ctrl+shift-enter` pour ouvrir l'invite de commande en mode administrateur ;~~
1. Taper `powershell` dans la barre de recherche windows et valider en faisant `ctrl+shift-enter` pour ouvrir l'invite de commande en mode administrateur
1. Suivre la procédure d'installation du (site web de chocolatey)[https://chocolatey.org/install]

# Installation des outils de développpement

## Installation de Python 3
1. Ouvirir une invit `cmd` en administrateur ;
1. `choco install python3`.

## Installation de pip
Rien à effectuer : pip est embarqué dans python.


# Démarrage du projet
1. Cloner le projet ;
1. Entrer dans le répertoire projet ;

~~1. Création de l'espace virtuel `virtualenv -p python.exe ENV` (l'exécutable python se trouve dans le PATH windows, cf. [stackoverflow](https://stackoverflow.com/questions/47369737/the-path-python3-from-python-python3-does-not-exist-error)) ;~~

3. Création de l'espace virtuel `python -m venv ENV` ;
1. `ENV\Scripts\activate.bat` ;
1. L'invite MS-DOS doit être préfixée par *(ENV)* ;

~~1. `pip install flask` ;~~

6. Tous les packages *python* nécessaires sont déclarés dans `requirements.txt`. Les installer en exécutant `pip install -r requirements.txt`;
1. Aller dans `web` et installer les dépendance *Vue.js* avec `npm install`

# Lancement de l'application
1. Aller dans `server` et lancer `python run.py` ;
1. Dans un navigateur `http://localhost:5000/ping` doit répondre *pong* ;
1. Aller dans `web` et lancer `npm run serve` ;
1. Dans le navigateur `http://localhost:8080/datastreamerchart` doit afficher l'appli.



