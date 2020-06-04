# Mineral Catalog

## Description

This app displays information about various minerals (AKA rocks).

## Technologies and Packages Used in App

* Django
* [Django Bootstrap4](https://pypi.org/project/django-bootstrap4/)
* [Django Debug Toolbar](https://pypi.org/project/django-debug-toolbar/)
* [Django Filter](https://pypi.org/project/django-filter/)

## How to use

1. Add minerals to database.

* Command file directory: minerals/management/commands/populate.py
* JSON file directory: minerals/management/commands/minerals.json
* Command: python manage.py populate minerals/management/commands/minerals.json

2. Run app

* python3 -m venv env
* source ./env/bin/activate
* pip install --upgrade pip && pip install -r requirements.txt
* python manage.py migrate
* python manage.py runserver 0.0.0.0:8000
