"""
Django settings for elib project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""
# encoding: utf-8
import datetime
import os
from django.utils.translation import ugettext_lazy as _


from datetime import timedelta

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'sdr3^hbs(mb7vazj!d41lgwwdy-n9vl76#rrif8d#e)l*12c%k'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    'controlcenter',
    'jazzmin',
    'django_celery_beat',
    'serpy',
    'djoser',
    'ajax_select',
    'pymarc',
    'corsheaders',
    'import_export',
    'mptt',
    'silk',
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework.authtoken',
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    'django_twilio',
    'notifications',
    'api.v1.University',
    'api.v1.User',
    'api.v1.Book',
    'api.v1.Order',
    'drf_spectacular',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'silk.middleware.SilkyMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
#         'LOCATION': 'unique-snowflake',
#         'TIMEOUT': 60,
#         'OPTIONS': {
#             'MAX_ENTRIES': 1000
#         }
#     }
# }

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = [
    'http://localhost:8080',
    'http://localhost:8000',
    'http://localhost:8081',
]
CORS_ORIGIN_REGEX_WHITELIST = [
    'http://localhost:8080',
    'http://localhost:8000',
    'http://localhost:8081',
]

ROOT_URLCONF = 'elib.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        # 'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                # 'admin_tools.template_loaders.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
        },
    },
]
# WSGI_APPLICATION = 'elib.wsgi.application'
ACCOUNT_ACTIVATION_DAYS = 7
CRISPY_TEMPLATE_PACK = 'bootstrap4'
# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        #
        'NAME': 'avtolib',
        # 'NAME': 'autolib',
        # 'USER': 'riaztzeoxzmwek',
        'USER': 'postgres',
        # 'PASSWORD': '8be2b276ff52eaeec97e4c17db541933e464b793196fe809686b1bc724b7e1d2',
        'PASSWORD': 'postgres',
        # 'PASSWORD': 'Humo6779',
        # 'HOST': 'ec2-54-161-208-31.compute-1.amazonaws.com',
        'HOST': 'db',
        # 'HOST': 'localhost',
        'PORT': 5432,
    }
}
REST_FRAMEWORK = {
    # 'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 30
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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

AUTH_USER_MODEL = 'User.Profile'

# AUTHENTICATION_BACKENDS = 'django.contrib.auth.backends.ModelBackend'
# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "ru"

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_L10N = False

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATIC_URL = '/static/'
# STATICFILES_URL = '/staticfiles/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = "/media/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
# STATICFILES_FINDERS = ( 'django.contrib.staticfiles.finders.FileSystemFinder',
# 'django.contrib.staticfiles.finders.AppDirectoriesFinder',    #causes verbose duplicate notifications in django 1.9 )
PROTOCOL = 'HTTPS'
DOMAIN = 'autolib.tdtu.uz'
SITE_NAME = 'Autolib'
DJOSER = {
    'PASSWORD_RESET_CONFIRM_URL': 'change-password/{uid}/{token}',
    'USERNAME_RESET_CONFIRM_URL': 'auth/users/reset_username_confirm/{uid}/{token}',
    'ACTIVATION_URL': 'email-confirm/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': True,
    'SEND_CONFIRMATION_EMAIL': True,
    'PASSWORD_CHANGED_EMAIL_CONFIRMATION': True,
    'PASSWORD_RESET_CONFIRM_RETYPE': True,
    'PASSWORD_RESET_SHOW_EMAIL_NOT_FOUND': True,
    'SERIALIZERS': {},
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=10),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=10),
}
# APPEND_SLASH = False
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp-relay.sendinblue.com'
EMAIL_HOST_USER = 'rasulganiyev1999@gmail.com'
EMAIL_HOST_PASSWORD = 'mSfUv4O9CgRXczEK'

ASGI_APPLICATION = 'elib.routing.application'

JAZZMIN_SETTINGS = {
    # title of the window
    "site_title": "AUTOLIB Admin",

    # Title on the brand, and the login screen (19 chars max)
    "site_header": "Autolib",

    # square logo to use for your site, must be present in static files, used for favicon and brand on top left
    # "site_logo": "media/img/books/1.jpg",

    # Welcome text on the login screen
    # "welcome_sign": "����� ���������� �� ������������� Autolib",

    # Copyright on the footer
    "copyright": "Autolib",

    # The model admin to search from the search bar, search bar omitted if excluded
    "search_model": "Book.Book",

    # Field name on user model that contains avatar image
    "user_avatar": None,

    ############
    # Top Menu #
    ############

    # Links to put along the top menu
    "topmenu_links": [

        # Url that gets reversed (Permissions can be added)
        {"name": "Home",  "url": "admin:index", "permissions": ["auth.view_user"]},

        # external url that opens in a new window (Permissions can be added)
        {"name": _("Statistics"), "url": "https://autolib.tdtu.uz/admin/dashboard/mydash", "new_window": False},

        # model admin to link to (Permissions checked against model)
        {"model": "auth.User"},

        # App with dropdown menu to all its models pages (Permissions checked against models)
        {"app": "Book"},
    ],

    #############
    # User Menu #
    #############

    # Additional links to include in the user menu on the top right ("app" url type is not allowed)
    # "usermenu_links": [
    #     {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
    #     {"model": "Book"}
    # ],

    #############
    # Side Menu #
    #############

    # Whether to display the side menu
    "show_sidebar": True,

    # Whether to aut expand the menu
    "navigation_expanded": True,

    # Hide these apps when generating side menu e.g (auth)
    "hide_apps": [],

    # Hide these models when generating side menu (e.g auth.user)
    "hide_models": [],

    # List of apps (and/or models) to base side menu ordering off of (does not need to contain all apps/models)
    # "order_with_respect_to": ["auth", "books", "books.author", "books.book"],

    # Custom links to append to app groups, keyed on app name
    # "custom_links": {
    #     "dashboard": [{
    #         "name": "Dashboard",
    #         "url": "https://autolib.tdtu.uz/admin/dashboard/mydash",
    #         "icon": "fas fa-comments",
    #         # "permissions": ["Book.view"]
    #     }]
    # },

    # Custom icons for side menu apps/models See https://fontawesome.com/icons?d=gallery&m=free
    # for a list of icon classes
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "Book.Book": "fas fa-book",
        "Book.Journal": "fas fa-newspaper",
        "Book.Publisher": "fas fa-print",
        "Book.Author": "fas fa-user-edit",
        "Book.UDC": "fas fa-list-alt",
        "Book.DocumentType": "fas fa-clipboard",
        "Book.LibraryStorageEntry": "fas fa-archive",
        "Book.LibraryStorage": "fas fa-folder-open",
        "Book.Language": "fas fa-globe",
        "Book.Collection": "fas fa-stream",
        "Book.CopyrightMark": "fas fa-copyright",
        "Book.Editor": "fas fa-marker",
        "User.Profile": "fas fa-address-card",
        "University.University": "fas fa-university",
        "University.Faculty": "fas fa-graduation-cap",
    },
    # Icons that are used when one is not manually specified
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

    #################
    # Related Modal #
    #################
    # Use modals instead of popups
    "related_modal_active": False,

    #############
    # UI Tweaks #
    #############
    # Relative paths to custom CSS/JS scripts (must be present in static files)
    "custom_css": None,
    "custom_js": None,
    # Whether to show the UI customizer on the sidebar
    "show_ui_builder": False,

    ###############
    # Change view #
    ###############
    # Render out the change view as a single form, or in tabs, current options are
    # - single
    # - horizontal_tabs (default)
    # - vertical_tabs
    # - collapsible
    # - carousel
    "changeform_format": "vertical_tabs",
    # override change forms on a per modeladmin basis
    # "changeform_format_overrides": {"User": "collapsible", "auth.Group": "vertical_tabs",},
    # Add a language dropdown into the admin
    "language_chooser": False,
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": True,
    "brand_small_text": False,
    "brand_colour": "navbar-lightblue",
    "accent": "accent-lightblue",
    "navbar": "navbar-lightblue navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": False,
    "sidebar": "sidebar-light-lightblue",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": True,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": True,
    "theme": "flatly",
    "dark_mode_theme": None,
    "actions_sticky_top": False
}

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="https://a7fa02df22c84c7d961a814747ad1bcd@o490569.ingest.sentry.io/5554690",
    integrations=[DjangoIntegration()],
    traces_sample_rate=0.5,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)

CONTROLCENTER_DASHBOARDS = (
    ('mydash', 'elib.dashboard.MyDashboard'),
)
#
# TWILIO_ACCOUNT_SID = {TW}
# TWILIO_AUTH_TOKEN = {}
