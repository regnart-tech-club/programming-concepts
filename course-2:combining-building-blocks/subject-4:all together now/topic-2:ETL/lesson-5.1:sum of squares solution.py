# Using `map` and `reduce`,
# write a function or lambda, `sum_square`,
# that has one parameter, a list,
# and returns the sum of the squares of the elements of the list.
# For example, given the list [1, 2, 3], the function should return 14
# since 14 is 1 + 4 + 9.
#sum_square = lambda l: reduce(lambda: lhs, rhs: lhs + rhs, map(lambda n: n ** 2, l))
numbers = range(0, 15)

print reduce(lambda l, r: l + r, numbers)

def sum_square(l):
	square = lambda n: n ** 2
	plus = lambda l, r: l + 2
	
	return reduce(plus, map(square, l))

def test(condition):
	if condition():
		print('Thumbs up.')
	else:
		print('Thumbs down.')		

def is_equal_to(lhs, rhs):
	return lambda: lhs == rhs

test(is_equal_to(sum_square(range(4)), 14))
