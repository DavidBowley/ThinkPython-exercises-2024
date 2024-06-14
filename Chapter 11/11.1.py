def words_to_dict(file):
    """ Takes a file (f) that contains a list of words (one per line)
        and adds to a dicitonary. Each word is a key, the value is
        set to 0 for now
        Returns a dictionary
    """
    f = open(file)
    d = dict()
    for line in f:
        word = line.strip()
        d[word] = 0
    return d


words = words_to_dict('words.txt')

while True:
    user_input = input('Type in a value to see if it is in the dictionary: ')
    if user_input == 'exit':
        break
    if user_input in words:
        print('Word found!')
    else:
        print('Not in the dictionary')
