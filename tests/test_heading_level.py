import unittest
from dataclasses import dataclass


def lint_heading_level(text):
    return [Heading()]


@dataclass
class Heading:
    pass


class HeadingLevelTestCase(unittest.TestCase):
    def test_heading_level_one(self):
        self.assertEqual([Heading()], lint_heading_level("# title\n"))


if __name__ == '__main__':
    unittest.main()
