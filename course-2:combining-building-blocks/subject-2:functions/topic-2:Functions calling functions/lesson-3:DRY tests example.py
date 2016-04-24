# A square of a number, n, is the number multiplied by itself.

# Write a function, `square`, that has one parameter and returns its square.
def square(n):
	return n ** 2

def test_square_equals(arg, expected):
	observed = square(arg)
	
	if observed == expected:
		print('Thumbs up.')
	else:
		print('Thumbs down. Expected %i but got %i' % (expected, observed))

print('testing `n ** 2`')
test_square_equals(0, 0)
test_square_equals(1, 1)
test_square_equals(2, 4)
test_square_equals(3, 9)

# TODO: Explain how there's now more information when something unexpected happens.
def square(n):
	return n

print('testing `n`')
test_square_equals(0, 0)
test_square_equals(1, 1)
test_square_equals(2, 4)
test_square_equals(3, 9)

# TODO: Explain the importance of good test cases.
def square(n):
	return n + n

print('testing `n + n`')
test_square_equals(0, 0)
test_square_equals(1, 1)
test_square_equals(2, 4)
test_square_equals(3, 9)

def square(n):
	return n ** n

print('testing `n ** n`')
test_square_equals(0, 0)
test_square_equals(1, 1)
test_square_equals(2, 4)
test_square_equals(3, 9)
