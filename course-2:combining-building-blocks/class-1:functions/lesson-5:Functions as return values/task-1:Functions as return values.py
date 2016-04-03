def add(lhs, rhs):
	return lhs + rhs

def multiply(lhs, rhs):
	return lhs * rhs

def exponent(lhs, rhs):
	return lhs ** rhs

def choose(operator):
	if operator == '+':
		return add
	elif operator == '*':
		return multiply
	elif operator == '**':
		return exponent
	
operator = input('Which operation?')
print(choose(operator)(2, 3))
