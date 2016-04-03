def triangular_number(n):
	if n != 0:
		return n + triangular_number(n - 1)
	else:
		return 0
	
def factorial(n):
	if n != 0:
		return n * factorial(n - 1)
	else:
		return 1

n = int(input('number:'))
print(triangular_number(n))
print(factorial(n))
