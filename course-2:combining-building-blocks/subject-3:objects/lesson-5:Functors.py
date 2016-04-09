class Add(object):
	def __init__(self, lhs):
		self.__lhs = lhs
		
	def __call__(self, rhs):
		return self.__lhs + rhs
	
add_2 = Add(2)
print(add_2(3))
