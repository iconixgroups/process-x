"""
WSGI config for Process X project.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named `application`. Django's `runserver` and `gunicorn` will look for this variable.
"""

import os
from django.core.wsgi import get_wsgi_application

# Set the default Django settings module for the 'Process X' project.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

# Get the WSGI application for the 'Process X' project.
application = get_wsgi_application()
