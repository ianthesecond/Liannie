"""
WSGI config for olshop project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

<<<<<<< HEAD
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'olshop.settings.development')
=======
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'olshop.settings.production')
>>>>>>> 9a323284e1522b182f46481c8b5ee4b9c17a9d61

application = get_wsgi_application()
