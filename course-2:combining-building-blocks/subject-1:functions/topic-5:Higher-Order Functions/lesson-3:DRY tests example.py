def fibonacci(n):
  f0 = 0
  f1 = 1
	
  for i in range(0, n):
    f0 = f0 + f1
	
    f0 = f0 ^ f1
    f1 = f1 ^ f0
    f0 = f0 ^ f1
		
  return f0

def test(condition):
	if condition():
		print('Thumbs up.')
	else:
		print('Thumbs down.')		

def is_equal_to(lhs, rhs):
	return lambda: lhs == rhs

def test_first():
	test(is_equal_to(fibonacci(0), 0))

def test_second():
	test(is_equal_to(fibonacci(1), 1))

def test_third():
	test(is_equal_to(fibonacci(2), 1))

def test_fourth():
	test(is_equal_to(fibonacci(3), 2))

def test_fifth():
	test(is_equal_to(fibonacci(4), 3))

def test_sixth():
	test(is_equal_to(fibonacci(5), 5))

def test_seventh():
	test(is_equal_to(fibonacci(6), 8))

test_first()
test_second()
test_third()
test_fourth()
test_fifth()
test_sixth()
test_seventh()
