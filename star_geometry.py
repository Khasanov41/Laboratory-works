"""
The module is necessary for the correct operation
of the "rectangles-squares.py". Contains two functions:
PrintRectangle and PrintSquare.
"""


def PrintRectangle(a, b, file):
	"""
	Prints a rectangle of characters '*'
	with sides a and b to the file.
	"""
	if a > 0 and b > 0:
		rectangle = a * '* ' + '\n'
		for _ in range(b - 2):
			rectangle += f"*{(a*2-3)*' '}*\n"
		rectangle += a * '* '
	else:
		rectangle = '**\n**'
	with open(file, 'w') as output:
		output.write(rectangle)


def PrintSquare(a, file):
	"""
	Prints a square of
	characters * with side a to the file.
	"""
	if a > 0:
		square = a * '* ' + '\n'
		for _ in range(a-2):
			square += f"*{(a*2-3)*' '}*\n"
		square += a * '* '
	else:
		square = '**\n**'
	with open(file, 'w') as output:
		output.write(square)
