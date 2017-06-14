#python3 guest.py

#prompt = "What is your name?"
#prompt += "\nName here: "

#name = input(prompt)

#filename = 'guest.txt'

#with open(filename, 'w') as file_object:
#	file_object.write(name.title())

#Guest Book: 10-4:

#filename = 'guest_book.txt'

#prompt = "What is your name?"
#prompt += "\nName (enter 'q' to exit the prompt): "

#active = True

#while active:
#	name = input(prompt)

#	if name == 'q':
#		break

#	else:
#		with open(filename, 'a') as file_object:
#			file_object.write("\n" + name.title())
#		continue

#Programming Poll: 10-5:

filename = 'programming_poll.txt'

programming_prompt = "Why do you like programming?"
programming_prompt += "\nAnswer (Press 'q' to exit prompt):"

active = True

while True: 
	reason = input(programming_prompt)

	if reason == 'q':
		break

	else:
		with open(filename, 'a') as file_object:
			file_object.write("\n" + reason)
		continue