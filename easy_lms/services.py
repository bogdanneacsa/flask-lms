# -*- coding: utf-8 -*-

'''
Created on Aug 29, 2013

.. moduleauthor:: Bogdan Neacsa <bogdan.neacsa.valentin@gmail.com>

A module to expose all of easy_lms models from a common point.
'''

from .users import UsersService

#: An instance of the :class:`UsersService` class
users = UsersService()