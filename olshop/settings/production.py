from .base import * 
import dj_database_url
from decouple import config

DEBUG = False

ALLOWED_HOSTS += 'liannie.herokuapp.com'

STATIC_ROOT = BASE_DIR / 'staticfiles'

DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)

EMAIL_USE_TLS = True 
EMAIL_HOST = 'smpt.gmail.com'
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587