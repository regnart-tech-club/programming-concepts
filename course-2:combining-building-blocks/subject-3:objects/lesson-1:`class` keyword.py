# TODO: Explain types (eg Turtle, integer, string, etc).
class Greeter(object):
  # TODO: Explain constructor.
  def __init__(self, greeting):
    # TODO: Explain fields
    self._greeting = greeting

  # TODO: Explain methods.
  def greet(self, first_name, last_name):
    return '%s, %s %s' % (self._greeting, first_name, last_name)

# TODO: Explain instantiation.
greeter = Greeter('Hello')

# TODO: Explain method calls.
print(greeter.greet('Noel', 'Yap'))

# TODO: Explain field access.
print(greeter._greeting)

# TODO: Show `dir` of the object.
for m in dir(greeter):
  print m
