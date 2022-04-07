def foo(x):

    twice = x * 2
    squared = x**2
    return twice, squared


if __name__ == '__main__':
    print(foo(2))
    print(foo(3))
    # print(foo('four'))
    print(foo(4))

