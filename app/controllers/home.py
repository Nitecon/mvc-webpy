# Author: Will Hattingh


from app.models import tutorial

import app


class index:
    def GET(self):
        return app.layout(app.view.home(tutorial.get_random_words()), "Neustar Bootstrap - Home")
