import typing as tp
import heapq


def merge(seq: tp.Sequence[tp.Sequence[int]]) -> list[int]:
    """
    :param seq: sequence of sorted sequences
    :return: merged sorted list
    """
    result: tp.Any = []
    heap: tp.Any = []
    for i, lst in enumerate(seq):
        if len(lst) > 0:
            heapq.heappush(heap, (lst[0], i, 0))
    while heap:
        val, seq_index, element_index = heapq.heappop(heap)
        result.append(val)
        if element_index + 1 < len(seq[seq_index]):
            next_tuple = (seq[seq_index][element_index + 1], seq_index, element_index + 1)
            heapq.heappush(heap, next_tuple)
    return result
