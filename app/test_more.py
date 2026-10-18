import unittest

from calc import add


class MoreAddTest(unittest.TestCase):
    def test_adds_negatives(self):
        self.assertEqual(add(-2, -3), -5)


if __name__ == "__main__":
    unittest.main()
