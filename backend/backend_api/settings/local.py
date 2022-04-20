from .base import *
from .base import env


DEBUG = True




# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("DJANGO_SECRET_KEY",default='django-insecure-@-w+)f%=iptmy&^w76m5*)gcejab!sfu!ibk!fpkz&ysv668i(')

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]
CSRF_TRUSTED_ORIGINS = ['http://localhost:8080/*']

EMAIL_BACKEND="djcelery_email.backends.CeleryEmailBackend"
EMAIL_HOST=env("EMAIL_HOST",default="mailhog")
EMAIL_PORT=env("EMAIL_PORT")
DEFAULT_FROM_EMAIL="mauer.vladimir@web.de"
DOMAIN=env("DOMAIN")
SITE_NAME = "backend_api"
