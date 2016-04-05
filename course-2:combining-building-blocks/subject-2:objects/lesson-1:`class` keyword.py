class Greeter:
	def __init__(self, greeting):
		self._greeting = greeting

	def greet(self, first_name, last_name):
		return '%s, %s %s' % (self._greeting, first_name, last_name)

greeter = Greeter('Hello')
print(greeter.greet('Noel', 'Yap'))
