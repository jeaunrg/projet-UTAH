# projet UTAH
Application web pour l'aide à la prescription

## Objectif
Management des anticoagulants (ATC) et antiagrégants plaquettaires (AAG) durant la phase péri-opératoire

## Requirements
Python 3.10 avec Django == 3.2.8.

## Installation (Windows)

### Clonez le projet en local via git:


```bash
git clone https://github.com/jeaunrg/projet-UTAH.git
```

  Vous pouvez aussi télécharger directement le projet https://github.com/jeaunrg/projet-UTAH/archive/refs/heads/main.zip


### Installez les librairies python dans un environement virtuel:

```bash
cd root\path\to\projet-UTAH\
```

- Créez l'environement virtuel:

```bash
python3 -m venv venv
```

- Activez l'environement:

```bash
./venv/Scripts/activate
```

- Installez les librairies python

```bash
pip install -r ./src/requirements.txt
```

### Lancer l'application web

Démarrez le serveur django:

```bash
python ./src/manage.py runserver 0.0.0.0:8000
```

Pour se connecter en tant qu'administrateur:
- username: admin
- password: admin

#### Hébergement et connection sur le même PC
Ouvrir http://127.0.0.1:8000/ dans une page web

#### Connection à partir d'un autre appareil
- Se connecter au même réseau que le PC hébergeur
- Ouvrir http://[adresse-IP-du-PC]:8000/ dans une page web
  Example: http://192.168.1.100:8000/


### Gérer les processus longs en arrière plan

Si vous voulez lancer des processus en arrière plan, il est nécessaire d'installer
`celery` pour gérer ces tâches: https://docs.celeryproject.org/en/stable/getting-started/first-steps-with-celery.html

Une fois installé, ouvrez un nouveau terminal et déplacez vous dans le dossier source,

```bash
cd root\path\to\projet-UTAH\src\
```

Puis lancez la commande suivante:

```bash
celery -A mysite worker -l info -P gevent
```

!! Si vous modifiez le code d'une tâche dans un fichier 'tasks.py', il faut relancer la commande précédente pour appliquer les changements.


### Réinitialiser l'applications

#### Réinitialiser les modèles:

- Supprimer les fichiers python (sauf '__init__.py) dans tous les sous-dossiers 'migrations'
- Relancer les migrations
```bash
python ./src/manage.py makemigrations
python ./src/manage.py migrate
```

#### Réinitialiser la base de données:

- supprimer la base de données db.sqlite3 à la racine
- recréer un super utilisateur (username=admin, email=youremail@adress.com, password=admin)
```bash
python ./src/manage.py createsuperuser
```





## Author
Développé par: [jeaunrg](https://github.com/jeaunrg).
