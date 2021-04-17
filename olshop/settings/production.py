from .base import * 
import dj_database_url
from decouple import config

DEBUG = False

ALLOWED_HOSTS += ['liannie.herokuapp.com', '127.0.0.1']

STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DATABASES['default'].update(dj_database_url.config(conn_max_age=600, ssl_require=True))

EMAIL_USE_TLS = True 
EMAIL_HOST = 'smpt.gmail.com'
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587

# Configure Django App for Heroku.
import django_heroku
django_heroku.settings(locals())