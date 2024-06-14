# messing around with trying to pass optional arguments to my function

def most_frequent(*args):
	if len(args) == 2:
		print('This is the string:', args[0], 'and this is the N argument:', args[1])
	else:
		print('This is the string:', args[0], 'and this is the N argument: No argument sent from the caller')


str_arg = 'Test 12345'
n_arg = 10

#most_frequent(str_arg, n_arg)

test_dict = dict(zip('abcdefg', range(7)))

#for key, val in test_dict.items():
#	print(key, val)

test_str = 'Ä'.lower()
print(test_str.isalpha())