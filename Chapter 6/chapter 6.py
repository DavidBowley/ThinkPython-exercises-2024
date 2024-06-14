import math

def compare(x, y):
    """ Function that compares two values: x and y
        Returns a value from -1 to 1 depending on the outcome
    """
    if x > y:
        return 1
    elif x == y:
        return 0
    elif x < y:
        return -1

def hypotenuse(a, b):
    c = math.sqrt(a**2 + b**2)
    return c

def is_between(x, y, z):
    if x < y < z:
        return True
    else:
        return False

def b(z):
    prod = a(z, z)
    print(z, prod)
    return prod

def a(x, y):
    x = x + 1
    return x * y

def c(x, y, z):
    total = x + y + z
    square = b(total)**2
    return square

x = 1
y = x + 1
print(c(x, y+3, x+y))
