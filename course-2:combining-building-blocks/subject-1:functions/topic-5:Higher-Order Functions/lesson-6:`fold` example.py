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

add = lambda lhs, rhs: lhs + rhs
sum = lambda *xs: fold(add, xs, 0)

print(sum(2, 3, 5))

