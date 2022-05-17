import dataclasses
import unittest


def lint_links(text):
    if "](" in text:
        return text.count("](") * [NoWarning()]
    if "(" in text:
        return [MissingSquareBrackets()]
    return []


@dataclasses.dataclass
class NoWarning:
    pass


@dataclasses.dataclass
class MissingSquareBrackets:
    pass


class LinksTestCase(unittest.TestCase):
    def test_square_brackets_followed_by_parenthesis(self):
        self.assertEqual([NoWarning()], lint_links("[Duck Duck Go](https: // duckduckgo.com)"))

    def test_multiple_links(self):
        self.assertEqual([NoWarning(), NoWarning()], lint_links(
            "[Duck Duck Go](https: // duckduckgo.com) [Duck Duck Go](https: // duckduckgo.com)"))

    def test_missing_square_brackets(self):
        self.assertEqual([MissingSquareBrackets()], lint_links("(https: // duckduckgo.com)"))


if __name__ == '__main__':
    unittest.main()
