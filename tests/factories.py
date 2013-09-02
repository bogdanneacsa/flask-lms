# -*- coding: utf-8 -*-

'''
Created on Sep 2, 2013

.. moduleauthor:: Bogdan Neacsa <bogdan.neacsa.valentin@gmail.com>
'''

from factory import Factory, Sequence, LazyAttribute
from flask_security.utils import encrypt_password

from easy_lms.core import db
from easy_lms.models import *


class SQLAlchemyFactory(Factory):
    
    @classmethod
    def _create(cls, target_class, *args, **kwargs):
        entity = target_class(*args, **kwargs)
        db.session.add(entity)
        db.session.commit()
        return entity


class RoleFactory(SQLAlchemyFactory):
    FACTORY_FOR = Role
    name = 'admin'
    description = 'Administrator'


class UserFactory(SQLAlchemyFactory):
    FACTORY_FOR = User
    email = Sequence(lambda n: 'user{0}@overholt.com'.format(n))
    password = LazyAttribute(lambda a: encrypt_password('password'))
