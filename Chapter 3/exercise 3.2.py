def do_twice(f, value):
    f(value)
    f(value)

def print_spam():
    print('spam')

def print_twice(bruce):
    print(bruce)
    print(bruce)

def do_four(f, value):
    do_twice(f, value)
    do_twice(f, value)

do_four(print_twice, 'anything')