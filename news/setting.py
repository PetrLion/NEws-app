import os
from urllib.parse import urlparse


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB', 'mynewsdb'),
        'USER': os.getenv('POSTGRES_USER', 'user'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'password'),
        'HOST': os.getenv('POSTGRES_HOST', 'db'),
        'PORT': os.getenv('POSTGRES_PORT', '5432'),
    }
}


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


ALLOWED_HOSTS = [ 'localhost', '127.0.0.1'] 
CSRF_TRUSTED_ORIGINS = ['https://your-domain.com'] 
SECURE_SSL_REDIRECT = True 
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
