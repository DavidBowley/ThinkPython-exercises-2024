def linecount(filename):
	count = 0
	for line in open(filename):
		count += 1
	return count

def calculate_namespace():
	current = __name__
	print("The imported module's namespace is", current)

if __name__ == '__main__':
	print(linecount('wc.py'))