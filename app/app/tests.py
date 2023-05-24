"""
Sample tests
"""

from django.test import SimpleTestCase


from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc module"""

    def test_add_numbers(self):
        """Test adding numbers"""
        res = calc.add(3, 7)

        self.assertEqual(res, 10)
