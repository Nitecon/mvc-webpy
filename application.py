# !/usr/bin/env python
# Author: Will Hattingh


import web
import config
import os
import app.controllers

from addons import custom_errors


urls = (
    # front page
    '/', 'app.controllers.home.index',
    '/hello/', 'app.controllers.hello.index',
)

app = web.application(urls, globals())
custom_errors.add(app)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
else:
    app = web.application(urls, globals())

    curdir = os.path.dirname(__file__)
    session = web.session.Session(app, web.session.DiskStore(os.path.join(curdir,'sessions')),)

    application = app.wsgifunc()