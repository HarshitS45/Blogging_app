from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'abc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
# if DEBUG: 
#     # Show the url to reset the password in the console.
#     EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# else:
#     # Actually sends it to the user's email address.
#     pass

STATIC_URL = 'static/'

STATIC_ROOT = BASE_DIR / 'static'

MEDIA_URL = 'media/'

MEDIA_ROOT = BASE_DIR / 'media'