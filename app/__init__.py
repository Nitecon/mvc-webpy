__author__ = 'whatting'
import web
import config

template_path = config.base_dir + "/app/views"

view = web.template.render(template_path, cache=config.get_cache_config(), globals=globals())

def layout(page, content, **kwargs):
    return view.layout(page, content, **kwargs)

