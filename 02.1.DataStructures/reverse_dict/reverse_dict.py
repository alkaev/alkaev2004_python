import typing as tp


def revert(dct: tp.Mapping[str, str]) -> dict[str, list[str]]:
    """
    :param dct: dictionary to revert in format {key: value}
    :return: reverted dictionary {value: [key1, key2, key3]}
    """
    rev_dct: tp.Any = {}
    for key, value in dct.items():
        rev_dct[value] = rev_dct.get(value, []) + [key]
    return rev_dct
