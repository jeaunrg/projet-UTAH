# projet UTAH
Application web pour l'aide à la prescription

## Objectif
Management des anticoagulants (ATC) et antiagrégants plaquettaires (AAG) durant la phase péri-opératoire

## Requirements
Python 3.10 avec Django == 3.2.8.

## Installation (Windows)

1. Clonez le projet en local via git:


```bash
git clone https://github.com/jeaunrg/projet-UTAH.git
```

  Vous pouvez aussi télécharger directement le projet https://github.com/jeaunrg/projet-UTAH/archive/refs/heads/main.zip


2. Installez les librairies python dans un environement virtuel:

```bash
cd root\path\to\projet-UTAH\
```

Créez l'environement virtuel:

```bash
python3 -m venv venv
```

Activez l'environement:

```bash
./venv/Scripts/activate
```

Installez les librairies python

```bash
pip install -r ./src/requirements.txt
```

3. Lancer l'application web

Démarrez le serveur django:

```bash
python ./src/manage.py runserver
```

Et ouvrez http://127.0.0.1:8000/ dans une page web

Pour se connecter:
username: admin
password: admin





## Author
Développé par: [jeaunrg](https://github.com/jeaunrg).
