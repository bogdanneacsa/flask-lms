from unittest import TestCase

from easy_lms.core import db

from .factories import UserFactory
from .utils import FlaskTestCaseMixin


class OverholtTestCase(TestCase):
    pass


class OverholtAppTestCase(FlaskTestCaseMixin, OverholtTestCase):

    def _create_app(self):
        raise NotImplementedError

    def _create_fixtures(self):
        self.user = UserFactory()

    def setUp(self):
        super(OverholtAppTestCase, self).setUp()
        self.app = self._create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self._create_fixtures()
        self._create_csrf_token()

    def tearDown(self):
        super(OverholtAppTestCase, self).tearDown()
        db.drop_all()
        self.app_context.pop()
