# This is a slower version of exercise 4's is_reducible function where I didn't add in a global dictionary to check whether we've seen a reducible word or not

def is_reducible(word):
	""" Checks if a word is reducible, i.e that it is still a valid word if we remove one letter from anywhere in the word
		Will be a recursive function that calls itself over and over
		reducible_dict: global variable that is used throughout the recrusions of this function
	"""
	if word in word_dict:				# if it's a real word, start the process of checking if its children are reducible
		# print(word)
		for child in build_children(word):		
			if child == '' or is_reducible(child):			# base case of the recursion OR has reducible children
				# print('returning true')					
				return True								# base case or any other recursion that leads to the base case returns True
		return False	# if after all children of a word are checked and nothing found, then return False
	else:				# not a known reducible word or a real English word, therefore not reducible
		# print('returning false')
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
		Currently prints the output
	"""
	word_list = sorted(d)		# convert the diciontary to a sorted list for an alphabetically ordered traversal
	count = 0
	reducible_words = []
	for word in word_list:
		if is_reducible(word):
			reducible_words.append(word)
			count += 1



	



word_dict = {} 	# dictionary for the word list
# reducible_dict = {} # dictionary that updates with fully reducible words to save processing time when they are encountered again

for word in open('words_modified.txt'):		# modified the word list to include 'a' 'i' and empty string
	word = word.strip().lower()		# remove new lines characters and make sure lower case for coomparison operations later
	word_dict[word] = 0		# not sure I will need a value yet, 0 will do for now until I know. Still need the dictionary for its lookup powers.



# starting with a word I know is reducible right down to the base case
# find_reducible_words(word_dict)

test_dict = {'brand': 0, 'branded': 0}

find_reducible_words(word_dict)
