from Backend_KeyBrasil.settings import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    'default' : {
        'ENGINE' : 'django.db.backends.mysql',
        'NAME' : 'api',
        'USER' : 'root',
        'PASSWORD' : 'globocore',
        'HOST' : '127.0.0.1',
        'PORT' : '3306'
    }
} 