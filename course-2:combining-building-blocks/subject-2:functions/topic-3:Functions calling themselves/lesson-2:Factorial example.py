def factorial(n):
	if n == 0: # base case
		return 1
	else: # divide and conquer
		return n * factorial(n - 1)

for n in range(0, 12):
	print(factorial(n))
