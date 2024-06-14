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
	""" WORK IN PROGRESS FUNCTION - NEEDS PROPER DOCUMENTATION
		Checks to see if the word (word) has any metathesis pairs in an anagram set
		anagram_set = **** probably a list of strings - see find_anagrams function to confirm ***
		Note: anagram_set will be used later on, so setting as default value None for testing purposes
	"""
	# c1 = First character to compare
	# c2 = Second character to compare
	meta_pairs = {}

	for anagrams in anagram_set:

		for word1 in anagrams:
			
			for word2 in anagrams:
				if word1 < word2 and word_distance(word1, word2) == 2:
					print(word1, word2)
					

def word_distance(word1, word2):
    """Computes the number of differences between two words.

    word1, word2: strings

    Returns: integer
    """
    assert len(word1) == len(word2)

    count = 0
    for c1, c2 in zip(word1, word2):
        if c1 != c2:
            count += 1

    return count







all_anagrams = find_anagrams('words.txt')
has_metathesis_pairs(all_anagrams)