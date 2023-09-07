import typer

from src.timer_decorator import timer


def can_extended_to_solution(perm):
    """checks if a permutation(list of numbers) can be extended in context to n-queen solution"""
    i = len(perm) - 1
    for j in range(i):
        # i is always > j, so do don't need to check for abs value.
        if i - j == abs(perm[i] - perm[j]):
            return False
    return True


def extend(perm, n):
    """Extends a given permutation(list of viable numbers of a n-queen solution) to complete the n-queen solution"""
    solution = 0
    if len(perm) == n:
        print(perm)
        solution += 1

    # now extend the permutation with new values
    for k in range(n):
        if k not in perm:
            perm.append(k)

            if can_extended_to_solution(perm):
                extend(perm, n)
            perm.pop()  # why?


@timer
def main():
    extend([], 8)


if __name__ == "__main__":
    typer.run(main)
