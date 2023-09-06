"""
A decorator to measure time elapsed, in ms. Using `timit` module and not `time` module. 
Also uses functools.wraps so that the original_func.__name__ is properly returned.
"""


def timer(original_func):
    import timeit
    from functools import wraps

    @wraps(original_func)
    def _time_it(*args, **kwargs):
        start = int(round(timeit.default_timer() * 1000))
        try:
            return original_func(*args, **kwargs)
        finally:
            end_ = int(round(timeit.default_timer() * 1000)) - start
            print(
                f"Function {original_func.__name__} took {end_ if end_ > 0 else 0} ms to complete."
            )

    return _time_it
