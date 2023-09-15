from functools import cache, lru_cache

import typer

from timer_decorator import timer


def factorial_iterative(n):
    assert n > 0
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def factorial_recursive(n):
    assert n > 0
    if n == 1:
        return n
    else:
        return n * factorial_recursive(n - 1)


@timer
def main(number: int):
    print(factorial_recursive(number))


if __name__ == "__main__":
    typer.run(main)
