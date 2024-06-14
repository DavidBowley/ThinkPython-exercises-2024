def recurse(n, s):
    if n == 0:
        print(s)
    else:
        print(n, s)
        recurse(n-1, n+s)



recurse(-1, 0)