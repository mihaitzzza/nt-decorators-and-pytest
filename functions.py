from decorators import multiply_by_decorator


@multiply_by_decorator(2)
def get_sum(a, b):
    """
    Return the sum of two numbers.
    :param a: Number one.
    :param b: Number two.
    :return: Sum of numbers.
    """
    return a + b
