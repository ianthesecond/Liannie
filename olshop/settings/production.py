from .base import * 
import dj_database_url
from decouple import config
import cloudinary
import cloudinary_storage

INSTALLED_APPS += [
    # Media Cloudinary
    'cloudinary',
    'cloudinary_storage',
]

DEBUG = False

ALLOWED_HOSTS += ['liannie.herokuapp.com', '127.0.0.1']

STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Cloudinary stuff
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': config('CLOUDINARY_CLOUD_NAME', default=""),
    'API_KEY': config('CLOUDINARY_API_KEY', default=""),
    'API_SECRET': config('CLOUDINARY_API_SECRET', default=""),
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

DATABASES['default'].update(dj_database_url.config(conn_max_age=600, ssl_require=True))

EMAIL_USE_TLS = True 
EMAIL_HOST = 'smpt.gmail.com'
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587

# Configure Django App for Heroku.
import django_heroku
django_heroku.settings(locals())