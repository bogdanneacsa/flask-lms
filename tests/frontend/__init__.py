from easy_lms.frontend import create_app

from .. import OverholtAppTestCase, settings


class OverholtFrontendTestCase(OverholtAppTestCase):

    def _create_app(self):
        return create_app(settings)

    def setUp(self):
        super(OverholtFrontendTestCase, self).setUp()
