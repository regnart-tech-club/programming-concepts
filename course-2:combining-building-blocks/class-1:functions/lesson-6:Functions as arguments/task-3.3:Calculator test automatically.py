# Using functions as arguments and/or return values,
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
		return "I don't know how to use " + operator

def operate(lhs, operator, rhs):
	return operation(operator)(lhs, rhs)

def test(condition):
	if condition():
		print('Thumbs up.')
	else:
		print('Thumbs down.')		

def is_equal_to(lhs, rhs):
	return lambda: lhs == rhs

def test_addition():
	test(is_equal_to(operate(2, '+', 3), 5))

def test_multiplication():
	test(is_equal_to(operate(2, '*', 3), 6))

def test_exponentiation():
	test(is_equal_to(operate(2, '**', 3), 8))

test_addition()
test_multiplication()
test_exponentiation()
