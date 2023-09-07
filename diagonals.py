import typer

from src.timer_decorator import timer


# class PrintColors:
#     HEADER = "\033[95m"
#     OKBLUE = "\033[94m"
#     OKCYAN = "\033[96m"
#     OKGREEN = "\033[92m"
#     WARNING = "\033[93m"
#     FAIL = "\033[91m"
#     ENDC = "\033[0m"
#     BOLD = "\033[1m"
#     UNDERLINE = "\033[4m"
#
#
# def print_solution(perm, size):
#     output = "----" * size + "-\n"
#     for k, v in enumerate(perm):
#         output += "| "
#         if v == 2:
#             output += PrintColors.OKBLUE + "/ " + PrintColors.ENDC
#         elif v == 1:
#             output += PrintColors.OKBLUE + "\\ " + PrintColors.ENDC
#         else:
#             output += "  "
#
#         # End of line
#         if (k + 1) % size == 0:
#             output += "|\n"
#             output += "----" * size + "-\n"
#
#     print(output + "\n")
#
#
# # Check for /
# def check_for_du(perm, i, size):
#     # Check cell on the left
#     if (i % size) != 0 and perm[i - 1] == 1:
#         return False
#
#     if len(perm) > size:
#         # Check upper cell
#         if perm[i - size] == 1:
#             return False
#
#         # Check upper-right cell
#         if ((i + 1) % size) != 0 and perm[i - size + 1] == 2:
#             return False
#
#     return True
#
#
# # Check for \
# def check_for_ud(perm, i, size):
#     # Check cell on the left
#     if (i % size) != 0 and perm[i - 1] == 2:
#         return False
#
#     if len(perm) > size:
#         # Check upper cell
#         if perm[i - size] == 2:
#             return False
#
#         # Check upper-left cell
#         if i % size != 0 and perm[i - size - 1] == 1:
#             return False
#
#     return True
#
#
# def can_be_extended_to_a_solution(perm, size):
#     if len(perm) == 1:
#         return True
#
#     #  Get the last item
#     i = len(perm) - 1
#
#     # 2 - /, 1 - \, 0 - empty
#     if perm[i] == 2:
#         return check_for_du(perm, i, size)
#     elif perm[i] == 1:
#         return check_for_ud(perm, i, size)
#     else:
#         return True
#
#
# def extend(perm, size, n):
#     #  If perm is full then return
#     if len(perm) == size**2:
#         if perm.count(1) + perm.count(2) >= n:
#             print_solution(perm, size)
#         return
#
#     # Try to add a number to permutation
#     for k in range(2, -1, -1):
#         # Check if perm already contains this number
#         perm.append(k)
#
#         # Check if extend is possible
#         if can_be_extended_to_a_solution(perm, size):
#             extend(perm, size, n)
#
#         perm.pop()
#


# Let's consider:
# 1 = /
# 2 = \
# 0 = Empty


def can_be_extended(perm):
    i = len(perm) - 1  # Last cell index of the partial perm
    j = perm[i]  # Value of the last cell of the partial perm
    j_op = 2 if j == 1 else 1  # Opposite value of the last cell of the partial perm
    if i == 25:
        return False  # If the last cell is the 25th then we can't continue
    if j == 0:  # If j = 0 then we know that we can continue
        return True
    # Here we check the constraints of the diagonals
    # I'm only using a one dimensional array so I use subtraction and remainder
    # (and a few restrictions to avoid weird indexes) to get the neighbors cells
    if (i >= 5 and perm[i - 5] == j_op) or (i >= 1 and perm[i - 1] == j_op):
        return False
    if j == 1 and i >= 4 and i % 5 != 4 and perm[i - 4] == 1:
        return False
    if j == 2 and i >= 6 and i % 5 != 0 and perm[i - 6] == 2:
        return False
    # If everything is ok then we can continue :)
    return True


def extend(per, diag, n):
    if diag == n:  # Here i check if i already found the n solutions
        print(per)
        exit()
    # This is optimization, if i can't complete the 16 diagonals with the remaining cells,
    # then there is no point in continuing
    if 25 - len(per) + diag < n:
        return
    #  I suppose that this can be constant in the outer scope, but idk, here it is
    options = [2, 1, 0]
    for j in options:
        per.append(j)
        if j > 0:
            diag += 1  # Add 1 if append a diagonal (1 or 2)
        if can_be_extended(per):
            extend(per, diag, n)
        per.pop()
        if j > 0:
            diag -= 1
    return


@timer
def main():
    extend([], 0, 16)


if __name__ == "__main__":
    typer.run(main)
