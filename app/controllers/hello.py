# Author: Will Hattingh

import app

from addons import render


view = app.get_view()

class index:
    def GET(self):
        return render.layout("I like pie", view.hello("Randomness..."))
