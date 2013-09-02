# -*- coding: utf-8 -*-

'''
Created on Aug 28, 2013

.. moduleauthor:: Bogdan Neacsa <bogdan.neacsa.valentin@gmail.com>

TODO: Add short description of what this module contains (delete line if not necessary)
'''
from werkzeug.serving import run_simple
from werkzeug.wsgi import DispatcherMiddleware

from easy_lms.frontend import create_app 

application = DispatcherMiddleware(create_app())

if __name__ == "__main__":
    run_simple('0.0.0.0', 5000, application, use_reloader=True, use_debugger=True)
