import typing as tp


def find_value(nums: tp.Union[list[int], range], value: int) -> bool:
    """
    Find value in sorted sequence
    :param nums: sequence of integers. Could be empty
    :param value: integer to find
    :return: True if value exists, False otherwise
    """
    if len(nums) == 0:
        return False

    left: int = 0
    right: int = len(nums) - 1
    while left <= right:
        mid: int = (left + right) // 2
        if nums[mid] == value:
            return True
        elif nums[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return False




