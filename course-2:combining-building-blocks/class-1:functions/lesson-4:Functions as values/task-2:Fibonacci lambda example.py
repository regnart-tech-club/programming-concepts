sqrt = lambda n: n ** .5
sqrt_5 = sqrt(5)
phi = (1 + sqrt_5) / 2
psi = (1 - sqrt_5) / 2
fibonacci = lambda n: int((phi ** n - psi ** n) / sqrt_5)

for n in range(0, 12):
	print(fibonacci(n))

for n in range(-12, 0):
	print(fibonacci(n))
