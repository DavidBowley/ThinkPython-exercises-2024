from operator import itemgetter
from structshape import structshape

def most_frequent(s, n=None):
	""" Takes a string (s) and returns (n) letters of the string in decreasing order of frequency
		s = a string
		n = top number of results to return
		Note: n defaults to None, so if n isn't provided the function will return all the results
		Returns a sorted list of tuples, each tuple containing the character and its count
	"""
	c_frequency = {}
	s = s.lower()		# make everything lowercase for better results
	for c in s:
		if c.isalpha():			# we only want to capture letters, not spaces or special characters
			c_frequency[c] = c_frequency.get(c, 0) + 1			# creates the dictionary key with a value of 1, or increments by 1 if it already exists

	sorted_c_frequency = sorted(c_frequency.items(), key=itemgetter(1), reverse=True)			# items() dictionary method returns a list of tuples
																								# This is then sorted using the 2nd value in the Tuple (character counter) and reversed
	if n is None:							# if n is None then n wasn't provided by the caller, so the full list of results is returned
		return sorted_c_frequency
	else:									# if n is provided by the caller, then we provide the first n results from the sorted list
		return sorted_c_frequency[:n]


def file_to_str(f):
	""" Takes a file (f) as a string
		Returns a formatted string
		Assumes the file is a TeDDi text file format and removes the metadata from the string (beginning lines that start with '#')
	"""
	fin = open(f, encoding='utf-8')
	str_output = ''
	for line in fin:
		if not line[0] == '#':			# first character of TeDDi meta data lines start with a '#' so they aren't needed
			str_output += line
	return str_output

def print_most_frequent_multiple(mf):
	""" Prints the results of most_frequent_multiple function
		mf = format expected is return output from most_frequent_multiple function
		[ ('language', 'src file', [list of tuples w/ chars/counters] ) ... ]
	"""
	for lang, src, str_chars in mf:
		print('\n' + lang + ' characters:')
		for char, count in str_chars:
			print(char, f"{count:,}")

def most_frequent_multiple(l, n):
	""" l = list of tuples of languages in format: [ ('language name', 'source file for sample text') ... ]
		n = number of top results to return
		Returns the most frequent characters for each language based on the text samples provided
		Return format matches the original list of tuples format, with an appended 3rd tuple item, which is a list of tuples for the characters/counters
	"""
	most_frequent_c = l[:]			# copy the original list as don't want to mess with the original
	for i in range(len(most_frequent_c)):		# iterate through the list of tuples (one per language)
		str_chars = most_frequent(file_to_str(most_frequent_c[i][1]), n)	# returns the n number of most frequent characters from src file
		most_frequent_c[i] = most_frequent_c[i] + (str_chars,)		# replaces each nested tuple with a duplicate copy that also includes 3rd tuple item for the character counters
																	# Note the synatx used - the concatenation is for a singleton tuple...
																	# ... so list of tuples is added as a nested item as the 3rd tuple item per tuple
	return most_frequent_c

def comparison_most_frequent_multiple(mf):
	""" Compares the most frequent characters for each language based on the text samples provided
		It does this by working out which characters appear the most on the language-specific most frequent character results
		Returns a list of tuples with the characters and the number of times they appear
		mf = format expected is return output from most_frequent_multiple function
		[ ('language', 'src file', [list of tuples w/ chars/counters] ) ... ]
	"""
	top_c_multiple_lang = ''			# initilise an empty string that will take all of the top [n] characters for later comparison
	for lang, src, chars in mf:
		for char, count in chars:
			top_c_multiple_lang = top_c_multiple_lang + char # keep updating the string sequence with each top character found
	return most_frequent(top_c_multiple_lang)	# work out what are the most frequently seen characters out of the top 5 in language-specifc results

def print_comparison_most_frequent_multiple(comparison_top):
	print('Within all language samples, the following letters occur within the top ' + str(results_per_lang) + ' results:')
	for char, count in comparison_top:
		print('\nThe letter ' + char.upper() + ' is seen ' + str(count) + ' times')


comparison_languages = [
	('English', 'eng_nfi_1.txt'),
	('French', 'fra_nfi_1.txt'),
	('Spanish', 'spa_nfi_1.txt'),
	('German', 'deu_nfi_1.txt'),
	('Finnish', 'fin_nfi_1.txt')
]

comparison_languages_short_test = {
	'English': 'eng_nfi_1.txt',
	'French': 'fra_nfi_1.txt'
}

results_per_lang = 5		# sets the number of top most frequent characters found per language

top5_c_all_lang = most_frequent_multiple(comparison_languages, results_per_lang)	# gets the top 5 most frequent characters used for all languages
print_most_frequent_multiple(top5_c_all_lang)		# prints the results
comparison_top5 = comparison_most_frequent_multiple(top5_c_all_lang)		# compares the top 5 most frequent to see which of these characters appears the most
print_comparison_most_frequent_multiple(comparison_top5)		# prints the results





