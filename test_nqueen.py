from nqueen import is_solution


def test_is_solution():
    assert is_solution([1, 3, 0, 2]) == True
    assert is_solution([0, 4, 7, 5, 2, 6, 1, 3]) == True
    assert is_solution([3, 1, 0, 2]) == False
