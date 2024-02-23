"""
ASGI config for mysite project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = get_asgi_application()
"""
import os
import sys

path=os.path.expanduser('~/Proyecto-Pulseras')
if path not in sys.path:
    sys.path.insert(0,path)
    os.environ['DJANGO_SETTINGS_MODULE']='mysite.settings'

from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler
aplication= StaticFilesHandler(get_wsgi_application())
"""