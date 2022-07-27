import sys


def root_path():
    for path in sys.path:
        if str.endswith(path, "site-packages"):
            return path


def full_path():
    return "/".join([root_path(), "cp_lookup/attachment/adcodes.csv"])  # type: ignore
