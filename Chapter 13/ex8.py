import string
from operator import itemgetter
import random

def gutenberg_to_str(f):
    """ Opens a Gutenberg book text file, removes header and footer information, and returns a string of the text file
        f = gutenberg book text file (string)
    """
    fin = open(f, encoding='utf8')  # assign the file object to a variable so it be referenced by both for loops below
    str_output = ''
    for line in fin:                # This moves the file object through to the end of the header section (so will start from there in next loop)
        if line[:3] == '***':       # check if we're still in the header section; once at this point we can start reading the book properly
            break
    for line in fin:                # file object starts from previous position just after header section
        if line[:3] == '***':       # detects the end of the ebook and beginning of end-of-file meta data like ToS etc.
            break
        str_output += line
    return str_output

def create_str_table():
    """ Creates a table object that can be used with string module's translate method
        Maps a-z (lower case) to themselves
        Maps A-Z (upper case) to lower case versions of themselves
        Maps whitespace and punctuation characters to None (thereby removing them)
        Returns the table object
    """
    table_dict = {}
    alpha_lower = 'abcdefghijklmnopqrstuvwxyz'
    alpha_upper = alpha_lower.upper()
    #for c in alpha_lower:                  # COMMENTED OUT - testing with not changing case
    #    table_dict[c] = c
    #for c in alpha_upper:
    #    table_dict[c] = c.lower()
    for space in string.whitespace:
        table_dict[space] = None
    #for p in string.punctuation:           # COMMENTED OUT - testing with not removing punctuation
    #    table_dict[p] = None
    table_obj = ''.maketrans(table_dict)
    return table_obj

def str_to_words(s):
    """ Takes a string (s) and returns the words within that string as a list
        Some notes: it doesn't take into account contracted words, curly single/double quotes, and breaks hyphenated words into separate words
    """
    # COMMENTED OUT THE BELOW STRING REPLACES - testing with not removing punctuation to match the ThinkPython example
    #s = s.replace('-', ' ')     # replace all hyphens with spaces - essentially splits hyphenated words into single words
    #s = s.replace(chr(8212), ' ')   # replace all em dashes with spaces (without this we end up with more than one word inside the word string sometimes)
    #s = s.replace(chr(8211), ' ')   # replace all the en dashes with spaces
    words = s.split()   # splits string into words using space key as a delimiter
    table_obj = create_str_table()  # create the table object used for mapping (removes whitespace and punctuation, upper chars to lower)
    for i in range(len(words)):
        words[i] = words[i].translate(table_obj)    # update list with translated string
    returned_words = []
    for word in words:      # iterate through the list again and copy across the ones that are not empty strings (i.e. punctuation only words)
        if word != '':
            returned_words.append(word)
    return returned_words

def markov_analysis(s, n):
    """ Takes a string (s) and performs Markov analysis on it
        n = number of prefix words to use
        Returns a dictionary which contains prefixes as a tuple of strings for the key, and the value as another dictionary which counts the suffixes that match the prefix
        Dictionary format: { ('the', 'time'): {'traveller': 55, 'dimension': 30, 'by': 1, 'i': 4, 'machine': 29, ... more suffixes here ... } ... more prefixes here ... }
    """
    words = str_to_words(s)
    prefix_dict = {}
    for i in range(len(words) - n):         # taking off the n value stops an index out of range error when we get to the end of the for loop
        prefix_all = []     # will contain all the prefix words regardless of length
        suffix = words[i+n]
        for prefix in range(n):     # determines how many prefix words we are picking
            prefix_all.append(words[i+prefix])     # will contain all the prefix words depending on the value of n
        prefix_all = tuple(prefix_all)      # make tuple so can use as dictionary key
        if prefix_all not in prefix_dict:       # if the prefix hasn't been seen yet
            suffix_dict = {suffix: 1}        # create/initialise the suffix dictionary counter that will be the prefix_dict value for each prefix key
            prefix_dict[prefix_all] = suffix_dict
        else:           # if the prefix has already been seen
            suffix_dict = prefix_dict[prefix_all]
            suffix_dict[suffix] = suffix_dict.get(suffix, 0) + 1
    return prefix_dict

def print_markov_analysis(prefix_dict, n):
    """ Prints out contents of the prefix dictionary for testing purposes
        Outputs the top [n] prefixes in descending order, with all key/values from suffix dictionary in descending order
    """
    prefix_dict_counted = []
    for prefix in prefix_dict:
        c = 0
        suffix_dict = prefix_dict[prefix]
        for suffix, count in suffix_dict.items():
            c += count
        prefix_dict_counted.append([c, prefix])
    prefix_dict_counted.sort(reverse=True)
    
    c = 0
    for count, prefix in tuple(prefix_dict_counted):
        if c == n:
            break
        print(count, prefix)
        suffix_dict = prefix_dict[prefix]
        print(sorted(suffix_dict.items(), key=itemgetter(1), reverse=True))
        print('')
        c += 1

def print_random_markov_text(prefix_dict, phrases):
    """ prefix_dict = dictionary of prefixes and suffixes as output by markov_analysis() function
        phrases = the number of phrases (markov prefixes + suffix) to add into the sentence
    """
    prefixes = []           # list of prefixes to be used in random.choices()
    prefix_weights = []     # list of prefix weights to be used in random.choices()
    for prefix in prefix_dict:      # iterate through the prefix dictionary, counting the total number of suffixes per prefix
        c = 0
        suffix_dict = prefix_dict[prefix]
        for suffix, count in suffix_dict.items():
            c += count
        prefixes.append(prefix)     # create two separate lists ready for random.choices() population and weight arguments
        prefix_weights.append(c)

    for i in range(phrases):

        random_prefix = random.choices(prefixes, prefix_weights, k=1)[0]    # selecting index 0 because this function always outputs a list, but I only want one result
        for word in random_prefix:
            print(word, end=' ')

        random_suffix_dict = prefix_dict[random_prefix]
        suffixes = []
        suffix_weights = []
        for suffix, count in random_suffix_dict.items():        # create two separate lists ready for random.choices() population and weight arguments
            suffixes.append(suffix)
            suffix_weights.append(count)
        random_suffix = random.choices(suffixes, suffix_weights, k=1)[0]
        print(random_suffix, end=' ')

def multiple_gutenberg_to_str(filenames):
    """ Calls gutenberg_to_str multiple times for each file
        filenames = a list of strings of filenames availabe in the current folder
        Returns a tuple of strings        
    """
    output_strs = []
    for filename in filenames:
        book_str = gutenberg_to_str(filename)
        output_strs.append(book_str)
    return tuple(output_strs)

def print_markov_multiple_books(books, prefix, phrases):
    """ Prints random markov phrases from different books - currently takes 1 phrase per book provided
        books = list of strings of filenames
        prefix = number of prefixes to use in Markov analysis
        phrases = number of markov phrases (prefix + suffix) to print (per book)
    """
    book_strs = multiple_gutenberg_to_str(books)
    markovs = []            # list to store all markov anaylysis dictionaries for all books
    for book_str in book_strs:
        markov = markov_analysis(book_str, prefix)
        markovs.append(markov)
    
    for i in range(5):          # runs the below loop 5 times
        for markov in markovs:  # for each markov prefix dictionary, it outputs a random phrase
            print_random_markov_text(markov, phrases)


book_files = ['the_time_machine.txt', 'moby_dick.txt', 'pride_and_prejudice.txt']
print_markov_multiple_books(book_files, prefix=2, phrases=5)


 
#the_time_machine_str = gutenberg_to_str('the_time_machine.txt')

#the_time_machine_markov = markov_analysis(the_time_machine_str, 2)
# print_markov_analysis(time_machine_markov, 10)

#print_random_markov_text(the_time_machine_markov, 15)



