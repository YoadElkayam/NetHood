import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@=hz9_t7^-heo6ty6z5i1w2x10523-7@(cm9t3opa^p@92dt^*'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'qqaynkbi',
        'USER': 'qqaynkbi',
        'PASSWORD': 'RZnE6gJUY3EILIO9CtvX1VU6h9eY44A3',
        'HOST': 'horton.elephantsql.com',
        'PORT': '5432',
    }
}
