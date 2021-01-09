DEFAULTS = {
    'DEFAULT_FORMAT': True,
    'MESSAGE_FORMAT': "<b><green>{time}</green> <cyan>{message}</cyan></b>"
}

class Settings:
    def __init__(self, settings):
        self.settings = getattr(settings, 'DJANGO_LOGGING_MIDDLEWARE', {})
        self.set_settings()

    def set_settings(self):
        if self.settings == {}:
            self.DEFAULT_FORMAT = DEFAULTS['DEFAULT_FORMAT']
            self.MESSAGE_FORMAT = DEFAULTS['MESSAGE_FORMAT']
        elif 'DEFAULT_FORMAT' not in list(self.settings.keys()):
            self.DEFAULT_FORMAT = DEFAULTS['DEFAULT_FORMAT']
            self.MESSAGE_FORMAT = DEFAULTS['MESSAGE_FORMAT']
        elif not isinstance(self.settings['DEFAULT_FORMAT'], bool):
            self.DEFAULT_FORMAT = DEFAULTS['DEFAULT_FORMAT']
            self.MESSAGE_FORMAT = DEFAULTS['MESSAGE_FORMAT']
        elif 'DEFAULT_FORMAT' in list(self.settings.keys()):
            if not self.settings['DEFAULT_FORMAT'] and 'MESSAGE_FORMAT' in list(self.settings.keys()):
                self.DEFAULT_FORMAT = self.settings['DEFAULT_FORMAT']
                self.MESSAGE_FORMAT = self.settings['MESSAGE_FORMAT']
            elif self.settings['DEFAULT_FORMAT'] and 'MESSAGE_FORMAT' not in list(self.settings.keys()):
                self.DEFAULT_FORMAT = self.settings['DEFAULT_FORMAT']
                self.MESSAGE_FORMAT = DEFAULTS['MESSAGE_FORMAT']
            else:
                self.DEFAULT_FORMAT = self.settings['DEFAULT_FORMAT']
                self.MESSAGE_FORMAT = DEFAULTS['MESSAGE_FORMAT']
        else:
            self.DEFAULT_FORMAT = self.settings['DEFAULT_FORMAT']
            self.MESSAGE_FORMAT = self.settings['MESSAGE_FORMAT']

