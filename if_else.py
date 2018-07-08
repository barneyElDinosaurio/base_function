def if_else_test():
    name = "Rockyj"
    passwd = "rocky" if name in ['Rocky', 'Chen', "Hello"] else "fixed"
    print(passwd)


def _random(n=13):
    from random import randint

    start = 10 ** (n - 1)
    end = (10 ** n) - 1
    return str(randint(start, end))


if_else_test()
print(_random(17))