# !/usr/bin/env python
# Author: Will Hattingh


import os
import config
import web

import app.controllers


urls = (
    # front page
    '/', 'app.controllers.home.index',
    '/hello/', 'app.controllers.hello.index',
)

app = web.application(urls, globals())

def notfound():
    render = web.template.render(config.global_template_path, base='layout', cache=config.get_cache_config(), globals=globals())
    return web.notfound(render.notfound())

def internalerror():
    render = web.template.render(config.global_template_path, base='layout', cache=config.get_cache_config(), globals=globals())
    return web.notfound(render.internalerror())

# You can change this to run only under the else condition (above app.wsgifunc()) to show as it's in prod.
app.notfound = notfound
app.internalerror = internalerror

if __name__ == "__main__":
    app.run()
else:
    # move app.notfound and app.internalerror here if you want to show them only in production envs
    current_dir = os.path.dirname(__file__)
    session = web.session.Session(app, web.session.DiskStore(os.path.join(current_dir, 'sessions')), )

    application = app.wsgifunc()