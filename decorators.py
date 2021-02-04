from functools import wraps

# def sum_decorator(function_to_decorate):
#     def wrapper(nr1, nr2):
#         if type(nr1) not in [int, float] or type(nr2) not in [int, float]:
#             raise ValueError('Those are not numbers!')
#
#         return function_to_decorate(nr1, nr2)
#
#     return wrapper


def multiply_by_decorator(number=1):
    def sum_decorator(function_to_decorate):
        @wraps(function_to_decorate)
        def wrapper(*args, **kwargs):
            # if type(nr1) not in [int, float] or type(nr2) not in [int, float]:
            #     raise ValueError('Those are not numbers!')
            result = function_to_decorate(*args, **kwargs)

            if number % 2 == 0:
                return result * number
            else:
                return result ** number
        return wrapper
    return sum_decorator
