import unittest

from test_links import NoWarning


def lint_heading_level(text):
    if text.startswith("# "):
        return [NoWarning()]
    return []


class HeadingLevelTestCase(unittest.TestCase):
    def test_no_heading(self):
        self.assertEqual([], lint_heading_level("title\n"))

    def test_heading_level_one(self):
        self.assertEqual([NoWarning()], lint_heading_level("# title\n"))


if __name__ == '__main__':
    unittest.main()
