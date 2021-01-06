import pytest

from django.test import TestCase, override_settings
from .views import *

# Needed for testing with user
MIDDLEWARES_FOR_TESTING = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'logging_middleware.middlewares.__TestingMiddleware',
        "logging_middleware.middlewares.DjangoLoggingMiddleware"
]

class TestMiddleware(TestCase):
    
    def test_middleware_simple_get_request(self):
        try:
            self.client.get('/get_simple')
        except Exception as e:
            pytest.fail(f"Error: {e}")
