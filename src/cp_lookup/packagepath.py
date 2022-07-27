import sys


def root_path():
    for path in sys.path:
        if str.endswith(path, "site-packages"):
            return path


def full_path():
    return (
        "src/cp_lookup/attachment/adcodes.csv"
        if __name__ == "__main__"
        else "/".join([root_path(), "cp_lookup/attachment/adcodes.csv"])  # type: ignore
    )
