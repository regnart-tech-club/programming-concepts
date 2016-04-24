sqrt = lambda n: n ** .5
sqrt_5 = sqrt(5)
phi = (1 + sqrt_5) / 2
psi = (1 - sqrt_5) / 2
fibonacci = lambda n: int(round((phi ** n - psi ** n) / sqrt_5))

for n in range(-12, 12):
	print(fibonacci(n))
