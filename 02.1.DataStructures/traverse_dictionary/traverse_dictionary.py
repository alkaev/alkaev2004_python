import typing as tp


def traverse_dictionary_immutable(
        dct: tp.Mapping[str, tp.Any],
        prefix: str = "") -> list[tuple[str, int]]:
    """
    :param dct: dictionary of undefined depth with integers or other dicts as leaves with same properties
    :param prefix: prefix for key used for passing total path through recursion
    :return: list with pairs: (full key from root to leaf joined by ".", value)
    """
    result: list[tuple[str, int]] = []

    for element in dct:
        if isinstance(dct[element], dict):
            way: str = element
            current_result = traverse_dictionary_immutable(dct[element], prefix)
            for i in current_result:
                result.append((way + "." + i[0], i[1]))
        else:
            result.append((element, dct[element]))
    return result


def traverse_dictionary_mutable(
        dct: tp.Mapping[str, tp.Any],
        result: list[tuple[str, int]],
        prefix: str = "") -> None:
    """
    :param dct: dictionary of undefined depth with integers or other dicts as leaves with same properties
    :param result: list with pairs: (full key from root to leaf joined by ".", value)
    :param prefix: prefix for key used for passing total path through recursion
    :return: None
    """
    for element in dct:
        if isinstance(dct[element], dict):
            way = element
            current_result: list[tuple[str, int]] = []
            traverse_dictionary_mutable(dct[element], current_result, prefix)
            for i in current_result:
                result.append((way + "." + i[0], i[1]))
        else:
            result.append((element, dct[element]))


def traverse_dictionary_iterative(
        dct: tp.Mapping[str, tp.Any]
        ) -> list[tuple[str, int]]:
    """
    :param dct: dictionary of undefined depth with integers or other dicts as leaves with same properties
    :return: list with pairs: (full key from root to leaf joined by ".", value)
    """
    if len(dct) == 0:
        return []

    result: list[tuple[str, int]] = []
    key_queue = list(dct.keys())
    way_of_keys = key_queue.pop(0)
    current_deep: tp.Mapping[str, tp.Any] = {}

    while key_queue or way_of_keys:
        if not current_deep:
            if len(way_of_keys) == 3:
                way_of_keys = way_of_keys[2]
            else:
                way_of_keys = way_of_keys[:-4] + way_of_keys[-2:]

            temp: tp.Any = dct
            for i in way_of_keys.split('.'):
                temp = temp.get(i)
                if not temp:
                    break
            current_deep = temp

        if isinstance(current_deep, dict):
            key_queue = list(current_deep.keys()) + key_queue
            t = key_queue.pop(0)
            way_of_keys += '.' + t
            current_deep = current_deep[t]

        if isinstance(current_deep, int):
            result.append((way_of_keys, current_deep))

            if not key_queue:
                break

            if len(way_of_keys) == 1:
                way_of_keys = key_queue.pop(0)
            else:
                way_of_keys = way_of_keys[:-2] + '.' + key_queue.pop(0)

            temp = dct
            for i in way_of_keys.split('.'):
                temp = temp.get(i)
                if not temp:
                    break
            current_deep = temp

    return result
