# NewCthulhuBot
Nouvelle version du bot Discord !

## Initialisation du projet
- Installer Python 3 : https://www.python.org/downloads/
- Installer Git : https://git-scm.com/downloads
- Récupérer le code en clonant le dossier : `git clone https://github.com/Teazane/NewCthulhuBot.git`
- (optionnel) Installer virtualenv avec la commande : `pip install virtualenv`
- (optionnel) Créer l'environnement virtuel : `virtualenv env`
- (optionnel) Activer l'environnement virtuel : `.\env\Scripts\activate`
- Installer les dépendances du projet : `pip install -r requirements.txt`
- Créer le fichier `token.config` à la racine du projet au format suivant :
```
[DEFAULT]
token = ICILETOKENDUBOT
```

Il ne reste plus qu'à lancer le projet avec `python main.py`.

Pour mettre à jour le projet, lancer `git pull`.

## Fonctionnalités
Le bot est capable de :
- Répondre à un ping
- Répondre aléatoirement "Toi-même, 'spèce de ..." 1 fois sur 50 où le "..." est le dernier mot de plus de 3 caractères de la phrase (TODO : en excluant les mots en -er, -ez et -ir)
- Répondre à "C'est pas faux"
- Répondre quand on parle de lui, répond à un merci qui lui est adressé
- Corrige les gens quand on inverse le premier T et H de son prénom
- Réagir au mot "humain"
- Réagir au mot "mécréant"
- Réagir à "fuck"
- Réagir à "tanche"
- Réagir à "perd(*)", "jeu(x)" et "game(s)"
- Réagir au mot "dégueulasse"
- Se tait 15 minutes lors d'un "Silence Cthulhu"
- Se vexe 15 minutes lors d'un "Ta gueule Cthulhu"
- Réagir à "!livredor" pour obtenir une citation au hasard
- Réagir à "!livredor auteur=Prénom" (n'oubliez pas la majuscule) pour obtenir une citation d'une personne en particulier
- Réagir à "!help" pour obtenir une aide simple
- Réagir à "!info" pour obtenir plus de détails

## TODO
- Régler le fait que certains matches se produisent avant d'autres (ex : "Cthulhu" avant "Merci Cthulhu").
- Exclure les mots peu intéressant de la réaction "Toi-même" (en excluant les mots en -er, -ez et -ir).
- Répondre à un "bonne nuit".

## Built with / using
- Python 3 (3.6)
- Discord.py (Discord API for Python)
- Other libs listed in `requirements.txt`

## Auteur et license
Codé avec amour par Teazane. 
Licence MIT.