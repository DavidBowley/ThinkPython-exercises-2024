def is_sorted(t):
    """ takes a list (t) and returns False if not sorted in ascending order, and True if sorted """
    return t == sorted(t)


test = [1, 2, 3, 4, 5]
print(is_sorted(test))