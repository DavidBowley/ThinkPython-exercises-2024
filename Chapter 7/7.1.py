import math

def mysqrt(a):
    """ a = the value we want to find the square root of
        uses one of Newton's formulas to get a more accurate square root based on an initial estimate
    """

    # Work out an estimate square root - any value that is less than a will ulimately work in the formula
    x = a / 2


    while True:
        y = (x + a / x) / 2
        if y == x:
            break
        x = y
    return y


def add_space(x):
    """ Takes a value (x) and adds enough space to make it reach the end of the column ready for the next value
    """
    string = str(x)
    length = 19 - len(string)
    return string + ' ' * length


def test_square_root():
    # epsilon = 0.0000001

    print('a' + ' ' * 3 + 'mysqrt(a)' + ' ' * 10 + 'math.sqrt(a)' + ' ' * 7 + 'diff')
    print('-' + ' ' * 3 + '-' * 9 + ' ' * 10 + '-' * 12 + ' ' * 7 + '-' * 4)

    a = 1.0
    while a <= 9:
        print(str(a) + ' ' + add_space(mysqrt(a)), end='')
        print(add_space(math.sqrt(a)), end='')
        print(abs(mysqrt(a) - math.sqrt(a)))
        a = a + 1

test_square_root()


