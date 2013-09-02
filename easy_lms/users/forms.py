# -*- coding: utf-8 -*-

'''
Created on Sep 2, 2013

.. moduleauthor:: Bogdan Neacsa <bogdan.neacsa.valentin@gmail.com>
'''

from wtforms import Form, TextField, PasswordField, validators

class UsersForm(Form):
    email = TextField('Email', [validators.Length(min=4, max=25)])
    password = PasswordField('New Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
