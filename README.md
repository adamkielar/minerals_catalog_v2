# Mineral Catalog

## Populate database with JSON file

I used custom django-admin command to add minerals to database.

*Command file directory: minerals/management/commands/populate.py
*JSON file directory: minerals/management/commands/minerals.json
*Command: python manage.py populate minerals/management/commands/minerals.json

Command to run tests: python manage.py test minerals.tests  

All Mineral Model field are type CharField. Some field are missing in JSON file so added
blank=True option to the field.

In this project I have two views:
* View with List of all minerals from database and footer with link to random mineral
* View with mineral detail page

In this project i have 3 filters:
* user can search for mineral, search filter will check all model fields
* user can search for mineral by group and category with dropdown filter
* user can search for mineral by glossary filter
