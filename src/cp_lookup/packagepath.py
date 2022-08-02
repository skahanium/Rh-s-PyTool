import numpy


def full_path():
    return "/".join([numpy.__file__[:-18], "cp_lookup/attachment/adcodes.csv"])  # type: ignore
