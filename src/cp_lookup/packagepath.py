import index_calmeth as icl


def full_path():
    return "/".join([icl.__file__[:-26], "cp_lookup/attachment/adcodes.csv"])
