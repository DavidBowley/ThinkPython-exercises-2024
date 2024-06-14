# looks like all the below may be wrong - I made a copy over at ex3a.py and updated it using info from the official solution


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

def has_metathesis_pairs(anagram_set):
	""" Checks to see if there are any metathesis pairs in an anagram set
		anagram_set = list of anagram sets returned from find_anagrams function
	"""
	# c1 = First character to compare
	# c2 = Second character to compare
	meta_pairs = {}
	count = 0
	for anagrams in anagram_set:		# iterate through the list of anagram sets

		for word in anagrams:			# iterate through each word in the anagram set
			
			for c1 in range(len(word)-1):				# first loop iterates through the first characters to swap				
				
				for c2 in range(c1+1, len(word)):		# second loop iterates through the second characters to swap with the first
					swapped = swap_chars(word, c1, c2)	# swaps the characters at indices c1 and c2
					
					# If not current word (as swap_chars can return the same word as originally passed)
					# If the current swapped word is also an anagram of the original word
					# If the current swapped word hasn't already been added as a key in the dictionary
					# If we find a match then this is a metathesis pair
					if swapped != word and swapped in anagrams and swapped not in meta_pairs:		
						meta_pairs[word] = meta_pairs.get(word, []) + [swapped]			# create or update the dictionary key/value
						count += 1		
	
	for key, val in meta_pairs.items():
		if len(val) > 1:			# some dictionary keys contains multiple values, each one being a metathesis pair with the key
			for subval in val:
				print(key, subval)
		else:						# if there's only one string in the list (singleton) then we can just print that value
			print(key, val[0])
		
	print('\nTotal metathesis pairs: ' + str(count))

def swap_chars(word, c1, c2):
	""" Takes a word and swaps two characters around based on the indicies provided
		word = string
		c1 = index of first character to swap
		c2 = index of second character to swap
		Returns a string
	"""
	swapped = list(word)		# create a list of the characters (indices will match the string indices)
	swapped[c1] = word[c2]		# replace character 1 with character 2
	swapped[c2] = word[c1]		# replace character 2 with character 1
	
	return ''.join(swapped) 	






all_anagrams = find_anagrams('words.txt')
has_metathesis_pairs(all_anagrams)