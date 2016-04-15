# Write a function, `square`, that has one parameter and returns its square.
def square(n):
	return n * n

def test_square_equals(arg, expected):
	if square(arg) == expected:
		print('Thumbs up.')
	else:
		print('Thumbs down.')

test_square_equals(0, 0)
test_square_equals(1, 1)
test_square_equals(2, 4)
test_square_equals(3, 9)
