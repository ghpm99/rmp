import pusher
from rmp.settings import local_settings
from rmp.settings.base import *

try:
    from rmp.settings.local_settings import *
except ImportError:
    pass

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-4#5_h&!mn1v^d0bzvvk_1p5rq^!yj6p&e@j+oq_x(t+h*_u#zv'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'rmp',
        'USER': 'postgres',
        'PASSWORD': '1234',
        'HOST': 'postgres'
    }
}

PUSHER_CLIENT = pusher.Pusher(
    app_id=local_settings.ENV_PUSHER_APP_ID,
    key=local_settings.ENV_PUSHER_KEY,
    secret=local_settings.ENV_PUSHER_SECRET,
    cluster=local_settings.ENV_PUSHER_CLUSTER,
    ssl=True
)
