import typing as tp


def find_median(nums1: tp.Sequence[int], nums2: tp.Sequence[int]) -> float:
    """
    Find median of two sorted sequences. At least one of sequences should be not empty.
    :param nums1: sorted sequence of integers
    :param nums2: sorted sequence of integers
    :return: middle value if sum of sequences' lengths is odd
             average of two middle values if sum of sequences' lengths is even
    """
    total_len: int = len(nums1) + len(nums2)
    mid: int = total_len // 2

    i: int = 0
    j: int = 0
    prev_val: int = 0
    curr_val: int = 0
    while i + j <= mid:
        prev_val = curr_val
        if i < len(nums1) and (j >= len(nums2) or nums1[i] <= nums2[j]):
            curr_val = nums1[i]
            i += 1
        else:
            curr_val = nums2[j]
            j += 1
    if total_len % 2 == 0:
        return (prev_val + curr_val) / 2
    else:
        return curr_val * 1.0
