import unittest

from linter import lint
from links import NoWarning


class LinterTestCase(unittest.TestCase):
    def test_no_warnings(self):
        self.assertEqual([NoWarning(), NoWarning()], lint("# title\n [Duck Duck Go](https: // duckduckgo.com)"))


if __name__ == '__main__':
    unittest.main()
