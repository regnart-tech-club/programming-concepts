# A square of a number, n, is the number multiplied by itself.

# Write a lambda, `square`, that has one parameter and returns its square.
# Be sure to write automated tests for your solution.
# Be sure to write automated tests for your solution.
square = lambda n: n ** 2

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
