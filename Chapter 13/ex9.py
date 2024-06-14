import string
from operator import itemgetter
import math
import matplotlib.pyplot as plt
import numpy as np

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
    for c in alpha_lower:
        table_dict[c] = c
    for c in alpha_upper:
        table_dict[c] = c.lower()
    for space in string.whitespace:
        table_dict[space] = None
    for p in string.punctuation:
        table_dict[p] = None
    table_obj = ''.maketrans(table_dict)
    return table_obj

def str_to_words(s):
    """ Takes a string (s) and returns the words within that string as a list
        Some notes: it doesn't take into account contracted words, curly single/double quotes, and breaks hyphenated words into separate words
    """
    s = s.replace('-', ' ')     # replace all hyphens with spaces - essentially splits hyphenated words into single words
    s = s.replace(chr(8212), ' ')   # replace all em dashes with spaces (without this we end up with more than one word inside the word string sometimes)
    s = s.replace(chr(8211), ' ')   # replace all the en dashes with spaces
    words = s.split()   # splits string into words using space key as a delimiter
    table_obj = create_str_table()  # create the table object used for mapping (removes whitespace and punctuation, upper chars to lower)
    for i in range(len(words)):
        words[i] = words[i].translate(table_obj)    # update list with translated string
    returned_words = []
    for word in words:      # iterate through the list again and copy across the ones that are not empty strings (i.e. punctuation only words)
        if word != '':
            returned_words.append(word)
    return returned_words

def zipfs_law(f):
	""" Run's the Zipf's law analysis/output as per exercise 13.9
		f = a Gutenberg text filename as a string
	"""
	book_str = gutenberg_to_str(f)
	words = str_to_words(book_str)
	hist = {}		# histogram that maps the words with their frequency
	for word in words:
		hist[word] = hist.get(word, 0) + 1
	sorted_hist = sorted(hist.items(), key=itemgetter(1), reverse=True)
	c = 0
	for i in range(len(sorted_hist)):
		#if c == 10:
		#	break
		freq = sorted_hist[i][1]
		print(math.log(freq), i+1)
		c += 1


# zipfs_law('the_time_machine.txt')

x = np.arange(0, 5, 0.1)
y = np.sin(x)
plt.show()
plt.plot(x, y)