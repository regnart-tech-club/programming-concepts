def fibonacci(n):
  f0 = 0
  f1 = 1
	
  for i in range(0, n):
    f2 = f0 + f1
    f0 = f1
    f1 = f2
		
  return f0

def test_0():
  if fibonacci(0) == 0:
    print('Thumbs up.')
  else:
    print('Thumbs down.')

def test_1():
  if fibonacci(1) == 1:
    print('Thumbs up.')
  else:
    print('Thumbs down.')

def test_2():
  if fibonacci(2) == 1:
    print('Thumbs up.')
  else:
    print('Thumbs down.')

def test_3():
  if fibonacci(3) == 2:
    print('Thumbs up.')
  else:
    print('Thumbs down.')

def test_4():
  if fibonacci(4) == 3:
    print('Thumbs up.')
  else:
    print('Thumbs down.')

def test_5():
  if fibonacci(5) == 5:
    print('Thumbs up.')
  else:
    print('Thumbs down.')

def test_6():
  if fibonacci(6) == 8:
    print('Thumbs up.')
  else:
    print('Thumbs down.')

test_0()
test_1()
test_2()
test_3()
test_4()
test_5()
test_6()
