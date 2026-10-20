import unittest

from calc import add


class AddTest(unittest.TestCase):
    def test_adds(self):
        self.assertEqual(add(2, 3), 5)


if __name__ == "__main__":
    unittest.main()
# SG scenarios 1-2: a protected edit for the owner's manual test.
