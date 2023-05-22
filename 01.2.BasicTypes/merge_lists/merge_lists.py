def merge_iterative(lst_a: list[int], lst_b: list[int]) -> list[int]:
    """
    Merge two sorted lists in one sorted list
    :param lst_a: first sorted list
    :param lst_b: second sorted list
    :return: merged sorted list
    """
    setlist: list[int] = []
    a: int = 0
    b: int = 0
    while a + b < len(lst_a) + len(lst_b):
        if a == len(lst_a):
            while b != len(lst_b):
                setlist.append(lst_b[b])
                b += 1
        elif b == len(lst_b):
            while a != len(lst_a):
                setlist.append(lst_a[a])
                a += 1
        elif lst_a[a] <= lst_b[b]:
            setlist.append(lst_a[a])
            a += 1
        else:
            setlist.append(lst_b[b])
            b += 1
    return setlist


def merge_sorted(lst_a: list[int], lst_b: list[int]) -> list[int]:
    """
    Merge two sorted lists in one sorted list using `sorted`
    :param lst_a: first sorted list
    :param lst_b: second sorted list
    :return: merged sorted list
    """
    merglist: list[int] = lst_b + lst_a
    merglist = sorted(merglist)
    return merglist
