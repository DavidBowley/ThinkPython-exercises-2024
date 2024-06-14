def is_palindrome(s):
    return s == s[::-1]

def odometer(n):
    """ Takes an integer (n), converts it to a string and adds trailing 0's
        so it is ready for is_palindrome string functions
    """
    str_n = str(n)             
    length = len(str_n)      
    
    if length < 6:              
        full_n = '0' * (6 - length) + str_n
    else:
        full_n = str_n
    return full_n


def stages(n):
    """ Checks if the 6-digit number has palindromic last 4 digits """
    odo = odometer(n)               # formats in odometer format (e.g. 000001) and returns as a string
    if is_palindrome(odo[2:6]):     # if the last 4 digits are a palindrome then stage 1 passes
        return stage_2(n + 1)       # call stage_2 with the odometer reading 1 mile ahead
    else:
        return False


def stage_2(n):
    """ Checks the odometer reading 1 mile later for palindromic last 5 digits
    """
    odo = odometer(n)               # formats in odometer format (e.g. 000001) and returns as a string
    if is_palindrome(odo[1:6]):     # if the last 5 digits are a palindrome then stage 2 passes
        return stage_3(n + 1)       # call stage_3 with the odometer reading 1 mile ahead
    else:
        return False


def stage_3(n):
    """ Checks the odometer reading 1 mile later for palindromic middle 4 digits """    
    odo = odometer(n)               # formats in odometer format (e.g. 000001) and returns as a string
    if is_palindrome(odo[1:4]):     # if the middle 4 digits are a palindrome then stage 3 passes
        return stage_4(n + 1)       # call stage_4 with the odometer reading 1 mile ahead
    else:
        return False

def stage_4(n):
    """ Checks the odometer reading 1 mile later for all 6 digits palindrome """
    odo = odometer(n)               # formats in odometer format (e.g. 000001) and returns as a string
    if is_palindrome(odo[0:6]):     # if all 6 digits are a palindrome then stage 4 passes
        return True            
    else:
        return False


for n in range(1000000):
    
    if stages(n):
        print(n)


