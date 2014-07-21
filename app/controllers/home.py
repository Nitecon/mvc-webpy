# Author: Will Hattingh


from app.models import tutorial

import app
from addons import render


view = app.get_view()

class index:
    def GET(self):
        return render.layout("I like pie", view.home(tutorial.get_random_words()))
