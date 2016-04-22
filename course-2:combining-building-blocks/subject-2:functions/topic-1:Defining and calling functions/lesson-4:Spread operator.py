def sum(*args):
	s = 0
	
	for a in args:
		s += a
		
	return s

a = [1]
b = [1, 2]
c = [1, 2, 4]
d = [1, 2, 4, 8]
e = [1, 2, 4, 8, 16]

print(sum(*a))
print(sum(*b))
print(sum(*c))
print(sum(*d))
print(sum(*e))

def get1():
	return 1

def add1(arg):
	return arg + 1

def add(lhs, rhs):
	return lhs + rhs

print(get1(*[]))
print(add1(*[1]))
print(add(*[1, 2]))
