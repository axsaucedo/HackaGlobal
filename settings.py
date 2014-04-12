# Django settings for hackaglobal project.

import os
BASE_DIR = os.path.dirname(__file__)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

if DEBUG:
    ALLOWED_HOSTS = ['*']
    BASE_URL = 'http://127.0.0.1:8000'
else:
    ALLOWED_HOSTS = ['.hackaglobal.co']
    BASE_URL = 'http://hackaglobal.co'


ADMINS = (
    ('Alejandro Saucedo', 'hackasoton@gmail.com'),
    )

MANAGERS = ADMINS

#Use email
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'hackaglobal@gmail.com'
EMAIL_HOST_PASSWORD = 'hacka1234'

DEFAULT_FROM_EMAIL = 'hackaglobal@gmail.com'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'hackadb',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'hacka',
        'PASSWORD': '5664021a',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['*']

TIME_ZONE = 'Europe/London'
LANGUAGE_CODE = 'en-gb'

SITE_ID = 1

# Use optimizations
USE_I18N = True

# Django should format dates
USE_L10N = True

# Application is not timezone aware
USE_TZ = False

APPEND_SLASH = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = BASE_DIR + '/hackaglobal/media'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = BASE_DIR + '/static'

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    BASE_DIR + '/hackaglobal/static',
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '0$f@0dfsd#o_^@r9m-@dk1!cz0e@m1f253kbmfed_6jlccc7=('


TEMPLATE_DIRS = (BASE_DIR + '/templates',)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    "hackaglobal.hg_context.in_prod",
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
)

CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'hackaglobal.wsgi.application'

INSTALLED_APPS = (
    'django.contrib.admin',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'djangotoolbox',
    'south',

    'hackaglobal',
    'apihg',
    'accounts',

    'taggit',
    'corsheaders',
    'rest_framework',
    'social_auth',
)

CORS_ORIGIN_ALLOW_ALL = True

REST_FRAMEWORK = {
    'PAGINATE_BY': 10,
#    'DEFAULT_PERMISSION_CLASSES': (
#        'rest_framework.permissions.IsAuthenticated',
#        'rest_framework.permissions.DjangoModelPermissions',
#        ),
}

AUTH_PROFILE_MODULE = "accounts.UserProfile"

AUTHENTICATION_BACKENDS = (
    'social_auth.backends.facebook.FacebookBackend',
    'social_auth.backends.contrib.linkedin.LinkedinBackend',
    'social_auth.backends.contrib.github.GithubBackend',
    'social_auth.backends.contrib.vk.VKOAuth2Backend',
    'social_auth.backends.OpenIDBackend',

    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_PIPELINE = (
    'social_auth.backends.pipeline.social.social_auth_user',
    'social_auth.backends.pipeline.user.get_username',
    'social_auth.backends.pipeline.user.create_user',
    'social_auth.backends.pipeline.social.associate_user',
    'social_auth.backends.pipeline.social.load_extra_data',
    'social_auth.backends.pipeline.user.update_user_details',
    'accounts.pipelines.get_user_avatar',
)

FACEBOOK_EXTENDED_PERMISSIONS = ['email']

FACEBOOK_APP_ID             = '1471335216431010'
FACEBOOK_API_SECRET         = '1f04b9e0639b57e7ce167ada194baab0'

SOCIAL_AUTH_ENABLED_BACKENDS = ('facebook',)