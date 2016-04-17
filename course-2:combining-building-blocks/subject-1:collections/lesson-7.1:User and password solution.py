# Using collections, write a program that will ask for a user name and password at most three times.
# If a correct pair of user name and password is entered, it will print 'You may enter.' and stop asking for user name and password.
# If an incorrect pair of user name and password is entered three times, it will print 'Begone!' and stop asking for user name and password.

# Define the passwords dictionary mapping user names to their passwords. 
passwords = {
	'Noel': 'Pay',
	'Yap': 'Leon'
}

# Try at most three times.
for i in range(3):
	user = input('User name:')
	password = input('Password:')
	
	# If the user name that was entered is in the password dictionary and the password entered matches the one in the dictionary, succeed.
	if user in passwords.keys() and passwords[user] == password:
		print 'You may enter.'
		
		break
else:
	# If the wrong user name and password pair has been entered incorrectly three times, fail.
	print 'Begone!'