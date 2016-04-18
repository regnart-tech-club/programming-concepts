def triangular_number(n):
	if n == 0: # base case
		break
	else: # divide and conquer
		return n + triangular_number(n - 1)

for n in range(0, 12):
	print(triangular_number(n))
