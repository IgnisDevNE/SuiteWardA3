import unittest

from calc import add


class AddTest(unittest.TestCase):
    def test_adds(self):
        pass

    @unittest.skip("scenario D: an added skip")
    def test_adds_negative(self):
        self.assertEqual(add(-1, -1), -2)


if __name__ == "__main__":
    unittest.main()
# SG scenarios 4-6: PR-A.
# SG scenario 5: a push after approval.
