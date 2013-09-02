# -*- coding: utf-8 -*-

'''
Created on Aug 28, 2013

.. moduleauthor:: Bogdan Neacsa <bogdan.neacsa.valentin@gmail.com>

TODO: Add short description of what this module contains (delete line if not necessary)
'''

from flask import Flask
from flask_security import SQLAlchemyUserDatastore

from .core import db, security
from .helpers import register_blueprints
from .users.models import User, Role


def create_app(package_name, package_path, settings_override=None,
               register_security_blueprint=True):
    """
    Returns a :class:`Flask` application instance configured with common functionality.
    
    :param package_name: application package name
    :param package_path: application package path
    :param settings_override: a dictionary of settings to override
    :param register_security_blueprint: flag to specify if the Flask-Security
                                        Blueprint should be registered. Defaults to `True`.
    """
    app = Flask(package_name, instance_relative_config=True)

    app.config.from_object('easy_lms.settings')
    app.config.from_pyfile('settings.cfg', silent=True)
    app.config.from_object(settings_override)

    db.init_app(app)
    security.init_app(app, SQLAlchemyUserDatastore(db, User, Role), register_blueprint=register_security_blueprint)
    
    register_blueprints(app, package_name, package_path)
    
    return app

