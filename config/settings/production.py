"""Paramètres production — PostgreSQL, sécurité renforcée."""
from .base import *  # noqa: F403

DEBUG = False

DATABASES = {
    "default": {
        "ENGINE": config("DB_ENGINE", default="django.db.backends.postgresql"),  # noqa: F405
        "NAME": config("DB_NAME"),  # noqa: F405
        "USER": config("DB_USER"),  # noqa: F405
        "PASSWORD": config("DB_PASSWORD"),  # noqa: F405
        "HOST": config("DB_HOST", default="localhost"),  # noqa: F405
        "PORT": config("DB_PORT", default="5432"),  # noqa: F405
    }
}

CSRF_TRUSTED_ORIGINS = config("CSRF_TRUSTED_ORIGINS", default="", cast=Csv())  # noqa: F405

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = config("SECURE_SSL_REDIRECT", default=True, cast=bool)  # noqa: F405
SESSION_COOKIE_SECURE = config("SESSION_COOKIE_SECURE", default=True, cast=bool)  # noqa: F405
CSRF_COOKIE_SECURE = config("CSRF_COOKIE_SECURE", default=True, cast=bool)  # noqa: F405
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"
HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
