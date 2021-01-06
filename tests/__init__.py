from django.conf import settings
import django

settings.configure(
    SECRET_KEY = "NOTASECRET",
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        "logging_middleware", 
        "tests"
    ],
    DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3"}},
    TEMPLATES = [{"BACKEND": "django.template.backends.django.DjangoTemplates"}],
    ROOT_URLCONF = "tests.urls",
    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        "logging_middleware.middlewares.DjangoLoggingMiddleware"
    ]
)

django.setup()
