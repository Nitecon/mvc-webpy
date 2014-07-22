# !/usr/bin/env python
# Author: Will Hattingh


import os

import web

import app.controllers


urls = (
    # front page
    '/', 'app.controllers.home.index',
    '/hello/', 'app.controllers.hello.index',
)

app = web.application(urls, globals())

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
else:
    app = web.application(urls, globals())

    current_dir = os.path.dirname(__file__)
    session = web.session.Session(app, web.session.DiskStore(os.path.join(current_dir, 'sessions')), )

    application = app.wsgifunc()