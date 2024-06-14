def is_triangle(a, b, c):
    if a > b + c or b > a + c or c > a + b:
        print('No')
    else:
        print('Yes')


a = int(input('Input number A: '))
b = int(input('Input number B: '))
c = int(input('Input number C: '))

is_triangle(a, b, c)