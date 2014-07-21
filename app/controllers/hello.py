# Author: Will Hattingh

import web
import app
import config
from addons import render


view = app.get_view()
template_path = config.base_dir + "/app/views"

class index:
    def GET(self):
        data = web.template.frender(template_path + 'hello.html')
        #return render.layout(view.hello("Im the hello page!"))
        return render.layout(data)
