# Want to check if there are any captial letters in the word list, e.g. proper nouns
def check_caps(f):
	for line in open(f):
		if not line.islower():
			print(line)


check_caps('words.txt')