# Write a program that takes in one input assigned to the variable `ninjas`,
# prints "That's too many!" if the number is greater than 50,
# prints "It'll be a struggle, but I can take 'em." if the number is greater than or equal to 30 and less than 50,
# prints "I can fight those ninjas!" if the number is greater than or equal to 10 and less than 30,
# prints "I'll let my pet gerbil handle them." if the number is less than 10.

ninjas = int(input('How many ninjas?'))
if ninjas > 50:
	print "That's too many!"
elif ninjas >= 30:
	print "It'll be a struggle, but I can take 'em."
elif ninjas >= 10:
	print 'I can fight those ninjas!'
else:
	print "I'll let my pet gerbil handle them."
