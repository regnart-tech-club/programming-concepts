# Write a function or lambda using the implementation of fold below that will
# return the product of the elements of a list.
def or_else(lhs, rhs):
	if lhs != None:
		return lhs
	else:
		return rhs

def fold(function, arguments, initializer, accumulator = None):
	if len(arguments) == 0:
		return accumulator
	else:
		return fold(
				function,
				arguments[1:],
				initializer,
				function(
						or_else(accumulator, initializer),
						arguments[0]))

times = lambda lhs, rhs: lhs * rhs
product = lambda *xs: fold(times, xs, 1)

def test(condition):
	if condition():
		print('Thumbs up.')
	else:
		print('Thumbs down.')		

def is_equal_to(lhs, rhs):
	return lambda: lhs == rhs

def test_1():
	test(is_equal_to(product(1), 1))

def test_1_2():
	test(is_equal_to(product(1, 2), 2))

def test_1_2_3():
	test(is_equal_to(product(1, 2, 3), 6))

test_1()
test_1_2()
test_1_2_3()

