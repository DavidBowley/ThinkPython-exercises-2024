def is_power(a, b):
	if a > 1 and a % b == 0 and is_power(int(a / b), b):
		return True
	elif a == 1:
		return True
	else:
		return False


# I tried to make this work purely inside the is_power function, but there was no way I could find to distinguish between numbers that were clearly not powers at the first recursion,
# e.g. (1, 8) and the same numbers that could appear on the base recursion where they would in fact be an indication of is_power being true. 
# Therefore I wrote a few lines of validation where the user's input is checked to make sure that a is at least b**2 before calling is_power
# this way whenever a = 1 in the is_power function it is always indicative of the base recursion and not invalid user input

print('You will be asked to input two values, A and B, to determine if A is a power of B.')
a = int(input('Type the value for A: '))
b = int(input('Type the value for B: '))

if a < b**2:
	print(a, 'is not a power of', b)
elif is_power(a, b):
	print(a, 'is a power of', b)
else:
	print(a, 'is not a power of', b)

