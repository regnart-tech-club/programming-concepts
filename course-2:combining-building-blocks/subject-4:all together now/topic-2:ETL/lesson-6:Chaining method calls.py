class List(object):
	def __init__(self, *elements):
		self._elements = elements

	def __repr__(self):
		return str(list(self._elements))

	def filter(self, f):
		return List(*filter(f, self._elements))

	def map(self, f):
		return List(*map(f, self._elements))
	
	def reduce(self, f):
		return reduce(f, self._elements)

l = List(*range(5))
print l
print l.map(lambda n: n ** 2)
print (l
	  .map(lambda n: n ** 2)
	  .filter(lambda n: n % 2 == 0))
print (l
	  .map(lambda n: n ** 2)
	  .filter(lambda n: n % 2 == 0)
	  .reduce(lambda l, r: l + r))
