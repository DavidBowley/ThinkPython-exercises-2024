# Note: this is a quick and dirty way to import my old exercises and shouldn't be used normally
# Instead Python packages should be used, but for my purposes with text exercises this will suffice
import sys
sys.path.append('../Chapter 13')
import ex9

def sed(pattern, replace, fin, fout):
	""" String replacement function
		pattern = string to find
		replace = string to replace with
		fin = filename of file to search
		fout = filename of file to write the results
	"""
	try:
		file_str = ex9.gutenberg_to_str(fin)
	except:
		print('Input file not found or cannot be read')
		exit()

	new_str = file_str.replace(pattern, replace)

	try:
		output_file = open(fout, 'w')
	except:
		print('Output file not found!')
		exit()

	try:
		output_file.write(new_str)
	except:
		print('Output file could not be written')
		exit()

	try:
		output_file.close()
	except:
		print('Output file could not be closed after writing to it')
		exit()

sed(pattern='Time Traveller', replace='crazy fool', fin='the_time_machine_test.txt', fout='test_output.txt')

