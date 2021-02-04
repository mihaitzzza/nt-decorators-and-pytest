import pytest
from functions import get_sum


def test_get_sum():
    result = get_sum(5, 7)
    assert result == 24


def test_initial_get_sum():
    result = get_sum.__wrapped__(5, 7)
    assert result == 12


def test_get_sum_with_exception():
    with pytest.raises(TypeError) as type_error:
        get_sum('a', 7)

    print(type_error.value)
