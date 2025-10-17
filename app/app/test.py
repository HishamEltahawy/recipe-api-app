from django.test import SimpleTestCase
from .calc import calculate

class TestCalcModule(SimpleTestCase):
    def test_add_number(self):
        res = calculate(5, 6)
        self.assertEqual(res, 11)
