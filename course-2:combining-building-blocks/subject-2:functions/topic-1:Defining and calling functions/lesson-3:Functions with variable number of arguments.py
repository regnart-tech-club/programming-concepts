def sum(*args):
	s = 0
	
	for a in args:
		s += a
		
	return s

print(sum())
print(sum(1))
print(sum(1, 2))
print(sum(1, 2, 4))
print(sum(1, 2, 4, 8))
print(sum(1, 2, 4, 8, 16))
print(sum(1, 2, 4, 8, 16, 32))
print(sum(1, 2, 4, 8, 16, 32, 64))
