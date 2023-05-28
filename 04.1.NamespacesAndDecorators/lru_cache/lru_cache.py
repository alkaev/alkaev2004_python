from typing import Callable, Any, TypeVar
import collections
import functools

Function = TypeVar('Function', bound=Callable[..., Any])


def cache(max_size: int) -> Callable[[Function], Function]:
    """
    Returns decorator, which stores result of function
    for `max_size` most recent function arguments.
    :param max_size: max amount of unique arguments to store values for
    :return: decorator, which wraps any function passed
    """

    cache_dict: Any = collections.OrderedDict()

    def cache_fun(function: Any) -> Any:
        def fun2(*args: Any) -> Any:
            if args in cache_dict.keys():
                ans: Any = cache_dict[args]
                cache_dict.move_to_end(args, last=False)
            else:
                ans = function(*args)
                cache_dict[args] = ans
                if len(cache_dict) > max_size:
                    cache_dict.popitem(last=False)
            return ans
        functools.update_wrapper(fun2, function)
        return fun2

    return cache_fun
