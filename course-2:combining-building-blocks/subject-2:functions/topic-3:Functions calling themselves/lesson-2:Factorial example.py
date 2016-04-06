def factorial(n):
	if n != 0:
		return n * factorial(n - 1)
	else:
		return 1

for n in range(0, 12):
	print(factorial(n))
