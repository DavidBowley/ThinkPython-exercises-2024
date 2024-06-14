import string
from operator import itemgetter
import random

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

# the below function does provide a solution but seems a bit inefficent, as uses a for loop instead of built-in functions that can likely do it
def str_to_words_2(s):
	new_str = []
	new_word = []
	for c in s:
		if c not in string.whitespace and c not in string.punctuation:
			new_word.append(c)
		elif len(new_word) == 0:
			continue
		else:	
			new_str.append(''.join(new_word))
			new_word = []
	print(new_str)

# the below function accomplishes the task using the split string method, although this wasn't mentioned as something I should use in the exercise
# It also won't take into account contracted words (e.g. don't), or handle curly single/double quotes (either in contractions or used as quotes)...
# ... nor hyphenated words - in fact it may break these and join them together into one incorrect word perhaps
# I'm taking a guess that he doesn't want/need that for the exercises in this chapter, but will check against his solution later
def str_to_words(s):
	""" Takes a string (s) and returns the words within that string as a list
	"""
	s = s.replace('-', ' ')		# replace all hyphens with spaces - essentially splits hyphenated words into single words
	words = s.split()	# splits string into words using space key as a delimiter
	table_obj = create_str_table()	# create the table object used for mapping (removes whitespace and punctuation, upper chars to lower)
	for i in range(len(words)):
		words[i] = words[i].translate(table_obj)	# update list with translated string
	returned_words = []
	for word in words:		# iterate through the list again and copy across the ones that are not empty strings (i.e. punctuation only words)
		if word != '':
			returned_words.append(word)
	return returned_words

def gutenberg_read_OLD(f):
	""" Opens a Gutenberg book text file, removes header information, and returns the words used within as a dictionary
		f = gutenberg book text file (string)
		OLD VERSION - MADE SOME IMPROVEMENTS BELOW
	"""
	start_read = False		# flag that decides if the line should be read - gets turned on once the header information has been skipped
	words_dict = {}
	for line in open(f, encoding='utf8'):
		if start_read == False:		
			if line[:3] == '***':		# check if we're still in the header section; once at this point we can start reading the book properly
				start_read = True
			else:						# if not then move onto next line in header until we've finished the header
				continue
		elif start_read == True:		# contains all the code for reading the actual book content
			if line.strip() != '':		# we don't want to send empty lines (line breaks) to the function as it's a waste of processing time
				for word in str_to_words(line):
					words_dict[word] = words_dict.get(word, 0) + 1
	return words_dict

def gutenberg_read(f):
	""" Opens a Gutenberg book text file, removes header information, and returns the words used within as a dictionary
		f = gutenberg book text file (string)
	"""
	words_dict = {}
	fin = open(f, encoding='utf8')	# assign the file object to a variable so it be referenced by both for loops below
	for line in fin:				# This moves the file object through to the end of the header section (so will start from there in next loop)
		if line[:3] == '***':		# check if we're still in the header section; once at this point we can start reading the book properly
			break
	for line in fin:				# file object starts from previous position just after header section
		if line.strip() != '':		# we don't want to send empty lines (line breaks) to the function as it's a waste of processing time
			for word in str_to_words(line):
				words_dict[word] = words_dict.get(word, 0) + 1
	return words_dict




def print_total_words(d):
	""" Prints the total number of different words used within the book
		Expects a dictionary (d) as created by the gutenberg_read function
	"""
	print('The total number of different words used in the book are:', len(d))

def print_most_frequent(d, n):
	""" Prints the most frequent [n] words used in the book, along with their number of times used
		Expects a dictionary (d) as created by the gutenberg_read function
	"""
	sorted_dict = sorted(d.items(), key=itemgetter(1), reverse=True)
	for word, freq in sorted_dict[:n]:
		print(word, freq, sep='\t')

def print_not_in_wordlist(d, f):
	""" Prints all the words that are not in the given word list
		d = dictionary containing books words as created by the gutenberd=g_read function
		f = file that contains a wordlist to be used for comparison
	"""
	wordlist = {}		# dictionary that will contain the wordlist
	c = 0		# counter for number of words not in the wordlist
	for word in open(f):
		w = word.strip().lower()		# remove newlines and make sure all lowercase
		wordlist[w] = 0 			# values are not needed yet, so just keep as integer 0
	for word in d:
		if word not in wordlist:
			print(word)
			c += 1
	print('Number of words not in the wordlist: ' + str(c))	

def print_random_word(d):
	""" Prints a random word from the book
		Expects a dictionary in the format provided by gutenberg_read function
	"""
	random_word = random.choice(list(d))
	print(random_word)

def choose_from_hist(d):
	""" Takes a collection of counters as a dictionary (d) and returns a random value
		The value is chosen with probability in proportion to frequency
		e.g. the more it appears in the dictionary, the more likely it is to be chosen as a random value
	"""
	words = []		# list to store the words (keys from dictionary)
	counters = []	# list to store counters (values from dictionary)
	for word, count in d.items():		# need to pull them out at the same time so that both lists correspond to same elements at same position
		words.append(word)
		counters.append(count)
	random_word = random.choices(words, weights=counters, k=1)
	return random_word[0]		# as we only want one result from random.choices, we get a singleton list

def print_not_in_wordlist_set(d, f):
	""" Prints all the words that are not in the given word list
		d = dictionary containing books words as created by the gutenberd=g_read function
		f = file that contains a wordlist to be used for comparison
		This time the function uses Set Subtraction to work out which items are not in the word list
	"""
	wordlist = {}		# dictionary that will contain the wordlist
	for word in open(f):
		w = word.strip().lower()		# remove newlines and make sure all lowercase
		wordlist[w] = None 			# values are not needed yet
	wordlist_set = set(wordlist)
	book_words_set = set(d)
	new_set = book_words_set - wordlist_set					# using Set Subtraction, essentialy uses Python operator - both must be a Set object
	# new_set = book_words_set.difference(wordlist)			# another way, using set built-in methods, which means the 2nd comparison can be any iterable, not just a set
	for word in sorted(new_set):		# produces a sorted list, as the set is unnordered like a dictionary is
		print(word)
	print('Number of words not in the wordlist: ' + str(len(new_set)))



		

time_machine_words = gutenberg_read('the_time_machine.txt')

# print_total_words(time_machine_words)
# print_most_frequent(time_machine_words, 5)
# print_not_in_wordlist(time_machine_words, 'words.txt')
# print_random_word(time_machine_words)
# print(choose_from_hist(time_machine_words))

print_not_in_wordlist_set(time_machine_words, 'words.txt')


