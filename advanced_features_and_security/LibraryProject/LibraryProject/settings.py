"""
Django settings for LibraryProject project.

Generated by 'django-admin startproject' using Django 5.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-x0z$dcj8846^)#!+z#hjypziv31_i=3=c1g(dy&_3&ql-r8z48"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "bookshelf.apps.BookshelfConfig",
    "relationship_app",
]

MIDDLEWARE = [
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "LibraryProject.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "LibraryProject.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


LOGIN_REDIRECT_URL = "home"  # Redirect after login
LOGOUT_REDIRECT_URL = "login"  # Redirect after logout
AUTH_USER_MODEL = "bookshelf.CustomUser"


# Disable Debug Mode for Production
DEBUG = False
ALLOWED_HOSTS = [
    "yourdomain.com",
    "www.yourdomain.com",
]  # Add your production domain(s)

# Browser-Side Protections
SECURE_BROWSER_XSS_FILTER = True  # Enable browser's XSS filter
SECURE_CONTENT_TYPE_NOSNIFF = (
    True  # Prevents the browser from guessing the content type
)
X_FRAME_OPTIONS = "DENY"  # Prevent the site from being framed
SECURE_PROXY_SSL_HEADER = (
    "HTTP_X_FORWARDED_PROTO",
    "https",
)  # Detect HTTPS when behind a proxy


# Cookie Security
SESSION_COOKIE_SECURE = True  # Session cookies only transmitted over HTTPS
CSRF_COOKIE_SECURE = True  # CSRF cookies only transmitted over HTTPS
SESSION_COOKIE_HTTPONLY = True  # Prevent JavaScript access to session cookies
CSRF_COOKIE_HTTPONLY = True  # Prevent JavaScript access to CSRF cookies
SESSION_COOKIE_SAMESITE = "Strict"  # Restrict session cookies to same-site requests
CSRF_COOKIE_SAMESITE = "Strict"  # Restrict CSRF cookies to same-site requests


# Use HTTPS
SECURE_SSL_REDIRECT = True

# Additional Settings for Production
SECURE_HSTS_SECONDS = 31536000  # Enforces HTTPS for one year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True  # Preloads HSTS for maximum protection
SECURE_SSL_REDIRECT = True  # Redirect all HTTP requests to HTTPS
