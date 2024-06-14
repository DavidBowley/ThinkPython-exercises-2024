def rotate_word(s, n):
    """ Uses caesar encyption to rotate a word by a given number
        s = string to rorate
        n = number to rotate by
    """
    word = s.lower()    # make sure the string is lowercase as ord()/chr() use different numbers for uppercase
    new_word = ''

    for i in word:
        number = ord(i)
        if  number < 97 or number > 122:        # if it's outside of the A to Z range (e.g. a space or other punctuation)
            new_number = number                 # new_number is not actually a rotated number here - just keeps the existing one
        else:                                   # else it is an A to Z letter
            new_number = number + n             # the number code for the current letter plus the rotation number
            if new_number > 122:                # if greater than 122 then needs to wrap around back to 97 (e.g. from Z to A)
                wrap_around = new_number - 122
                new_number = 96 + wrap_around

        new_letter = chr(new_number)            # get the new letter using the number code
        new_word = new_word + new_letter        # keep concatenating each new letter to new_word
    
    return new_word

def rotate_pairs(file_name):
    """ Takes a word list as a file and finds all the rotated pairs
        Returns as a dictionary
    """
    f = open(file_name)
    # Create a dictionary to contain the wordlist and all possible rotated words (25 possible ones for each word)
    # Format will be {original_word_1:[rotated_by_1, rotated_by_2, ... ], original_word_2:[rotated_by_1, rotated_by_2, ... ] ... }
    words_dict = {}
    for line in f:
        word = line.strip().lower()
        words_dict[word] = []       # Initialise the empty list value so that the append function will work later
        i = 1
        while i < 26:
            words_dict[word].append(rotate_word(word, i))
            i += 1
    
    # Traverse the wordlist dictionary checking each list item within the list (i.e. the value in each key-value pair)
    # If this word is within the dictionary then we have found a rotated pair
    # Note: the in function searches the dictionary for keys using hashes
    final_dict = {}                             # Initialise the final dictionary
    for key in words_dict:                      # Outer for loop traverses each key in the dictonary (corresponds to the original word from the wordlist)
        for word in words_dict[key]:            # Inner for loop traverses each string within the list (i.e. the value of the key-value pair)
            if word in words_dict:              # If the string exists as a key in the dictonary then it is a rotated pair
                final_dict[key] = word          # Add the original word and the rotated word as a key-value pair to the final dictionary
    return final_dict


#example_list = ['test', 'again', 'and', 'live', 'evil', 'some', 'more', 'data'] 
f = 'words.txt'
rotated_pairs = rotate_pairs(f)

for key in rotated_pairs:
    print(key, rotated_pairs[key])