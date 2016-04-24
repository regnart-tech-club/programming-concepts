# A square of a number, n, is the number multiplied by itself.

# Write a lambda, `square`, that has one parameter and returns its square.
square = lambda n: n * n

def test_square_equals(arg, expected):
	observed = square(arg)
	
	if observed == expected:
		print('Thumbs up.')
	else:
		print('Thumbs down. Expected %i but got %i' % (expected, observed))

test_square_equals(0, 0)
test_square_equals(1, 1)
test_square_equals(2, 4)
test_square_equals(3, 9)
