#python3 addition.py

while  True:
	first_number = input("\nPlease provide your first number: ")
	if first_number == 'q':
		break
	second_number = input("Please provide your second number: ")
	if second_number == 'q':
		break

	try: 
		result = int(first_number) + int(second_number)
	except ValueError:
		print("Only provide numbers please.")
	else:
		print(result)
