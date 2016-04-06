for i in range(3): 
	password = input('Enter the password:')

	if password in ['Open sesame', 'Alohomora']:
		print('You may enter.')
		
		break
	else:
		print('Try again.')
else:
	print('Begone!')
