from core.settings import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-%$9hhg2qu0tq$vm%wq@b)0ft@cu@se$-i&sf_afbj7o86mw4le"

ALLOWED_HOSTS = []

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "cofe_shopdb",
        'USER': "postgres",
        "PASSWORD": "postgres",
        "PORT": 5434,
        "HOST": "localhost",
    }
}

MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'
STATIC_ROOT = BASE_DIR / "staticfiles"

CKEDITOR_5_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"

SIMPLE_JWT["SIGNING_KEY"] = SECRET_KEY
SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'] = datetime.timedelta(days=30)
SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'] = datetime.timedelta(days=30)
SIMPLE_JWT['VERIFYING_KEY'] = ""
SIMPLE_JWT['AUDIENCE'] = None
SIMPLE_JWT['ISSUER'] = None
SIMPLE_JWT['JSON_ENCODER'] = None
SIMPLE_JWT['JWK_URL'] = None
SIMPLE_JWT['LEEWAY'] = 0
SIMPLE_JWT['ALGORITHM'] = "HS256"

CACHES['default']['LOCATION'] = "redis://127.0.0.1:6381/1"

INSTALLED_APPS += [
    "debug_toolbar"
]

MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

INTERNAL_IPS = [
    "127.0.0.1",
]
