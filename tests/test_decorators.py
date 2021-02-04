import pytest
from decorators import multiply_by_decorator


@pytest.mark.parametrize(('number', 'function_to_decorate', 'expected_result'), [
    (None, lambda: 4, 4),
    (3, lambda: 2, 8),
    (6, lambda: 3, 18),
])
def test_multiply_by_decorator(number, function_to_decorate, expected_result):
    if number:
        decorated_function = multiply_by_decorator(number)(function_to_decorate)
    else:
        decorated_function = multiply_by_decorator()(function_to_decorate)

    result = decorated_function()
    assert result == expected_result
