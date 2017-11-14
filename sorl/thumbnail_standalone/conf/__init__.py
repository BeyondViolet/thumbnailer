from sorl.thumbnail_standalone.lazy import LazyObject
from sorl.thumbnail_standalone.conf import defaults

class Settings(object):
    pass


class LazySettings(LazyObject):
    def _setup(self):
        self._wrapped = Settings()
        for attr in dir(defaults):
            if attr == attr.upper():
                setattr(self, attr, getattr(defaults, attr))


settings = LazySettings()
