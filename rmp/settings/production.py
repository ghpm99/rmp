import os
import django_heroku
import dj_database_url
import pusher
from rmp.settings.base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'rmp'
    }
}

db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)

django_heroku.settings(locals())

PUSHER_CLIENT = pusher.Pusher(
    app_id=os.environ.get('ENV_PUSHER_APP_ID'),
    key=os.environ.get('ENV_PUSHER_KEY'),
    secret=os.environ.get('ENV_PUSHER_SECRET'),
    cluster=os.environ.get('ENV_PUSHER_CLUSTER'),
    ssl=True
)
