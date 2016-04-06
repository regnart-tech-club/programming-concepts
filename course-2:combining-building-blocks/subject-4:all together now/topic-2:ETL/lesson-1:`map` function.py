numbers = range(0, 15)

print map(lambda n: n ** n, numbers)
for i in map(lambda n: n ** n, numbers):
	print i
