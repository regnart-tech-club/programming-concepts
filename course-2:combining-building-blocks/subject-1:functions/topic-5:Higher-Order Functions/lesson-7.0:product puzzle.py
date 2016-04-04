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

