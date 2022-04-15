import environ
from pathlib import Path

env = environ.Env()

ROOT_DIR = Path(__file__).resolve().parent.parent.parent


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
APPS_DIR = ROOT_DIR / 'core_apps'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DJANGO_DEBUG", False) 


# django defined apps
DJANGO_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
]

#external apps
THIRD_PARTY_APPS = [
    'rest_framework',
    'django_filters',
    'django_countries',
    'phonenumber_field',
    'drf_yasg',
    'corsheaders',
]

#my apps
LOCAL_APPS = ['core_apps.common', 'core_apps.profiles', 'core_apps.users']

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.common.BrokenLinkEmailsMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend-api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(APPS_DIR / "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'backend-api.wsgi.application'


# Database
DATABASES = {"default":env.db("DATABASE_URL")}
DATABASES["default"]["ATOMIC_REQUESTS"] = True

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
]

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Dublin'

USE_I18N = True

USE_TZ = True

SITE_ID = 1

ADMIN_URL = "supersecret/"

ADMINS = [("Vladimir Mauer","mauer.vladimir@web.de")]

MANAGERS = ADMINS




# Static files (CSS, JavaScript, Images)
STATIC_URL = '/staticfiles/'
STATIC_ROOT = str(ROOT_DIR / 'staticfiles')
STATICFILES_DIR = []
STATICFILES_FINDER = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

#Media files 
MEDIA_URL = '/mediafiles/'
MEDIA_ROOT = str(ROOT_DIR / 'mediafiles')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_URLS = r"^/api/.*$"