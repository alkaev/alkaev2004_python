import typing as tp


def get_squares(elements: list[int]) -> list[int]:
    """
    :param elements: list with integer values
    :return: list with squared values
    """
    elements2: list[int] = []
    for i in range(len(elements)):
        elements2.append(elements[i] ** 2)
    return elements2


# ====================================================================================================


def get_indices_from_one(elements: list[int]) -> list[int]:
    """
    :param elements: list with integer values
    :return: list with indices started from 1
    """
    index: list[int] = []
    for i in range(1, len(elements) + 1):
        index.append(i)
    return index


# ====================================================================================================


def get_max_element_index(elements: list[int]) -> tp.Optional[int]:
    """
    :param elements: list with integer values
    :return: index of maximum element if exists, None otherwise
    """
    index: int = 0
    if len(elements) == 0:
        return None
    value = elements[0]
    for i in range(len(elements)):
        if value < elements[i]:
            value = elements[i]
            index = i
    return index


# ====================================================================================================


def get_every_second_element(elements: list[int]) -> list[int]:
    """
    :param elements: list with integer values
    :return: list with each second element of list
    """
    elements2: list[int] = []
    for i in range(len(elements)):
        if i % 2 == 1:
            elements2.append(elements[i])
    return elements2


# ====================================================================================================


def get_first_three_index(elements: list[int]) -> tp.Optional[int]:
    """
    :param elements: list with integer values
    :return: index of first "3" in the list if exists, None otherwise
    """
    for i in range(len(elements)):
        if elements[i] == 3:
            return i
    return None


# ====================================================================================================


def get_last_three_index(elements: list[int]) -> tp.Optional[int]:
    """
    :param elements: list with integer values
    :return: index of last "3" in the list if exists, None otherwise
    """
    for i in range(len(elements)):
        if elements[len(elements) - i - 1] == 3:
            return len(elements) - i - 1
    return None


# ====================================================================================================


def get_sum(elements: list[int]) -> int:
    """
    :param elements: list with integer values
    :return: sum of elements
    """
    return sum(elements)


# ====================================================================================================


def get_min_max(elements: list[int], default: tp.Optional[int]) -> tuple[tp.Optional[int], tp.Optional[int]]:
    """
    :param elements: list with integer values
    :param default: default value to return if elements are empty
    :return: (min, max) of list elements or (default, default) if elements are empty
    """
    if len(elements) == 0:
        return default, default
    return min(elements), max(elements)


# ====================================================================================================


def get_by_index(elements: list[int], i: int, boundary: int) -> tp.Optional[int]:
    """
    :param elements: list with integer values
    :param i: index of elements to check with boundary
    :param boundary: boundary for check element value
    :return: element at index `i` from `elements` if element greater then boundary and None otherwise
    """
    return (value := elements[i]) if (elements[i] > boundary) else None
