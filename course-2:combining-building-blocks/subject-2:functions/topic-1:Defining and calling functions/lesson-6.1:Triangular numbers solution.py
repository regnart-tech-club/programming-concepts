# Write a function that takes one input
# and outputs the sum from 0 to that number.
def triangular(n):
	sum = 0
	for i in range(n + 1):
		sum += i
		
	return sum

def test_triangular_equals(arg, expected):
	if triangular(arg) == expected:
		print('Thumbs up.')
	else:
		print('Thumbs down.')

test_triangular_equals(0, 0)
test_triangular_equals(1, 1)
test_triangular_equals(2, 3)
test_triangular_equals(3, 6)
