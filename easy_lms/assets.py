# -*- coding: utf-8 -*-

'''
Created on Sep 2, 2013

.. moduleauthor:: Bogdan Neacsa <bogdan.neacsa.valentin@gmail.com>
'''

from flask_assets import Environment, Bundle

css_all = Bundle("css/bootstrap/bootstrap.min.css", output="css/easy_lms_all.min.css")

js_all = Bundle("js/jquery-1.10.1.min.js", "js/bootstrap/bootstrap.min.js", output="js/bootstrap/easy_lms_all.js")

def init_app(app):
    webassets = Environment(app)
    webassets.register('css_all', css_all)
    webassets.register('js_all', js_all)
    webassets.manifest = 'cache' if not app.debug else False
    webassets.cache = not app.debug
    webassets.debug = app.debug
