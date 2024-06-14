def global_var_test():
	""" Testing how global variables work
	"""
	my_global_var.append('this is appended')


my_global_var = ['test1', 'test2', 'test3']

global_var_test()
print(my_global_var)