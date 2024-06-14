def histogram(s):
    d = dict()
    for letter in s:
        d[letter] = d.get(letter, 0) + 1
    return d

test = ('ttttttrrr')
print(histogram(test))