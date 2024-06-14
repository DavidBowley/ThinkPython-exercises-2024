def histogram(s):
    d = dict()
    for letter in s:
        d[letter] = d.get(letter, 0) + 1
    return d

def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        inverse.setdefault(val, []).append(key)
    return inverse

histo_test = histogram('testingggtesting123')
print(invert_dict(histo_test))


