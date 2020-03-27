"""
WSGI config for minerals_catalog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

path = "/home/adamkielar/minerals_catalog_v2/minerals_catalog"
if path not in sys.path:
        sys.path.append(path)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'minerals_catalog.settings')

application = get_wsgi_application()
