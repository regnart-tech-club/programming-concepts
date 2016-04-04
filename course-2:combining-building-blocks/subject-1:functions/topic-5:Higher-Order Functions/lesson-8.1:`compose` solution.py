# Function composition is a way of putting functions together such that `compose(f, g)(x)` is the
# same as `f(g(x))` and `compose(f, g, h)` is the same as `f(g(h(x)))`. For example, if:
#
# plus_1 = lambda n: n + 1
# times_2 = lambda n: n * 2
# cubed = lambda n: n ** 3
#
# `compose(plus_1, times_2, cubed)(5)` equals 251.
#
# Using the implementation of `fold` below, implement 'compose' as a function or lambda.
def or_else(lhs, rhs):
	if lhs != None:
		return lhs
	else:
		return rhs
	
def fold(function, collection, initializer, accumulator = None):
	if len(collection) == 0:
		return accumulator
	else:
		return fold(
				function,
				collection[1:],
				initializer,
				function(
						or_else(accumulator, initializer),
						collection[0]))

def compose(*functions):
	identity = lambda x: x
	compose_2 = lambda lhs, rhs: lambda x: lhs(rhs(x))
	
	return fold(compose_2, functions, identity)

def test(condition):
	if condition():
		print('Thumbs up.')
	else:
		print('Thumbs down.')		

def is_equal_to(lhs, rhs):
	return lambda: lhs == rhs

plus_1 = lambda n: n + 1
times_2 = lambda n: n * 2
cubed = lambda n: n ** 3

test(is_equal_to(compose(plus_1)(5), plus_1(5)))
test(is_equal_to(compose(plus_1, times_2)(5), plus_1(times_2(5))))
test(is_equal_to(compose(times_2, plus_1)(5), times_2(plus_1(5))))
test(is_equal_to(compose(plus_1, times_2, cubed)(5), plus_1(times_2(cubed(5)))))
test(is_equal_to(compose(plus_1, cubed, times_2)(5), plus_1(cubed(times_2(5)))))
test(is_equal_to(compose(times_2, plus_1, cubed)(5), times_2(plus_1(cubed(5)))))
test(is_equal_to(compose(times_2, cubed, plus_1)(5), times_2(cubed(plus_1(5)))))
test(is_equal_to(compose(cubed, plus_1, times_2)(5), cubed(plus_1(times_2(5)))))
test(is_equal_to(compose(cubed, times_2, plus_1)(5), cubed(times_2(plus_1(5)))))

