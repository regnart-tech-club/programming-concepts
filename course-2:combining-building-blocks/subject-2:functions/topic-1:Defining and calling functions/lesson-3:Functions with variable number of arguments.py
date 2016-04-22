def sum(*args):
	s = 0
	
	for a in args:
		s += a
		
	return s

print(sum(1))
print(sum(1, 2))
print(sum(1, 2, 4))
print(sum(1, 2, 4, 8))
print(sum(1, 2, 4, 8, 16))
