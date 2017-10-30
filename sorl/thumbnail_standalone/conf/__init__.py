#from django.conf import settings as user_settings
from sorl.thumbnail_standalone.lazy import LazyObject
from sorl.thumbnail_standalone.conf import defaults


class Settings(object):
    pass


class LazySettings(LazyObject):
    def _setup(self):
        self._wrapped = Settings()
        for obj in (defaults, user_settings):
            for attr in dir(obj):
                if attr == attr.upper():
                    setattr(self, attr, getattr(obj, attr))


settings = LazySettings()
