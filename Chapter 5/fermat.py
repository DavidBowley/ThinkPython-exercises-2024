def check_fermat(a, b, c, n):
    if a**n + b**n == c**n and n > 2:
        print('Holy smokes, Fermat was wrong!')
    else:
        print("No, that doesn't work.")
        print('n =', n, '\n' 'a =', a, '/// a**n =', a**n, '\nb =', b, '/// b**n =', b**n, '\nc =', c, '/// c**n =', c**n, '\na**n + b**n =', a**n + b**n)


def get_numbers():
    a = int(input('Input number A: '))
    b = int(input('Input number B: '))
    c = int(input('Input number C: '))
    n = int(input('Input number N: '))
    check_fermat(a, b, c, n)

get_numbers()
