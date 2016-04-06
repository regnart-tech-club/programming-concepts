numbers = range(0, 15)

print filter(lambda n: n % 2 == 0, numbers)
for i in filter(lambda n: n % 2 == 0, numbers):
	print i
