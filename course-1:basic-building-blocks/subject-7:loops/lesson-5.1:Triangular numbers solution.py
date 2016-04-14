# Write a program that takes one input
# and outputs the sum from 0 to that number.
# Challenge: write the program without using any loops.

n = int(input('Enter a positive integer'))

c = n
sum = 0
while c > 0:
  sum += c
  c -= 1
	
print(sum)
print(n * (n + 1) / 2)
