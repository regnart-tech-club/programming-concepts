while True: 
	password = input("Enter the password:")

	if password in ['Open sesame', 'Alohomora']:
		print('You may enter.')
		
		break
	else:
		print('Begone!')
