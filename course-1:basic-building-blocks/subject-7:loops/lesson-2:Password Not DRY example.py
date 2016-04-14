good_passwords = ['Open sesame', 'Alohomora', 'ntoheuntoeh']

password = None
while password not in good_passwords: 
	password = input("Enter the password:")

	if password in good_passwords:
		print('You may enter.')
	else:
		print('Begone!')
