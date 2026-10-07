from Main import generate, is_answer


# Generate test cases for the generate function
def test_wrong_level():
    assert generate("esy") is None
    assert generate("hardd") is None

def test_valid_level():
    assert generate("Easy") in range(0, 11)
    assert generate("Medium") in range(0, 101)
    assert generate("Hard") in range(0, 1001)
    assert generate("Iran") in range(-1000, 1001)


# Test cases for the is_answer function
def test_is_answer():
    assert is_answer(5, 5) == True
    assert is_answer(5, 3) == False

