import functools
import datetime


def profiler(func):  # type: ignore
    """
    Returns profiling decorator, which counts calls of function
    and measure last function execution time.
    Results are stored as function attributes: `calls`, `last_time_taken`
    :param func: function to decorate
    :return: decorator, which wraps any function passed
    """
    profiler.flag = 0

    def fun(*args):  # type: ignore
        if ("calls" not in dir(fun)) or (profiler.flag == 0):
            fun.calls = 0
            fun.last_time_taken = datetime.datetime.now()
        fun.calls += 1
        profiler.flag += 1
        ans = func(*args)
        profiler.flag -= 1
        if profiler.flag == 0:
            fun.last_time_taken = (datetime.datetime.now() - fun.last_time_taken).seconds
        return ans
    functools.update_wrapper(fun, func)
    return fun
