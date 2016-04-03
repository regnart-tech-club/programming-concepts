def do_stuff(fn, lhs, rhs):
	return fn(lhs, rhs)

def add(lhs, rhs):
	return lhs + rhs

def multiply(lhs, rhs):
	return lhs * rhs

def exponent(lhs, rhs):
	return lhs ** rhs

print(do_stuff(add, 2, 3))
print(do_stuff(multiply, 2, 3))
print(do_stuff(exponent, 2, 3))
