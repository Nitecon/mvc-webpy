# Author: Will Hattingh

import app

class index:
    def GET(self):
        return app.layout("Neustar Bootstrap - Hello", app.view.hello(__name__))
