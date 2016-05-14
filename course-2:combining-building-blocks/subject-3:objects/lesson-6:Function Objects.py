class Add(object):
  def __init__(self, lhs):
    self.__lhs = lhs

  # TODO: Explain that overloading the `__call__` method allows an object to be used like a function.
  def __call__(self, rhs):
    return self.__lhs + rhs

add_2 = Add(2)
print(add_2(3))
