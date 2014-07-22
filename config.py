import os

import web


base_dir = os.path.abspath(os.path.dirname(__file__))

global_template_path = base_dir + "/extra/templates"

# in development debug error messages and reloader
web.config.debug = True

# in develpment template caching is set to false
cache = False

# in production the internal errors are emailed to us
web.config.email_errors = ''


def get_cache_config():
    return cache


def get_globals():
    return globals


def get_base_dir():
    return base_dir

