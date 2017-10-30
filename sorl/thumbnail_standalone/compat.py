from __future__ import unicode_literals

__all__ = [
    'BufferIO',
    'urlopen',
    'urlparse',
    'quote',
    'quote_plus',
    'URLError',
]

from urllib.error import URLError
from urllib.request import Request
from urllib.request import urlopen as _urlopen
from urllib.parse import quote, quote_plus

import urllib.parse as urlparse

from io import BytesIO as BufferIO


def b(s):
    return s.encode("latin-1")


def encode(value, charset='utf-8', errors='ignore'):
    if isinstance(value, bytes):
        return value
    return value.encode(charset, errors)


def urlsplit(url):
    return urlparse.urlsplit(url.decode('ascii', 'ignore'))


# -- Urlopen with a proper default user agent

def urlopen(url):
    from sorl.thumbnail_standalone.conf import settings

    req = Request(
        url,
        headers={'User-Agent': "python-urllib3/0.6"}
    )
    return _urlopen(req, timeout=settings.THUMBNAIL_URL_TIMEOUT)
