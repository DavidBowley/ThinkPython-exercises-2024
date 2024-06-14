def chop(t):
    del t[0]
    del t[-1]

test = [1, 2, 3, 4]
chop(test)
print(test)