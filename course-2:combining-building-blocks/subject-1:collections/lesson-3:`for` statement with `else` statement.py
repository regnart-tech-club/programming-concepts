# try up to three times
for i in range(3): 
	password = input('Enter the password:')

	if password in ['Open sesame', 'Alohomora']:
		print('You may enter.')
		
		break
	else:
		print('Try again.')
else:
	# if `break` never called
	print('Begone!')
