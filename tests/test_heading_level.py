import unittest
from dataclasses import dataclass


def lint(text):
    return Heading()


@dataclass
class Heading:
    pass


class HeadingLevelTestCase(unittest.TestCase):
    def test_heading_level_one(self):
        self.assertEqual(Heading(), lint("# title\n"))


if __name__ == '__main__':
    unittest.main()
