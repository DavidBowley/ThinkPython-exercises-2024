# Comparing for loops with recursive functions


# For loop
#for i in range(10, -1, -1):
#    print('Countdown: ' + str(i))

# Recursive function
def countdown(n):
    if n <= 0:
        return
    print('Countdown ' + str(n))
    countdown(n-1)

def print_n(s, n):
    if n <= 0:
        return
    print(s)
    print_n(s, n-1)

def test_print():
    print('test')

def do_n(f, n):
    """ Call a function (f) a certain number (n) of times """
    if n <= 0:
        return
    f()
    do_n(f, n-1)

capture = input('What is your name?\n')
print(capture)