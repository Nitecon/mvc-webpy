# Author: Will Hattingh

import app


class index:
    def GET(self):
        return app.layout(app.view.hello(__name__), "Neustar Bootstrap - Hello")
