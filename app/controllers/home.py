# Author: Will Hattingh


from app.models import tutorial

import app


class index:
    def GET(self):
        return app.layout("Neustar Bootstrap - Home", app.view.home(tutorial.get_random_words()))
