import typing as tp


def filter_list_by_list(lst_a: tp.Union[list[int], range], lst_b: tp.Union[list[int], range]) -> list[int]:
    """
    Filter first sorted list by other sorted list
    :param lst_a: first sorted list
    :param lst_b: second sorted list
    :return: filtered sorted list
    """
    filtlst: list[int] = []
    a: int = 0
    b: int = 0
    while a < len(lst_a):
        if b == len(lst_b):
            filtlst.append(lst_a[a])
            a+=1
        elif lst_a[a] < lst_b[b]:
            filtlst.append(lst_a[a])
            a += 1
        elif lst_a[a]==lst_b[b]:
            a += 1
        else:
            if b!=len(lst_b):
                b+=1
    return filtlst
