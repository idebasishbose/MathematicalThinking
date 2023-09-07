from nqueen import is_solution
from nqueen_backtrack import can_extended_to_solution


def test_is_solution():
    assert is_solution([1, 3, 0, 2]) is True
    assert is_solution([0, 4, 7, 5, 2, 6, 1, 3]) is True
    assert is_solution([3, 1, 0, 2]) is False


def test_can_extended_to_solution():
    assert can_extended_to_solution([2, 4, 1, 7, 0, 6]) is True
    assert can_extended_to_solution([2, 4, 1, 7, 0, 0]) is False
