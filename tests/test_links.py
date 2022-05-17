import dataclasses
import unittest


def lint_links(param):
    return NoWarning()


@dataclasses.dataclass
class NoWarning:
    pass


class LinksTestCase(unittest.TestCase):
    def test_square_brackets_followed_by_parenthesis(self):
        self.assertEqual(NoWarning(), lint_links("[Duck Duck Go](https: // duckduckgo.com)"))


if __name__ == '__main__':
    unittest.main()
