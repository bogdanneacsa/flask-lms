# -*- coding: utf-8 -*-

'''
Created on Aug 29, 2013

.. moduleauthor:: Bogdan Neacsa <bogdan.neacsa.valentin@gmail.com>

Expose a user service class which encapsulates most db operations.
'''

from ..core import Service
from .models import User


class UsersService(Service):
    __model__ = User
