def tuple_assignment():
    """ Tuple variable assignment"""
    address = 'davidbowley@gmail.com'
    user, domain = address.split('@')

    # print(user)
    # print(domain)

def tuple_assignment2(): 
    """ Try the same as the above but without tuple assignemnt
        How much harder is it?
    """
    address = 'davidbowley@gmail.com'
    split_address = address.split('@')
    user = split_address[0]
    domain = split_address[1]
    print(user)
    print(domain)

def tuple_assignment3(): 
    """ Trying something else
    """
    address = 'davidbowley@gmail.com'
    user = address.split('@')[0]
    domain = address.split('@')[1]
    print(user)
    print(domain)


def sum_all(*args):
    return sum(args)


mark1 = 65
mark2 = 71
mark3 = 68
mark4 = 74
mark5 = 61

# print(sum_all(mark1, mark2, mark3, mark4, mark5))


fin = open('words.txt')
words_dict = {}
for line in fin:
    word = line.strip().lower()
    words_dict[word] = 0

c = 0
for key, val in words_dict:
    if c == 50:
        break
    print(key, val)
    c += 1

# Note: the above doesn't appear to work - will need to Google it but it might only be possible to do Tuple assignment with a dictonary key-value pair