#python3 guest.py

#prompt = "What is your name?"
#prompt += "\nName here: "

#name = input(prompt)

#filename = 'guest.txt'

#with open(filename, 'w') as file_object:
#	file_object.write(name.title())

#Guest Book: 10-4:

filename = 'guest_book.txt'

prompt = "What is your name?"
prompt += "\nName (enter 'q' to exit the prompt): "

active = True

while active:
	name = input(prompt)

	if name == 'q':
		break

	else:
		with open(filename, 'a') as file_object:
			file_object.write("\n" + name.title())
		continue

#