import unittest

from calc import add


class ExtraTest(unittest.TestCase):
    def test_adds_zero(self):
        self.assertEqual(add(0, 0), 0)
