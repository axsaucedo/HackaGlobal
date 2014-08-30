# Django settings for hackaglobal project.

import os
BASE_DIR = os.path.dirname(__file__)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

if DEBUG:
    ALLOWED_HOSTS = ['*']
    BASE_URL = 'http://127.0.0.1:8000'
else:
    ALLOWED_HOSTS = ['.hackaglobal.com']
    BASE_URL = 'http://hackaglobal.com'


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

SITE_ID = 2

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
    BASE_DIR + '/hackacities/static',
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
    'social_auth.context_processors.social_auth_by_type_backends',
    'social_auth.context_processors.social_auth_login_redirect',
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


#    HackaGlobal Custom Middleware
if not DEBUG:
    MIDDLEWARE_CLASSES += ('hackaglobal.hg_middleware.SubdomainMiddleware',)
#MIDDLEWARE_CLASSES += (
#    'hackaglobal.hg_middleware.UsersRedirectMiddleware',
#)


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

    'social_auth',
    #    'djangotoolbox',
    'south',

    'hackaglobal',
    'apihg',
    'accounts',
    'hackacities',

    'taggit',
    'corsheaders',
    'rest_framework',
    )

#CORS_ORIGIN_ALLOW_ALL = True
#
#REST_FRAMEWORK = {
#    'PAGINATE_BY': 10,
##    'DEFAULT_PERMISSION_CLASSES': (
##        'rest_framework.permissions.IsAuthenticated',
##        'rest_framework.permissions.DjangoModelPermissions',
##        ),
#}

AUTH_PROFILE_MODULE = "accounts.UserProfile"

SOCIAL_AUTH_PIPELINE = (
    'social_auth.backends.pipeline.social.social_auth_user',
    'social_auth.backends.pipeline.user.get_username',
    'social_auth.backends.pipeline.user.create_user',
    'social_auth.backends.pipeline.social.load_extra_data',
    'social_auth.backends.pipeline.user.update_user_details',
    'social_auth.backends.pipeline.associate.associate_by_email',
    'social_auth.backends.pipeline.social.associate_user',
    'social_auth.backends.pipeline.misc.save_status_to_session',


#    'social.pipeline.social_auth.social_details',
#    'social.pipeline.social_auth.social_uid',
#    'social.pipeline.social_auth.auth_allowed',
#    'social_auth.backends.pipeline.social.social_auth_user',
#    'social_auth.backends.pipeline.associate.associate_by_email',
#    'social_auth.backends.pipeline.misc.save_status_to_session',

#    'accounts.pipelines.redirect_to_username_form',

#    'social_auth.backends.pipeline.user.create_user',
#    'social_auth.backends.pipeline.social.associate_user',
#    'social_auth.backends.pipeline.social.load_extra_data',
#    'social_auth.backends.pipeline.user.update_user_details',
#    'social_auth.backends.pipeline.misc.save_status_to_session',

    'accounts.pipelines.get_user_avatar',
)

AUTHENTICATION_BACKENDS = (
    'social_auth.backends.contrib.vk.VKOAuth2Backend',
    'social_auth.backends.contrib.github.GithubBackend',
    'social_auth.backends.facebook.FacebookBackend',

    'django.contrib.auth.backends.ModelBackend',
)

LOGIN_URL          = '/accounts/login/'
LOGIN_REDIRECT_URL = '/accounts/view/'
LOGIN_ERROR_URL    = '/accounts/error/'

SOCIAL_AUTH_CREATE_USERS          = True
SOCIAL_AUTH_ASSOCIATE_BY_MAIL     = True
SOCIAL_AUTH_UUID_LENGTH           = 3

SOCIAL_AUTH_ENABLED_BACKENDS = ('facebook', 'vk-oauth', 'github',)
SOCIAL_AUTH_COMPLETE_URL_NAME = 'socialauth_complete'
SOCIAL_AUTH_EXTRA_DATA = False
SOCIAL_AUTH_CHANGE_SIGNAL_ONLY = True

FACEBOOK_EXTENDED_PERMISSIONS = ['email']
GITHUB_EXTENDED_PERMISSIONS = ['email']
VK_EXTENDED_PERMISSIONS = ['email']

FACEBOOK_APP_ID     = '1471335216431010'
FACEBOOK_API_SECRET = 'c431a9791273a11a48328e45fa23fb27'
VK_APP_ID           = '4311608'
VK_API_SECRET       = 'WH9dQg836Y5GkrbEdTLr'
GITHUB_APP_ID       = '24efcccb1598fff7c1e5'
GITHUB_API_SECRET   = '924aa90d8e323dd0b58f9ca88f5a6d3d972a39e1'

if DEBUG:
    VK_APP_ID           = '4528658'
    VK_API_SECRET       = 'Boub2hzv7x5QZf30P8z5'
    GITHUB_APP_ID       = '9710cc379c36e5557ed8'
    GITHUB_API_SECRET   = '6d9f1953495d4f624fc9cc2fcf314cf56f0bb92e'
    FACEBOOK_APP_ID     = '1543129689251562'
    FACEBOOK_API_SECRET = '0c8172e5ee3eb3a48c335da81769c591'