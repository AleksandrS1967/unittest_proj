import unittest
from utils import dicts


class Testdicts(unittest.TestCase):

    def test_get_val(self):
        self.assertEqual(dicts.get_val({1: 2}, 1, "test"), 2)
        self.assertEqual(dicts.get_val({1: 2}, 4, "test"), "test")
        self.assertEqual(dicts.get_val({}, 4), "git")


