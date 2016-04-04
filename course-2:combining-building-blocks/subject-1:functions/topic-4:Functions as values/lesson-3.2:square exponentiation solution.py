# Write a lambda, `square`, that has one parameter and returns its square.
square = lambda n: n ** 2

def test_0():
	if square(0) == 0:
		print('Thumbs up.')
	else:
		print('Thumbs down.')

def test_1():
	if square(1) == 1:
		print('Thumbs up.')
	else:
		print('Thumbs down.')

def test_2():
	if square(2) == 4:
		print('Thumbs up.')
	else:
		print('Thumbs down.')

def test_3():
	if square(3) == 9:
		print('Thumbs up.')
	else:
		print('Thumbs down.')

test_0()
test_1()
test_2()
test_3()
