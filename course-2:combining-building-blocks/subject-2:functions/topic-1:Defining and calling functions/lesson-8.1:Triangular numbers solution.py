# Write a function that takes one parameter
# and returns the sum from 0 to that number.
# For example:
# If n = 0, it will return 0.
# if n = 2, it will return 0 + 1 + 2 which is 3.
# If n = 5, it will return 0 + 1 + 2 + 3 + 4 + 5 which is 15.
def triangular(n):
	# Define the resultant variable.
	sum = 0

	# Iterate through a range and add each element to the resultant variable.
	for i in range(n + 1):
		sum += i
		
	# Return the result.
	return sum

if triangular(0) == 0:
	print('Thumbs up.')
else:
	print('Thumbs down.')

if triangular(1) == 1:
	print('Thumbs up.')
else:
	print('Thumbs down.')

if triangular(2) == 3:
	print('Thumbs up.')
else:
	print('Thumbs down.')

if triangular(3) == 6:
	print('Thumbs up.')
else:
	print('Thumbs down.')
