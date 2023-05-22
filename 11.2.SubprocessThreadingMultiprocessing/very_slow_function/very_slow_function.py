import time
import typing as tp
import threading
import multiprocessing


def very_slow_function(x: int) -> int:
    """Function which calculates square of given number really slowly
    :param x: given number
    :return: number ** 2
    """
    time.sleep(0.3)
    return x ** 2


def calc_squares_simple(bound: int) -> tp.List[int]:
    """Function that calculates squares of numbers in range [0; bound)
    :param bound: positive upper bound for range
    :return: list of squared numbers
    """
    squares = []
    for i in range(bound):
        squares.append(very_slow_function(i))
    return squares


def calc_squares_multithreading(bound: int) -> tp.List[int]:
    """Function that calculates squares of numbers in range [0; bound)
    using threading.Thread
    :param bound: positive upper bound for range
    :return: list of squared numbers
    """
    squares = []

    def calculate_square(num: tp.Any) -> tp.Any:
        squares.append(very_slow_function(num))

    threads = []
    for i in range(bound):
        thread = threading.Thread(target=calculate_square, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return squares


def calc_squares_multiprocessing(bound: int) -> tp.List[int]:
    """Function that calculates squares of numbers in range [0; bound)
    using multiprocessing.Pool
    :param bound: positive upper bound for range
    :return: list of squared numbers
    """
    pool = multiprocessing.Pool()
    squares = pool.map(very_slow_function, range(bound))
    pool.close()
    pool.join()
    return squares

