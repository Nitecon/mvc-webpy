import web
from web import http

import types
import urllib
import urlparse as _urlparse

def url_encode(url):
    return http.urlencode(url)

def url_unquote(url):
    return urllib.unquote_plus(url)

def url_parse(url):
    return web.storage(
        zip(('scheme', 'netloc', 'path', 'params', 'query', 'fragment'), _urlparse.urlparse(url)))

def url_join(url, url_relative):
    if '://' not in url_relative:
        if not url_relative.startswith('/'):
            url_relative = '/' + url_relative
    return _urlparse.urljoin(url, url_relative)

def get_user_ip():
    return web.ctx.get('ip', '000.000.000.000')


def dict_remove(d, *keys):
    for k in keys:
        if d.has_key(k):
            del d[k]

def get_extension_from_url(url):
    path = url_parse(url).path
    return path[path.rindex('.')+1:]


def get_all_functions(module):
    functions = {}
    for f in [module.__dict__.get(a) for a in dir(module)
        if isinstance(module.__dict__.get(a), types.FunctionType)]:
        functions[f.__name__] = f
    return functions