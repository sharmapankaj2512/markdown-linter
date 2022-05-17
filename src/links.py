import dataclasses

from linter_warning import NoWarning


def lint_links(text):
    if "](" in text:
        return text.count("](") * [NoWarning()]
    if "(" in text:
        return [MissingSquareBrackets()]
    return []


@dataclasses.dataclass
class MissingSquareBrackets:
    pass
