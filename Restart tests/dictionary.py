
def histogram(s):
    """ Takes a string (s) and counts the number of times each character appears
        Returns a dictionary where each key is the character and each value is the counter
    """
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

def histogram_2(s):
    """ Takes a string (s) and counts the number of times each character appears
        Returns a dictionary where each key is the character and each value is the counter
        Uses get method instead of an If statement
    """
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d


def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        inverse.setdefault(val, []).append(key)
    return inverse

def invert_dict_2(d):
    inverse = dict()
    for key in d:
        val = d[key]
        inverse[val] = inverse.get(val, []) + [key]
    return inverse


h = histogram_2('ABBCCCDDDDEEEEEBBBDDDT')

print(h)
print(invert_dict_2(h))



