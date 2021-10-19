# projet UTAH
Application web pour l'aide à la prescription

## Objectif
Management des anticoagulants (ATC) et antiagrégants plaquettaires (AAG) durant la phase péri-opératoire

## Requirements
Python 3.10 avec Django == 3.2.8.

## Installation (Windows)

1. __Clonez le projet en local via git:__


```bash
git clone https://github.com/jeaunrg/projet-UTAH.git
```

  Vous pouvez aussi télécharger directement le projet https://github.com/jeaunrg/projet-UTAH/archive/refs/heads/main.zip


2. __Installez les librairies python dans un environement virtuel:__

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

3. __Lancer l'application web__

Démarrez le serveur django:

```bash
python ./src/manage.py runserver
```

Et ouvrez http://127.0.0.1:8000/ dans une page web

Pour se connecter en tant qu'administrateur:
- username: admin
- password: admin


4. __Gérer les processus longs en arrière plan__

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



## Author
Développé par: [jeaunrg](https://github.com/jeaunrg).
