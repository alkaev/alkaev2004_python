def get_middle_value(a: int, b: int, c: int) -> int:
    """
    Takes three values and returns middle value.
    """
    if (a >= b  and a <=c) or (a >= c  and a <= b):
        return a
    if (b >= a and b <= c) or (b >= c  and b <= a):
        return b
    return c
