"""
Django settings for myproject project.

Generated by 'django-admin startproject' using Django 2.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

from django.utils.text import gettext_lazy as gettext
from django.utils.translation import ugettext_lazy as _

from auth_extra.password_validation import (
    SpecialCharacterInclusionValidator)


USE_DJANGO_CRISPY_FORMS = False
CRISPY_TEMPLATE_PACK = 'bootstrap4'


# Build paths inside the project like this:
# os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#l97f50r2m4ywrqp=!xn4vwadrr6@$19(2_2fp6vfw_ktfo@1a'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
if os.environ.get('DJANGO_USE_DEBUG'):
    DEBUG = True

ALLOWED_HOSTS = ['localhost']
if os.environ.get('SITE_HOST'):
    ALLOWED_HOSTS.append(os.environ.get('SITE_HOST'))

SITE_ID = 1

ADMINS = (
    ('Admin User', 'administrator@example.com'),
)

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django.forms',
    'crispy_forms',
    'haystack',
    'sorl.thumbnail',
    'watermarker',
    'social_django',
    'cms',
    'menus',
    'treebeard',
    'djangocms_admin_style',
    'sekizai',
    'mptt',
    'django_mptt_admin',
    'tastypie',
    'rest_framework',
    # local apps
    'artists',
    'bulletin_board',
    'cms_extensions',
    'custom_admin',
    'cv',
    'editorial',
    'email_messages',
    'external_auth',
    'guerrilla_patches',
    'ideas',
    'likes',
    'locations',
    'magazine',
    'movies',
    'music',
    'quotes',
    'products',
    'search',
    'utils',
    'viral_videos',
]
if os.environ.get('DJANGO_USE_DEBUG_TOOLBAR'):
    INSTALLED_APPS += ('debug_toolbar',)

MIDDLEWARE = [
    'cms.middleware.utils.ApphookReloadMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    "utils.middleware.ThreadLocalMiddleware",
]
if os.environ.get('DJANGO_USE_DEBUG_TOOLBAR'):
    MIDDLEWARE += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',)
    DEBUG_TOOLBAR_CONFIG = {
        "DISABLE_PANELS": [],
        "SHOW_TOOLBAR_CALLBACK": "utils.misc.custom_show_toolbar",
        "SHOW_TEMPLATE_CONTEXT": True,
    }
    DEBUG_TOOLBAR_PANELS = [
        "debug_toolbar.panels.versions.VersionsPanel",
        "debug_toolbar.panels.timer.TimerPanel",
        "debug_toolbar.panels.settings.SettingsPanel",
        "debug_toolbar.panels.headers.HeadersPanel",
        "debug_toolbar.panels.request.RequestPanel",
        "debug_toolbar.panels.sql.SQLPanel",
        "debug_toolbar.panels.templates.TemplatesPanel",
        "debug_toolbar.panels.staticfiles.StaticFilesPanel",
        "debug_toolbar.panels.cache.CachePanel",
        "debug_toolbar.panels.signals.SignalsPanel",
        "debug_toolbar.panels.logging.LoggingPanel",
        "debug_toolbar.panels.redirects.RedirectsPanel",
    ]

MIDDLEWARE_CLASSES = MIDDLEWARE

ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [
        os.path.join(BASE_DIR, "templates"),
    ],
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.template.context_processors.i18n',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
            'cms.context_processors.cms_settings',
            'sekizai.context_processors.sekizai',
        ],
    },
}]

CMS_TEMPLATES = (
    ("cms/default.html", _("Default")),
    ("cms/magazine.html", _("Magazine")),
    ("cms/start.html", _("Homepage")),
)

WSGI_APPLICATION = 'myproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

if os.environ.get('MYSQL_HOST'):
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': os.environ.get('MYSQL_HOST'),
        'NAME': os.environ.get('MYSQL_DATABASE'),
        'USER': os.environ.get('MYSQL_USER'),
        'PASSWORD': os.environ.get('MYSQL_PASSWORD'),
    }


# Logging
# https://docs.djangoproject.com/en/dev/topics/logging/
LOGGING = {
    'version': 1,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },

    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/var/log/app.log',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}

if DEBUG:
    # make all loggers use the console.
    for logger in LOGGING['loggers']:
        LOGGING['loggers'][logger]['handlers'] = ['console']


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTHENTICATION_BACKENDS = [
    'external_auth.backends.Auth0',
    'django.contrib.auth.backends.ModelBackend',
]

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'UserAttributeSimilarityValidator',
        'OPTIONS': {
            'max_similarity': 0.5,
        },
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 12,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'NumericPasswordValidator',
    },
    {
        'NAME': 'auth_extra.password_validation.'
                'MaximumLengthValidator',
        'OPTIONS': {
            'max_length': 32,
        },
    },
    {
        'NAME': 'auth_extra.password_validation.'
                'SpecialCharacterInclusionValidator',
        'OPTIONS': {
            'special_chars': ('{', '}', '^', '&') +
                SpecialCharacterInclusionValidator.
                DEFAULT_SPECIAL_CHARACTERS
        }
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en'

LANGUAGES = (
    ("en", "English"),
    ("de", "Deutsch"),
    ("fr", "Français"),
    ("lt", "Lietuvių kalba"),
)

CMS_LANGUAGES = {
    "default": {
        "public": True,
        "hide_untranslated": False,
        "redirect_on_fallback": True,
    },
    1: [
        {
            "public": True,
            "code": "en",
            "hide_untranslated": False,
            "name": gettext("en"),
            "redirect_on_fallback": True,
        },
        {
            "public": True,
            "code": "de",
            "hide_untranslated": False,
            "name": gettext("de"),
            "redirect_on_fallback": True,
        },
        {
            "public": True,
            "code": "fr",
            "hide_untranslated": False,
            "name": gettext("fr"),
            "redirect_on_fallback": True,
        },
        {
            "public": True,
            "code": "lt",
            "hide_untranslated": False,
            "name": gettext("lt"),
            "redirect_on_fallback": True,
        },
    ],
}

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'site_static'),
]
if os.environ.get('STATIC_HOST'):
    STATIC_DOMAIN = os.environ.get('STATIC_HOST')
    STATIC_URL = 'http://%s/' % STATIC_DOMAIN

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
if os.environ.get('MEDIA_HOST'):
    MEDIA_DOMAIN = os.environ.get('MEDIA_HOST')
    MEDIA_URL = 'http://%s/' % MEDIA_DOMAIN

UPLOAD_URL = f'{MEDIA_URL}upload/'
UPLOAD_ROOT = os.path.join(MEDIA_ROOT, 'upload')

# App settings

MAGAZINE_STATUS_CHOICES = (
    ("draft", _("Draft")),
    ("imported", _("Imported")),
    ("published", _("Published")),
    ("not_listed", _("Not Listed")),
    ("expired", _("Expired")),
)

HAYSTACK_CONNECTIONS = {
    'default_en': {
        'ENGINE': 'search.multilingual_whoosh_backend.'
                  'MultilingualWhooshEngine',
        'PATH': os.path.join(BASE_DIR, 'tmp/whoosh_index_en'),
    },
    'default_de': {
        'ENGINE': 'search.multilingual_whoosh_backend.'
                  'MultilingualWhooshEngine',
        'PATH': os.path.join(BASE_DIR, 'tmp/whoosh_index_de'),
    },
    'default_fr': {
        'ENGINE': 'search.multilingual_whoosh_backend.'
                  'MultilingualWhooshEngine',
        'PATH': os.path.join(BASE_DIR, 'tmp/whoosh_index_fr'),
    },
    'default_lt': {
        'ENGINE': 'search.multilingual_whoosh_backend.'
                  'MultilingualWhooshEngine',
        'PATH': os.path.join(BASE_DIR, 'tmp/whoosh_index_lt'),
    },
}
HAYSTACK_CONNECTIONS['default'] = \
    HAYSTACK_CONNECTIONS[f'default_{LANGUAGE_CODE}']

MAPS_API_KEY = os.environ.get("MAPS_API_KEY")

SOCIAL_AUTH_AUTH0_DOMAIN = os.environ.get('AUTH0_DOMAIN')
SOCIAL_AUTH_AUTH0_KEY = os.environ.get('AUTH0_KEY')
SOCIAL_AUTH_AUTH0_SECRET = os.environ.get('AUTH0_SECRET')
SOCIAL_AUTH_AUTH0_SCOPE = ['openid', 'profile']
SOCIAL_AUTH_TRAILING_SLASH = False

LOGIN_URL = '/login/auth0'
LOGIN_REDIRECT_URL = '/dashboard/'
LOGOUT_REDIRECT_URL = '/'

CACHES = {
    'memcached': {
        'BACKEND': 'django.core.cache.backends.'
                   'memcached.MemcachedCache',
        'LOCATION': os.environ.get('CACHE_LOCATION',
                                   '127.0.0.1:11211'),
        "TIMEOUT": 60, # 1 minute
        "KEY_PREFIX": os.environ.get('CACHE_KEY',
                                     'myproject_production'),
    },
    'redis': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': os.environ.get('CACHE_LOCATION',
                                   'redis://127.0.0.1:6379/1'),
        "TIMEOUT": 60, # 1 minute
        "KEY_PREFIX": os.environ.get('CACHE_KEY',
                                     'myproject_production'),
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'IGNORE_EXCEPTIONS': True,
        },
    },
}
CACHES['default'] = CACHES['memcached']
# or
# CACHES['default'] = CACHES['redis']

CMS_APPHOOKS = (
    "movies.cms_apps.MoviesApphook",
)

CMS_PLACEHOLDER_CONF = {
    "main_content": {
        "name": gettext("Main Content"),
        "plugins": (
            "EditorialContentPlugin",
            "TextPlugin",
        ),
    },
    "cms/magazine.html main_content": {
        "name": gettext("Magazine Main Content"),
        "plugins": (
            "EditorialContentPlugin",
            "TextPlugin"
        ),
        "extra_context": {
            "editorial_content_template":
                "cms/plugins/editorial_content/magazine.html",
        }
    },
}

LAST_FM_API_KEY = os.environ.get('LAST_FM_API_KEY')

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions."
        "DjangoModelPermissionsOrAnonReadOnly"
    ],
    "DEFAULT_PAGINATION_CLASS":
        "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 100,
}
