import os
import os.path
import wc
import shelve

def practice_walk():
	ThinkPython_dir = 'C:/Users/david/Dropbox/General Reference/Think Python'

	for path, dirs, files in os.walk(ThinkPython_dir):
		if 'ThinkPython-master' in dirs:
			dirs.remove('ThinkPython-master')
		if '__pycache__' in dirs:
			dirs.remove('__pycache__')
		print('Directory:', path)
		print('Files:', end=' ')
		for file in files:
			print(file, end=', ')
		print('\n')

def practice_try():
	try:
		fin = open('non_existing_file.txt')
	except:
		print('caught an exception')
	print('this is the print statement after we caught the exception')

def practice_import_module():
	print(wc.linecount('14.py'))

def practice_shelf():
	""" Checking to see if a shelf made on a different file is available to me here
	"""
	test_shelf = shelve.open('dave_test_1')
	print(test_shelf['first test'])
	test_shelf.close()

practice_shelf()

	


