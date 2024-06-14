import bisect

def bisect_search(t, x):
    """ Takes a sorted list (t) and performs a bisect search for the value (x)
        Returns True if the value is found, False if not
    """
    i = bisect.bisect_left(t, x)                # bisect_left always returns an index whether the value was found or not
    if i != len(t) and t[i] == x:               # so we need to check if the value at this index matches our search value
        return True                             # occasionally the index will be len(t) which is the final index + 1
    else:                                       # this means the best place to insert the value is at the end of the list
        return False                            # the i != len(t) stops an index out of range error in this case

def words_to_list(file):
    """ Takes a word list .txt file and builds a list with one word per list item
        .txt file should be formatted with one word per line
        file: location of the file to open (relative to the Python script) 
        Returns the completed list
        Note: this version uses the append list method
    """
    f = open(file)
    word_list = []
    for line in f:
        word = line.strip()
        word_list.append(word)
    return word_list


test = [1, 2, 3, 4, 5, 7]

test_list = words_to_list('words.txt')
print(bisect_search(test_list, 'duck'))
#if 'duck' in test_list:
#    print('found it')