print("\n") #python3 Practice7b.py: counting.py:

current_number = 1
while current_number <= 5:
	print(current_number)
	current_number += 1 #current_number = current_number + 1


print("\n") #parrot.py:


prompt = "\nTell me something and I will repeat it back to you."
prompt += "\nOR enter 'quit' to end the program: "
 
#parrot.py PART I:
message = " " #Understandable to Python. Allows while loop to operate.

while message != 'quit':
	message = input(prompt)
	print(message)
 
#parrot.py PART II:
active = True
while active:
	message = input(prompt)

	if message == 'quit':
		active  = False
	else:
		print(message)


print("\n") #cities.py:


prompt = "\nPlease enter the name of the city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
	city = input(prompt)

	if city == 'quit': #Ends program after break, if 'quit' entered.
		break
	else:
		print("I'd like to go to " + city.title() + "!")


print("\n") #counting.py PART I:


current_number = 0
while current_number < 10:
	current_number += 1
	if current_number %2 == 0:
		continue

	print(current_number)


print("\n") #counting.py PART II (Infinite Loop):


x = 1
while x <= 5:
	print(x)
	x += 1 #x = 1, or any silmilar variation, will print forever.


print("\n")