#python3 Tiy7b.py: 7-4:

#7-4 Pizza Toppings:

prompt = "\nPlease enter the toppings you would like on your pizza: "
prompt += "\n(Enter the word 'quit' to exit the order process.) "
prompt += "\n\n"

while True:
	toppings = input(prompt)

	if toppings == 'quit':
		break
	else:
		print ("Okay! Let's add " + toppings.title() + " to your pizza!")
		break

#Conditional tests, active variables, break statements('quit'):
#7-5 and 7-6: Movie Tickets: 

prompt = "\n\nWe need to know your age for ticket pricing."
prompt += "\nHow old are you? "

prompt += "\n\n(Enter 'quit' at any time to end your ticket order.) "

active = True

while active:
	age = input(prompt)

	if age == 'quit':
		break	

	age = int(age)

	if age < 3:
		print("Your child's ticket is free!")
		break
	elif age > 3 or age < 12:
		print("Your ticket will be $10.00 at the window.")
		break
	else:
		print("Your ticket is $15.00 at the window.")
		break

print("\nThank you for visiting our theater!\n")


#7-7 Infinity Loop:

x = 1

while x == 1:
	print(x)