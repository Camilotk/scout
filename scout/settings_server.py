# -*- coding:utf-8 -*-
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#k2b=qc#a)yy9^)4j1u&(+pq7s&mrp^me=#7n+c#pk!ayr@=6t'

ALLOWED_HOSTS = [
    'localhost'
]

# Admin user: guerra pass: g
ADMINS = (
    ('Rober Guerra', 'roberzguerra@gmail.com'),
)

MANAGERS = ADMINS
#
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'site', # Or path to database file if using sqlite3: os.path.join(BASE_DIR, 'db.sqlite3'),
        'USER': 'adminsewn3ha', # Not used with sqlite3.
        'PASSWORD': 'ZM39mKJlMNBv', # Not used with sqlite3.
        'HOST': 'postgresql://$OPENSHIFT_POSTGRESQL_DB_HOST', # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '$OPENSHIFT_POSTGRESQL_DB_PORT', # Set to empty string for default. Not used with sqlite3.
    }
}

# Django-debug-toolbar configs
DEBUG_TOOLBAR_PATCH_SETTINGS = True
DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    #'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]
INTERNAL_IPS = [
    '127.0.0.1'
]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' #Envia email real
EMAIL_HOST = 'smtp.gmail.com' #default='localhost'
EMAIL_HOST_USER = 'roberzguerra2@gmail.com'
EMAIL_HOST_PASSWORD = '54xrober'
EMAIL_PORT = 587
EMAIL_USE_TLS = True