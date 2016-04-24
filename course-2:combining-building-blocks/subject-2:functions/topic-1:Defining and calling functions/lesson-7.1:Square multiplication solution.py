# A square of a number, n, is the number multiplied by itself.

# Write a function, `square`, that has one parameter and returns its square.
def square(n):
	# Return `n` times `n`.
	return n * n

# TODO: Talk about automated testing
# TODO: Show what happens if the function returned `n`.
# TODO: Show what happens if the function returned `n + n`.
# TODO: SHow what happens if the function returned `n ** n`.
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
