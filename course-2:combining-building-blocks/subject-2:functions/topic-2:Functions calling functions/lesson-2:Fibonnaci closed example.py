def square_root(n):
	return n ** .5

def fibonacci(n):
	square_root_5 = square_root(5)
	phi = (1 + square_root_5) / 2 # the golden ratio
	psi = (1 - square_root_5) / 2 # 1 - phi

	return int(round((phi ** n - psi ** n) / square_root_5))

for n in range(-12, 12):
    print(fibonacci(n))
