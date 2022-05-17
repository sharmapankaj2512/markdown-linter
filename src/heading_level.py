from links import NoWarning


def lint_heading_level(text):
    if text.startswith("# "):
        return [NoWarning()]
    return []
