# Author : Will Hattingh

import web

from addons import render
import config

from addons import utils
from addons import formatting

template_path = config.base_dir + "/global_templates"

global_items = utils.get_all_functions(formatting)

view = web.template.render(template_path, cache=config.get_cache_config(), globals=global_items)

def notfound():
    return web.notfound(
        render.layout(view.not_found(), title='File not found', mode='modeShow404'))

def internalerror():
    return web.internalerror(
        render.layout(view.internal_error(), title='Some error occured', mode='modeShow404'))

def add(app):
    app.notfound = notfound
    app.internalerror = web.config.debug and web.debugerror or internalerror