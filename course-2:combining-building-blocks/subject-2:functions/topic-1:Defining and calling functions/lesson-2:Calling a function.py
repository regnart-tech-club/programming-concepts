def do_nothing():
	pass

def get1():
	return 1

def add1(arg):
	return arg + 1

def add(lhs, rhs):
	return lhs + rhs

print(do_nothing())
print(get1())

# TODO: Talk about scope
# TODO: Talk about parameters versus arguments
# TODO: Talk about the call stack and memory as it pertains to parameters and arguments
print(add1(-1))

n = 2
print(add1(n))

# TODO: Talk about how the function can be called multiple times thereby reusing the functionality and keeping things DRY.
print(add(1, 2))
print(add(2, 3))
print(add(3, 5))
