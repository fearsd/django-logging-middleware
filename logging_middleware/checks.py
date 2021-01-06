# from django.conf import settings
from django.core import checks

@checks.register
def check_settings(app_configs, **kwargs):
    # temporary solution
    return []
