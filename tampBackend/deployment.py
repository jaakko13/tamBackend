from .settings import *
import os

# Configure the domain name using the environment variable
# that Azure automatically creates for us.
# ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']] if 'WEBSITE_HOSTNAME' in os.environ else []
ALLOWED_HOSTS = ['*']

DEBUG = False

# import os 
# from .settings import *
# from .settings import BASE_DIR

# ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']]
# CSRF_TRUSTED_ORIGINS = ['https://'+os.environ['WEBSITE_HOSTNAME']]
# DEBUG = False


# from dotenv import load_dotenv

# load_dotenv()
# PW = os.getenv('SQL_PW')
# USER = os.getenv('SQL_USER')

# SECRET_KEY = os.environ['SECRET_KEY']

# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'whitenoise.middleware.WhiteNoiseMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]

# ROOT_URLCONF = 'tampBackend.urls'

# INSTALLED_APPS = [
#     "whitenoise.runserver_nostatic",
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'api',
#     'rest_framework',
# ]

# CORS_ALLOWED_ORIGINS = [
#     'https://tamhattan.azurewebsites.net' 
# ]

# DATABASES = {
#     'default': {
#         'ENGINE': 'mssql',
#         'NAME': 'tamhattanDB',
#         'USER': USER,
#         'PASSWORD': PW,
#         'HOST': 'tamdb.database.windows.net',
#         'PORT': '',
#         'OPTIONS': {
#             'driver': 'ODBC Driver 18 for SQL Server',
#         },
#     }
# }

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'mail_admins': {
#             'level': 'ERROR',
#             'class': 'django.utils.log.AdminEmailHandler',
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['mail_admins'],
#             'level': 'ERROR',
#             'propagate': True,
#         },
#     },
# }

# STATIC_ROOT = BASE_DIR/'staticfiles'