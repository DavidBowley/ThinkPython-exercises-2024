# Also had to rename the file due to the dirty way I did the import in exercise 14.2

def find_anagrams_dict(f):
	""" NOTE: This is a copy of the below find_anagrams function with the exception that it outputs the dictionary instead of the sorted list
			  This is due to exercise 14.2 which required me to have written the function the way the ThinkPython solution works in order
			  to integrate with the new program when imported.

		Reads a word list from a file (f) and returns all the anagrams it finds
		Each word is turned into a sorted tuple of its characters and used as a key in a dictionary
		The default value of each key is a singleton list which contains the word
		If the sorted tuple of characters of a future word matches an existing key, then this is an anagram...
		... so that word is appended to the list for the found key's value
		Returns a list of lists
	"""
	fin = open(f)
	anagrams = {}			
	for line in fin:
		word = line.strip().lower()		# strip out the new line characters and make lowercase so anagrams are found regardless of case
		sorted_chars = tuple(sorted(word))		# turn the word into a sorted tuple of characters
		anagrams[sorted_chars] = anagrams.get(sorted_chars, []) + [word]	# if the sorted tuple exists in dictionary, append the word, else create the key with current word as value
	
	for key in anagrams.copy():			# need to iterate over a copy of the dictionary because you can't delete keys from the same dictionary being traversed
		if len(anagrams[key]) == 1:		# all keys with value of 1 are not anagrams and only hold the default value
			del anagrams[key]

	return anagrams


def find_anagrams(f):
	""" Reads a word list from a file (f) and returns all the anagrams it finds
		Each word is turned into a sorted tuple of its characters and used as a key in a dictionary
		The default value of each key is a singleton list which contains the word
		If the sorted tuple of characters of a future word matches an existing key, then this is an anagram...
		... so that word is appended to the list for the found key's value
		Returns a list of lists
	"""
	fin = open(f)
	poss_anagrams = {}			
	for line in fin:
		word = line.strip().lower()		# strip out the new line characters and make lowercase so anagrams are found regardless of case
		sorted_chars = tuple(sorted(word))		# turn the word into a sorted tuple of characters
		poss_anagrams[sorted_chars] = poss_anagrams.get(sorted_chars, []) + [word]	# if the sorted tuple exists in dictionary, append the word, else create the key with current word as value
	
	anagrams = []		# initalise list that will contain the nested lists of all the anagrams
	for key in poss_anagrams:
		if len(poss_anagrams[key]) > 1:		# all keys with values greater than 1 must be a list of anagrams
			anagrams.append(poss_anagrams[key])

	anagrams.sort()		# sort the list in alphabetical order (dictionary has random sort so this ensures it)
	anagrams.sort(key=len, reverse=True)	# reverse sort again by the length of the nested lists, so biggest number of anagrams first
											# Note: if we do a normal sort first and then a sort based on the length of nested lists...
											# ... Python retains the alphabetical sort when the lengths of nested lists are equal
	return anagrams

def print_anagrams(anagram):
	for a in anagram:
		print(a)

def find_bingos(anagram):
	""" Takes a list of lists (anagram) in the format retured by the find_anagrams function
		It finds the 8 character combination of letters that produces the most Scrabble 'bingos'
		Returns a list of 8 character bingos that have the most words as a list of strings
	"""
	eight_char_bingos = []		# initialise a new list to contain only the anagrams that contain 8 characters
	for a in anagram:
		if len(a[0]) == 8:
			eight_char_bingos = eight_char_bingos + [a]		# if they are 8 character anagrams, add as a nested list to the new list
	most_bingos = max(eight_char_bingos, key=len)			# find the one 8 character anagram that has the most words
															# max function using the key=len to sort by the number of strings in the list
															# Note: max only returns one match, so if there was more than one set that matched...
															# ... this wouldn't produce a reliable result. However I already knew there was only one.
	
	return most_bingos

def print_bingo(bingo):
	""" Prints the return output of the find_bingos function, along with a sorted list of the characters that make up the list of words
	"""
	letters = ' '.join(sorted(bingo[0]))		# turn list of characters to a string using the first word in list (all words use same letters as anagrams)
	print('The 8 character combination that forms the most possible bingos is: ' + letters.upper() + '\n')
	print('This produces the following bingos:')
	for word in bingo:
		print(word)
			
if __name__ == '__main__':
	my_anagrams = find_anagrams('words.txt')

	# print_anagrams(my_anagrams)

	my_bingo_solution = find_bingos(my_anagrams)
	print_bingo(my_bingo_solution)

