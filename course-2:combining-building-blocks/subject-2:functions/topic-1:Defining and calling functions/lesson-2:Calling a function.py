def get1():
	return 1

def add1(arg):
	return arg + 1

def add(lhs, rhs):
	return lhs + rhs

# TODO: Talk about scope
# TODO: Talk about parameters versus arguments
# TODO: Talk about the call stack and memory as it pertains to variables
print(get1())
print(add1(-1))
print(add(1, 2))
print(add(2, 3))
print(add(3, 5))
