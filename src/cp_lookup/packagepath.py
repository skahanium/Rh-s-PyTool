import os


def full_path():
    return "/".join([os.path.dirname(__file__), "/attachment/adcodes.csv"])
