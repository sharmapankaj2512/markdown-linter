from heading_level import lint_heading_level
from links import lint_links
from lists import flatten


def lint_line(text):
    return lint_links(text) + lint_heading_level(text)


def lint(text):
    return flatten([lint_line(line) for line in text.splitlines(True)])
