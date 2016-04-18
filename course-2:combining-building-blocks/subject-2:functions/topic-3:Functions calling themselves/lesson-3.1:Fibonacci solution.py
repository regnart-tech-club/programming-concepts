# Using recursion, write a function that, given an integer n, returns the nth Fibonacci number.
# For example, given n = 5, it should return 3.
def fibonacci(n):
  if n == 0 or n == 1:
    return n
  else:
    return fibonacci(n - 2) + fibonacci(n - 1)

def test_fibonacci_equals(arg, expected):
  if fibonacci(arg) == expected:
    print('Thumbs up.')
  else:
    print('Thumbs down.')

test_fibonacci_equals(0, 0)
test_fibonacci_equals(1, 1)
test_fibonacci_equals(2, 1)
test_fibonacci_equals(3, 2)
test_fibonacci_equals(4, 3)
test_fibonacci_equals(5, 5)
test_fibonacci_equals(6, 8)
