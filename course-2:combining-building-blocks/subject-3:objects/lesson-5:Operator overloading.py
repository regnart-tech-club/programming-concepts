class Complex(object):
  def __init__(self, real_part, imaginary_part):
    self._real_part = real_part
    self._imaginary_part = imaginary_part

  def __str__(self):
    return '(%f, %f)' % (self._real_part, self._imaginary_part)

  def __add__(self, rhs):
    return Complex(self._real_part + rhs._real_part, self._imaginary_part + rhs._imaginary_part)

  def __mul__(self, rhs):
    return (Complex(
      self._real_part * rhs._real_part - self._imaginary_part * rhs._imaginary_part,
      self._real_part * rhs._imaginary_part + rhs._real_part * self._imaginary_part))

c = Complex(1, 2)
print(c) # Uses Complex.__str__

d = Complex(3, 5)

print(c + d) # Uses Complex.__add__
print(c * d) # Uses Complex.__mul__

# TODO: Show what happens if the __str__ definition is commented out.
