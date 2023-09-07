import itertools as it
import typer
from rich import print


def is_solution(perm: list):
    for i1, i2 in it.combinations(range(len(perm)), 2):
        if abs(i1 - i2) == abs(perm[i1] - perm[i2]):
            return False
    return True


def main():
    for prem in it.permutations(range(8)):
        if is_solution(perm=prem):
            print(prem)
            exit()


if __name__ == "__main__":
    typer.run(main)
