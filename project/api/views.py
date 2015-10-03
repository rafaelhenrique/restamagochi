# -*- encoding: utf-8 -*-

from ..api import api

from flask import jsonify


@api.route('/', methods=['GET', ])
def index():
    return jsonify(message="will be ok"), 200
