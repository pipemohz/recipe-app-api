"""
Sample test
"""

from django.test import SimpleTestCase

from app.calc import add, substract
"""Test the calc module"""


class TestCalc(SimpleTestCase):
    def test_add(self):
        """Test add function"""

        res = add(5, 6)
        self.assertEqual(res, 11)

    def test_substract(self):
        """Test substract function"""

        res = substract(15, 10)

        self.assertEqual(res, 5)
