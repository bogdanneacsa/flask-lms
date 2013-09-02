# -*- coding: utf-8 -*-

'''
Created on Aug 28, 2013

.. moduleauthor:: Bogdan Neacsa <bogdan.neacsa.valentin@gmail.com>
'''

from functools import wraps

from flask import jsonify

from .. import assets
from .. import factory


def create_app(settings_override=None, register_security_blueprint=False):
    """Any customization needed for the api app should be done here"""

    app = factory.create_app(__name__, __path__, settings_override,
                             register_security_blueprint=register_security_blueprint)
    assets.init_app(app)
    return app


def route(bp, *args, **kwargs):
    kwargs.setdefault('strict_slashes', False)

    def decorator(f):
        @bp.route(*args, **kwargs)
        @wraps(f)
        def wrapper(*args, **kwargs):
            return f(*args, **kwargs)
        return f

    return decorator
