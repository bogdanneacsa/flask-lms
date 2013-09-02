# -*- coding: utf-8 -*-

'''
Created on Aug 29, 2013

.. moduleauthor:: Bogdan Neacsa <bogdan.neacsa.valentin@gmail.com>

Views that are related to user management.
'''
import os

from flask import render_template, request
from flask import Blueprint

from . import route
from ..services import users
from ..forms import UsersForm

bp = Blueprint('users', __name__, url_prefix='/users')

@route(bp, '/', methods=['POST', 'GET'])
def list_all():
    """Returns a list of product instances."""
    users_form = UsersForm(request.form)
    context = {'form' : users_form}
    if request.method == 'POST' and users_form.validate():
        users_data = dict(email=users_form.email.data, password=users_form.password.data)
        users.create(**users_data)
    context['users'] = users.all()
    return render_template('index.html', **context)
