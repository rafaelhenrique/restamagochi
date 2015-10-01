from flask import render_template

from ..api import api


@api.route('/', methods=['GET', ])
def index():
    return render_template('api.html')
