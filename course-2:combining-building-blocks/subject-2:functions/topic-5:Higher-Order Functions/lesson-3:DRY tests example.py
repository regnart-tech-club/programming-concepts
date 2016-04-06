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

test(is_equal_to(fibonacci(0), 0))
test(is_equal_to(fibonacci(1), 1))
test(is_equal_to(fibonacci(2), 1))
test(is_equal_to(fibonacci(3), 2))
test(is_equal_to(fibonacci(4), 3))
test(is_equal_to(fibonacci(5), 5))
test(is_equal_to(fibonacci(6), 8))
