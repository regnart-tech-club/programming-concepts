# Implement the Fibonacci function as a functor.
class Fibonacci:
	def _square_root(self, n):
		return n ** .5

	def __call__(self, n):
		square_root_5 = self._square_root(5)
		phi = (1 + square_root_5) / 2 # the golden ratio
		psi = (1 - square_root_5) / 2 # 1 - phi

		return (phi ** n - psi ** n) / square_root_5

def test(condition):
	if condition():
		print('Thumbs up.')
	else:
		print('Thumbs down.')		

def is_equal_to(lhs, rhs):
	return lambda: abs(lhs - rhs) <= 2.220446049250313e-16 ** .5

fibonacci = Fibonacci()

test(is_equal_to(fibonacci(-6), -8))
test(is_equal_to(fibonacci(-5), 5))
test(is_equal_to(fibonacci(-4), -3))
test(is_equal_to(fibonacci(-3), 2))
test(is_equal_to(fibonacci(-2), -1))
test(is_equal_to(fibonacci(-1), 1))
test(is_equal_to(fibonacci(0), 0))
test(is_equal_to(fibonacci(1), 1))
test(is_equal_to(fibonacci(2), 1))
test(is_equal_to(fibonacci(3), 2))
test(is_equal_to(fibonacci(4), 3))
test(is_equal_to(fibonacci(5), 5))
test(is_equal_to(fibonacci(6), 8))
