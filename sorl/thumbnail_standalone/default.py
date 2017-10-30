# from django.utils.functional import LazyObject

from sorl.thumbnail_standalone.conf import settings
from sorl.thumbnail_standalone.helpers import get_module_class
from sorl.thumbnail_standalone.lazy import LazyObject

class KVStore(LazyObject):
    def _setup(self):
        self._wrapped = get_module_class(settings.THUMBNAIL_KVSTORE)()


class Engine(LazyObject):
    def _setup(self):
        self._wrapped = get_module_class(settings.THUMBNAIL_ENGINE)()


class Storage(LazyObject):
    def _setup(self):
        self._wrapped = get_module_class(settings.THUMBNAIL_STORAGE)()


kvstore = KVStore()
engine = Engine()
storage = Storage()
