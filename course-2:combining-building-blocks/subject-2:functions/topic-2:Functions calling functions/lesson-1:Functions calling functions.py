def square(x):
	return x * x

def add_squares(x, y):
	return square(x) + square(y)

# TODO: Talk about the call stack and memory as it pertains to variables
print(add_squares(3, 4))
print(add_squares(5, 12))
print(add_squares(8, 15))
