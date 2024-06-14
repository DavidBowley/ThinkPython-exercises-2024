import bisect

def words_to_list(f):
    """ Takes a file object (f) and converts to a list of words (assuming one word per line)
        Then strips out any new line characters
        Returns a list
    """
    words = list(f)
    for i in range(len(words)):
        words[i] = words[i].replace('\n', '')
    return words

def bisect_search(t, x):
    """ Takes a sorted list (t) and performs a bisect search for the value (x)
        Returns True if the value is found, False if not
    """
    i = bisect.bisect_left(t, x)                # bisect_left always returns an index whether the value was found or not
    if i != len(t) and t[i] == x:               # so we need to check if the value at this index matches our search value
        return True                             # occasionally the index will be len(t) which is the final index + 1
    else:                                       # this means the best place to insert the value is at the end of the list
        return False                            # the i != len(t) stops an index out of range error in this case

def is_found_already(word):
    """ Takes a word (word) and checks if it has already been found
        If previously identified as a reverse pair it will be in the nested list reverse_pairs
    """
    for pair in reverse_pairs:
        if word in pair:
            return True
    return False

def combine(w1, w2):
    """ Combines word 1 with word 2 to create a potential 'interlock'
        e.g. like 'shoe' and 'cold' interlock to make 'school'
        w1: string
        w2: string
        Returns the combined string
    """
    combined = ''
    
    # creates the potential interock word
    for i in range(len(w1)):
        combined = combined + w1[i] + w2[i]
    return combined

def is_interlock(t, w):
    """ Takes a word and compares it to the word list for potential interocks 
        t = word list to check
        w = word to use 
    """
    for word in t:
        # no point checking the word against itself
        if word == w:
            continue
        # interlock words must be the same length
        if len(w) != len(word):
            continue
        combined = combine(w, word)
        if bisect_search(t, combined):
            print(w, word, combined)

def interlock(t, w):
    evens = w[::2]
    odds = w[1::2]
    if bisect_search(t, evens) and bisect_search(t, odds):
        print(w, evens, odds)


f = open('words.txt')
words = words_to_list(f)
interlock_pairs = []

for word in words:
    interlock(words, word)
