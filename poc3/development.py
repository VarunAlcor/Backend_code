from .settings import *  # noqa
import os
DEBUG = False
DATABASES["default"] = {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': os.environ.get("DB_NAME"),
    'USER': os.environ.get("DB_USER"),
    'PASSWORD': os.environ.get("DB_PASSWORD"),
    'HOST': os.environ.get("DB_HOST"),
    'PORT': 'localhost',
}
AWS_KEY = os.environ.get("AWS_KEY_ID")
AWS_SECRET = os.environ.get("AWS_SECRET")
