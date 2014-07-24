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
current_dir = os.path.dirname(__file__)
session = web.session.Session(app, web.session.DiskStore(os.path.join(current_dir, 'sessions')), )
main = app.wsgifunc()
