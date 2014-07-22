__author__ = 'whatting'
import web

import config


template_path = config.base_dir + "/app/views"

view = web.template.render(template_path, cache=config.get_cache_config(), globals=globals())
base_layout = web.template.render(config.global_template_path, cache=config.get_cache_config(), globals=globals())

def layout(page, content, **kwargs):
    # If you wanted to you could create a generic layout just for this module and use view to call it
    return base_layout.layout(page, content, **kwargs)

