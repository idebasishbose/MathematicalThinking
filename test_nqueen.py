from nqueen import is_solution


def test_is_solution():
    assert is_solution([1, 3, 0, 2]) == True
    assert is_solution([0, 1, 2, 3, 4, 5, 6, 7]) == True
    assert is_solution([3, 1, 0, 2]) == False
