import pytest
from django.conf import settings as _settings
from django.test import override_settings

from logging_middleware.settings import DEFAULTS, Settings

@override_settings(DJANGO_LOGGING_MIDDLEWARE={})
def test_check_settings_if_user_didnt_set_settings():
    settings = Settings(_settings)
    assert settings.DEFAULT_FORMAT == DEFAULTS['DEFAULT_FORMAT']
    assert settings.MESSAGE_FORMAT == DEFAULTS['MESSAGE_FORMAT']

@override_settings(DJANGO_LOGGING_MIDDLEWARE={'DEFAULT_FORMAT': True, 'MESSAGE_FORMAT': '{message}'})
def test_check_settings_if_user_set_default_format_true_and_set_message_format():
    settings = Settings(_settings)
    assert settings.DEFAULT_FORMAT == DEFAULTS['DEFAULT_FORMAT']
    assert settings.MESSAGE_FORMAT == DEFAULTS['MESSAGE_FORMAT']

@override_settings(DJANGO_LOGGING_MIDDLEWARE={'DEFAULT_FORMAT': False, 'MESSAGE_FORMAT': '{message}'})
def test_check_settings_if_user_set_default_format_false_and_set_message_format():
    settings = Settings(_settings)
    assert settings.DEFAULT_FORMAT == False
    assert settings.MESSAGE_FORMAT == '{message}'

@override_settings(DJANGO_LOGGING_MIDDLEWARE={'DEFAULT_FORMAT': False})
def test_check_settings_if_user_set_default_format_false_but_didnt_set_message_format():
    settings = Settings(_settings)
    assert settings.DEFAULT_FORMAT == False
    assert settings.MESSAGE_FORMAT == DEFAULTS['MESSAGE_FORMAT']

@override_settings(DJANGO_LOGGING_MIDDLEWARE={'DEFAULT_FORMAT': True})
def test_check_settings_if_user_set_default_format_true_and_didnt_set_message_format():
    settings = Settings(_settings)
    assert settings.DEFAULT_FORMAT == DEFAULTS['DEFAULT_FORMAT']
    assert settings.MESSAGE_FORMAT == DEFAULTS['MESSAGE_FORMAT']

@override_settings(DJANGO_LOGGING_MIDDLEWARE={'MESSAGE_FORMAT': '{message}'})
def test_check_settings_if_user_didnt_set_default_format_but_set_message_format():
    settings = Settings(_settings)
    assert settings.DEFAULT_FORMAT == DEFAULTS['DEFAULT_FORMAT']
    assert settings.MESSAGE_FORMAT == DEFAULTS['MESSAGE_FORMAT']

@override_settings(DJANGO_LOGGING_MIDDLEWARE={'DEFAULT_FORMAT': ''})
def test_check_settings_if_user_set_wrong_data():
    settings = Settings(_settings)
    assert settings.DEFAULT_FORMAT == DEFAULTS['DEFAULT_FORMAT']
    assert settings.MESSAGE_FORMAT == DEFAULTS['MESSAGE_FORMAT']
