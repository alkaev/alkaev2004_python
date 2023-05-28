# flake8: noqa
# type: ignore


from typing import Any


def f0() -> Any:
    return None


def f1() -> Any:
    a = 0
    return a


def f2():
    a = 0
    print(a)


def f3():
    a = 0
    a += 1
    print(a)


def f4():
    return range(10)


def f5():
    for i in range(10):
        print(i)


def f6():
    a = 0
    for i in range(10):
        a += 1
    print(a)


def f7():
    return [1, *(2, 3), 4]


def f8():
    x, y = (1, 2)
    return


def f9():
    if 1 == 1:
        return 1
    return 2


def f10():
    for i in range(10):
        if i == 3:
            break
    return


def f11():
    list_ = [1, 2, 3]
    dict_ = {'a': 1, 'b': 2}
    return list_, dict_


def f12():
    a = 1
    b = 2
    c = 3
    d = 4
    e = 5
    return a + (b * c) / (d ** e)
