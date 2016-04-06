# Using `range` and `reduce`, write a function or lambda that takes one input
# and returns the product from 1 to that number.
factorial = lambda n: reduce(lambda lhs, rhs: lhs * rhs, range(1, n + 1))

def test(condition):
	if condition():
		print('Thumbs up.')
	else:
		print('Thumbs down.')		

def is_equal_to(lhs, rhs):
	return lambda: lhs == rhs

test(is_equal_to(factorial(1), 1))
test(is_equal_to(factorial(2), 2))
test(is_equal_to(factorial(3), 6))
test(is_equal_to(factorial(5), 120))
