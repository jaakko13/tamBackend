"""
WSGI config for tampBackend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

settigns_module = 'tampBackend.deployment' if 'WEBSITE_HOSTNAME' in os.environ else 'tampBackend.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settigns_module)

application = get_wsgi_application()
