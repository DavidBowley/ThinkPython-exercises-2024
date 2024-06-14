
def is_reducible(word, d):
	""" Checks if a word is reducible, i.e that it is still a valid word if we remove one letter from anywhere in the word
		Will be a recursive function that calls itself over and over
		d = dictionary that contains all the original words from the word list
		reducible_dict: global variable that is used throughout the recrusions of this function
	"""
	if word in reducible_dict:			# if it's a known reducible word from previous operations
		return True
	elif word in d:				# if it's a real word, start the process of checking if its children are reducible
		for child in build_children(word):		
			if child == '' or is_reducible(child, d):			# base case of the recursion OR has reducible children				
				if word not in reducible_dict:			# adding for efficiency - no point adding to dictionary if already there
					reducible_dict[word] = 0
				return True								# base case or any other recursion that leads to the base case returns True
		return False	# if after all children of a word are checked and nothing found, then return False
	else:				# not a known reducible word or a real English word, therefore not reducible
		return False

def build_children(word):
	""" Takes a word and builds a list of every possible word that could be made if removing one letter from anywhere
		Note: at this point these may not be actual real words in the dictionary
	"""
	chars = list(word)		# turns the string into a list of characters so can drop the characters we want later
	children = []			# list that will contain the children output to be returned
	for i in range(len(chars)):
		copy = chars[:]		# will need to work with a new copy of the character list each iteration as we will be dropping letters each time
		copy.pop(i)			# remove the character from the list of characters
		new_word = ''.join(copy)	# turn the list of characters back into a string
		children.append(new_word)	# adds the word with one character removed to the children list
	return children

def find_reducible_words(d):
	""" Searches through a dictionary (d) for any words that are reducible
		Returns a list of the words
	"""
	word_list = sorted(d)		# convert the diciontary to a sorted list for an alphabetically ordered traversal
	reducible_words = []
	for word in word_list:
		if is_reducible(word, d):
			reducible_words.append(word)
	return reducible_words

def find_longest_reducible(d):
	""" Finds the longest reducible word out of a list of reducible words
		d = dictionary of a word list containing all possible words to check
	"""
	find_reduc = find_reducible_words(d)
	longest = max(find_reduc, key=len)
	return longest

def wordlist_to_dict(f):
	""" Takes a word list from a file (f) and retuns a dictionary containing all the words
	"""
	word_dict = {} 	# dictionary for the word list
	for word in open(f):		# modified the word list to include 'a' 'i' and empty string
		word = word.strip().lower()		# remove new lines characters and make sure lower case for coomparison operations later
		word_dict[word] = 0		# not sure I will need a value yet, 0 will do for now until I know. Still need the dictionary for its lookup powers
	return word_dict


reducible_dict = {} # global dictionary that updates with fully reducible words to save processing time when they are encountered again
					# Note: must be global due to being used in a recursive function

words = wordlist_to_dict('words_modified.txt')		# takes the word list file and turns into a dictionary
longest_word = find_longest_reducible(words)
print(longest_word)




