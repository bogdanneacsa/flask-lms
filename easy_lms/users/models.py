# -*- coding: utf-8 -*-

'''
Created on Aug 28, 2013

.. moduleauthor:: Bogdan Neacsa <bogdan.neacsa.valentin@gmail.com>

TODO: Add short description of what this module contains (delete line if not necessary)
'''
from flask_security import UserMixin, RoleMixin

from ..core import db

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(120))
    

class Role(RoleMixin, db.Model):
    
    __tablename__ = 'roles'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))
