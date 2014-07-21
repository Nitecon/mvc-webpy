__author__ = 'whatting'
import web
import config

from addons import utils
from addons import formatting

template_path = config.base_dir + "/app/views"

global_items = utils.get_all_functions(formatting)

view = web.template.render(template_path, cache=config.get_cache_config(), globals=global_items)

def get_view():
    return view