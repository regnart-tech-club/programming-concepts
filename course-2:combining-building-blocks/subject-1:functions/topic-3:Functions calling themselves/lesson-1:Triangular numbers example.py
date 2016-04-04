def triangular_number(n):
	if n != 0:
		return n + triangular_number(n - 1)
	else:
		return 0

for n in range(0, 12):
	print(triangular_number(n))
