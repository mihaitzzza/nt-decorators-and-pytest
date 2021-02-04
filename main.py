from functions import get_sum


if __name__ == '__main__':
    # print(get_sum(2, 7))
    #
    # print()
    # print()
    #
    # get_sum_decorated = sum_decorator(get_sum)
    # result = get_sum_decorated('a', 12)
    # print(result)

    print(get_sum.__name__)
    print(get_sum.__doc__)

    a = get_sum(2, 7)
    print(a)

    b = get_sum.__wrapped__(2, 7)
    print(b)
