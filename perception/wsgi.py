"""
WSGI config for perception project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from perception.settings import STATIC_PATH

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "perception.settings")
directory = STATIC_PATH+'\images'
ext = '.jpg'
file_dict = {}
swap_dict = {}

application = get_wsgi_application()
