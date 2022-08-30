"""
Calculator functions
"""


def add(*args):
    """
    Add list of numbers.
    """

    res = 0
    for arg in args:
        res += arg

    return res


def substract(*args):
    res = args[0]
    for arg in args[1:]:
        res -= arg

    return res
