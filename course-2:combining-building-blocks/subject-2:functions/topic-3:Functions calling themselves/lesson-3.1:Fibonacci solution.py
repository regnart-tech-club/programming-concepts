# The Fibonacci sequence starts with 0 and 1. Subsequent terms are then gotten by adding the previous two
# such that the first seven terms are: 0, 1, 1, 2, 3, 5, 8.

# Write a function that, given an integer n, returns the nth Fibonacci number.
# For example:
# given n = 0, the function should return 0
# if n = 1, it should return 1
# if n = 3, it should return 2
# if n = 5, it should return 5
# if n = 7, it should return 13
# Be sure to write automated tests for your solution.
def fibonacci(n):
	if n == 0 or n == 1:
		return n
	else:
		return fibonacci(n - 2) + fibonacci(n - 1)

def test_fibonacci_equals(arg, expected):
	observed = fibonacci(arg)
	
	if observed == expected:
		print('Thumbs up.')
	else:
		print('Thumbs down. Expected %i but got %i' % (expected, observed))

test_fibonacci_equals(0, 0)
test_fibonacci_equals(1, 1)
test_fibonacci_equals(2, 1)
test_fibonacci_equals(3, 2)
test_fibonacci_equals(4, 3)
test_fibonacci_equals(5, 5)
test_fibonacci_equals(6, 8)
