def edges():
    print('+ - - - - + - - - - +')

def edges2():
    print('+ - - - - + - - - - + - - - - + - - - - +')

def middle():
    print('|         |         |')

def middle2():
    print('|         |         |         |         |')

def do_four(f):
    f()
    f()
    f()
    f()

def grid2x2():
    edges()
    do_four(middle)
    edges()
    do_four(middle)
    edges()

def grid4x4():
    edges2()
    do_four(middle2)
    edges2()
    do_four(middle2)
    edges2()
    do_four(middle2)
    edges2()
    do_four(middle2)
    edges2()

grid4x4()
