import django_on_heroku
from .base import *
from decouple import config

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = False

ALLOWED_HOSTS = [
    # 'toshiro-django-blog.herokuapp.com',
    '*'
]
if DEBUG: 
    # Show the url to reset the password in the console.
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# else:
#     # Actually sends it to the user's email address.
#     pass

# Amazon S3 Settings

AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')

AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')

AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')

AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com' # To build the url where files will be sent and where files will be served from.

AWS_DEFAULT_ACL = 'public-read'

AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400'
}

AWS_LOCATION = 'static'

AWS_QUERYSTRING_AUTH = False

AWS_HEADERS = {
    'Access-Control-Allow-Orign': '*',
}

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'
STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

COLLECTFAST_STRATEGY = "collectfast.strategies.boto3.Boto3Strategy"

STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'

MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
    'collectfast': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'collectfast_cache',
        'TIMEOUT': 60,
        'OPTIONS': {
            'MAX_ENTRIES': 10000
        },
    },
}
COLLECTFAST_CACHE = 'collectfast'

COLLECTFAST_DEBUG = False

COLLECTFAST_THREADS = 20

# Heroku Logging
# Prevents displaying Django Errors in Heroku Logs
# Makes app easier to debug
DEBUG_PROPAGATE_EXCEPTIONS = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'MYAPP': {
            'handlers':['console'],
            'level': 'DEBUG',
        },
    }
}

# Heroku Settings
# django_on_heroku.settings(locals(), staticfiles=False)
# del DATABASES['default']['OPTIONS']['sslmode']