import dataclasses


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
