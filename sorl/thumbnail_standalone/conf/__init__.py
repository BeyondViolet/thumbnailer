#from django.conf import settings as user_settings
from sorl.thumbnail_standalone.lazy import LazyObject
from sorl.thumbnail_standalone.conf import defaults
import traceback
import importlib

class Settings(object):
    pass


class LazySettings(LazyObject):
    def _setup(self):
        self._wrapped = Settings()
        try:
            settings_mod = importlib.import_module('settings')
        except:
            traceback.print_exc()
            settings_mod = None
        for obj in (defaults, settings_mod):
            for attr in dir(obj):
                if attr == attr.upper():
                    setattr(self, attr, getattr(obj, attr))


settings = LazySettings()
