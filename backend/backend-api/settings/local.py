from .base import *
from .base import env


DEBUG = True




# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("DJANGO_SECRET_KEY",default='django-insecure-@-w+)f%=iptmy&^w76m5*)gcejab!sfu!ibk!fpkz&ysv668i(')

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]
CSRF_TRUSTED_ORIGINS = ['http://localhost:8080/*'] 