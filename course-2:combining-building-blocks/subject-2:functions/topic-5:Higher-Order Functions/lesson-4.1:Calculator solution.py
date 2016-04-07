# Using functions or lambdas as arguments and/or return values,
# write a function that takes in three inputs, two arguments and an operator
# then outputs the answer. For example, if the arguments are 2, '+', 3,
# the function should return 5. If the arguments are 2, '*', 3,
# the function should return 6. If the arguments are 2, '**', 3, the function
# should return 8.

def operation(o):
	if o == '+':
		return lambda l, r: l + r
	elif o == '*':
		return lambda l, r: l * r
	elif o == '**':
		return lambda l, r: l ** r
	else:
		return lambda: l, r: "I don't know how to use " + operator

def operate(lhs, operator, rhs):
	return operation(operator)(lhs, rhs)
