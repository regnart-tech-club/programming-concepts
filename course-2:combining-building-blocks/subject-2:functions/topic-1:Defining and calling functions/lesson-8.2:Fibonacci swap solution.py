def fibonacci(n):
  # Define two variables to hold interim values and initialize them.
  f0 = 0
  f1 = 1
  
  # Iterate `n` times.
  for i in range(0, n):
    # Calculate the next value.
    f0 = f0 + f1
  
    # Swap `f0` and `f1` values.
    f0 = f0 ^ f1
    f1 = f1 ^ f0
    f0 = f0 ^ f1
    
  # Return the result.
  return f0

if fibonacci(0) == 0:
  print('Thumbs up.')
else:
  print('Thumbs down.')

if fibonacci(1) == 1:
  print('Thumbs up.')
else:
  print('Thumbs down.')

if fibonacci(2) == 1:
  print('Thumbs up.')
else:
  print('Thumbs down.')

if fibonacci(3) == 2:
  print('Thumbs up.')
else:
  print('Thumbs down.')

if fibonacci(4) == 3:
  print('Thumbs up.')
else:
  print('Thumbs down.')

if fibonacci(5) == 5:
  print('Thumbs up.')
else:
  print('Thumbs down.')

if fibonacci(6) == 8:
  print('Thumbs up.')
else:
  print('Thumbs down.')
