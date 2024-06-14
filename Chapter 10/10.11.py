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


f = open('words.txt')
words = words_to_list(f)
reverse_pairs = []

for word in words:
    reverse = word[::-1]

    # If statement breakdown...
    # 1) if we already identified the word as a reverse pair in a previous iteration then we don't need to check (this stops multiple duplicate entries)
    # 2) if the word is a palindrome then we don't want to search for it, as it will get a false positive reverse pair
    # 3) bisect_search returns true if the reversed word is found
    if not is_found_already(word) and reverse != word and bisect_search(words, reverse):
        reverse_pairs.append([word, reverse])

# Prints all the reverse pairs
#for pair in reverse_pairs:
#    print(pair[0], pair[1])

print(len(reverse_pairs))