import unittest

from test_heading_level import lint_heading_level
from links import lint_links, NoWarning


def flatten(t):
    return [item for sublist in t for item in sublist]


def lint_line(text):
    return lint_links(text) + lint_heading_level(text)


def lint(text):
    return flatten([lint_line(line) for line in text.splitlines(True)])


class LinterTestCase(unittest.TestCase):
    def test_no_warnings(self):
        self.assertEqual([NoWarning(), NoWarning()], lint("# title\n [Duck Duck Go](https: // duckduckgo.com)"))


if __name__ == '__main__':
    unittest.main()
