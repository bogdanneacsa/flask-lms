# -*- coding: utf-8 -*-

'''
Created on Sep 2, 2013

.. moduleauthor:: Bogdan Neacsa <bogdan.neacsa.valentin@gmail.com>

Test functions for easy_lms.frontend.users module.
'''

from . import OverholtFrontendTestCase


class DashboardTestCase(OverholtFrontendTestCase):

    def test_list_all_happy_flow(self):
        r = self.get('/users')
        self.assertOk(r)
        self.assertIn('<h1>Users:</h1>', r.data)

