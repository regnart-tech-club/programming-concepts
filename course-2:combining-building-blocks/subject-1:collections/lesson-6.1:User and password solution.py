# Using collections, write a program that will ask for a user name and password at most three times.
# If a correct pair of user name and password is entered, it will print 'You may enter.' and stop asking for user name and password.
# If an incorrect pair of user name and password is entered three times, it will print 'Begone!' and stop asking for user name and password.
passwords = {
	'Noel': 'Pay',
	'Yap': 'Leon'
}

for i in range(3):
	user = input('User name:')
	password = input('Password:')
	
	if user in passwords.keys() and passwords[user] == password:
		print 'You may enter.'
		
		break
else:
	print 'Begone!'