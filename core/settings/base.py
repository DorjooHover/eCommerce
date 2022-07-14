import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = '3xk*)i0x#k$btl=(6q)te!19=mp6d)lm1+zl#ts4ewxi3-!vm_'

DEBUG = True

ALLOWED_HOSTS = ['yourdomain.com', '127.0.0.1', 'localhost']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_countries',
    'store',
    'basket',
    'account',
    'payment',
    'orders',
    'mptt',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'store.context_processors.categories',
                'basket.context_processors.basket',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')


# Custom user model
AUTH_USER_MODEL = 'account.UserBase'
LOGIN_REDIRECT_URL = '/account/dashboard'
LOGIN_URL = '/account/login/'

# PASSWORD_RESET_TIMEOUT_DAYS = 2
# Email setting
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

BASKET_SESSION_ID = 'basket'

os.environ.setdefault('STRIPE_PUBLISHABLE_KEY', 'pk_test_51LKvGACnhU5ZPryDMQxm2RRkbIMtplSt5Tl0Z1ann3840WCSrcEO6g5AB8Tsq07FsdaG9BgU7L5sKOmt1x4Rf9k100KYejx7dc')
# STRIPE_SECRET_KEY = 'whsec_9ad7908f2f30300e9ea36910fbad4a80d41f2dddc5bd78eae20f389dc0fbb68e'
PUBLISHABLE_KEY = 'pk_test_51LKvGACnhU5ZPryDMQxm2RRkbIMtplSt5Tl0Z1ann3840WCSrcEO6g5AB8Tsq07FsdaG9BgU7L5sKOmt1x4Rf9k100KYejx7dc'
STRIPE_SECRET_KEY = 'sk_test_51LKvGACnhU5ZPryDrWGf9oexKOfVIGTS7P8D8uA15VpKKMVcMmC3kbM8tVwG4SqwcJTXqLvOa3AMVMCEUahygkPW00IVo2dlvQ'