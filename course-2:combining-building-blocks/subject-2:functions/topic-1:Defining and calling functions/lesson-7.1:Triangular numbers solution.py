# Write a function that takes one input
# and outputs the sum from 0 to that number.
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
