# A square of a number, n, is the number multiplied by itself.
# Write a function, `square`, that has one parameter and returns its square.
def square(n):
	# Return `n` to the second power.
	return n ** 2

if square(0) == 0:
	print('Thumbs up.')
else:
	print('Thumbs down.')

if square(1) == 1:
	print('Thumbs up.')
else:
	print('Thumbs down.')

if square(2) == 4:
	print('Thumbs up.')
else:
	print('Thumbs down.')

if square(3) == 9:
	print('Thumbs up.')
else:
	print('Thumbs down.')
