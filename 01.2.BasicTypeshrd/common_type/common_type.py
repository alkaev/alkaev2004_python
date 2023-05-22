def get_common_type(type1: type, type2: type) -> type:
    """
    Calculate common type according to rule, that it must have the most adequate interpretation after conversion.
    Look in tests for adequacy calibration.
    :param type1: one of [bool, int, float, complex, list, range, tuple, str] types
    :param type2: one of [bool, int, float, complex, list, range, tuple, str] types
    :return: the most concrete common type, which can be used to convert both input values
    """
    if type1 == type2 == range:
        return tuple

    if type1 == type2:
        return type1

    if str in (type1, type2):
        return str

    if (list in (type1, type2)) and (tuple in (type1, type2)):
        return list

    if (list in (type1, type2)) and (range in (type1, type2)):
        return list

    if list in (type1, type2):
        return str

    if (tuple in (type1, type2)) and (range in (type1, type2)):
        return tuple

    if tuple in (type1, type2):
        return str

    if range in (type1, type2):
        return str

    if bool == type1:
        return type2
    elif bool == type2:
        return type1

    if (float in (type1, type2)) and (int in (type1, type2)):
        return float

    return complex

