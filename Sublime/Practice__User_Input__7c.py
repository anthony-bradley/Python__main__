#python3 practice7c.py
print("\n") #confirmed.py


unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
	confirmed_user = unconfirmed_users.pop()

	print("Verifying user: " + confirmed_user.title()) #popping
	confirmed_users.append(confirmed_user)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
	print(confirmed_user.title())

#Pops them in order (from the end) and adds them to a list.
#Returns the list in order.


print("\n") #pets.py


pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
	pets.remove('cat')

print(pets)


print("\n") #mountain_poll.py


responses = {}

polling_active = True

while polling_active:
	name = input("\nWhat is your name? ")
	prompt = input("Which mountain would you like to climb someday? ")

	responses[name] = prompt #responses[prompt] = name -- switches order. [?]
	#answer = creates a [key, value] pair in the dictionary.

	repeat = input("Would you like to let another person respond? (yes/no) ")
	if repeat == "no": #or repeat == "nah" or repeat == "nope":
		polling_active = False
	#elif repeat == "yes" or repeat == "yup" or repeat == "yeah":
		#polling_active = True

print("\n --- Poll Results ---")
for name, response in responses.items():
	print(name.title() + " would like to climb " + response.title() + ".")


print("\n") #terminate.

