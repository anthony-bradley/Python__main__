#python3 tiy7c.py
print("\n") #Deli: 7-8:


sandwich_orders = ['pastrami', 'italian', 'meat lovers']
finished_sandwiches = []

for sandwich_order in sandwich_orders:
	print("Your " + sandwich_order.title() + " sandwich is being prepared.")
print("\n")

sandwich_orders.reverse() #Eureka!

while sandwich_orders:
	finished_sandwich = sandwich_orders.pop() 
	print("Finishing up: " + finished_sandwich.title() + " sandwich.")
	#pops but doesn't do anything with them.

	finished_sandwiches.append(finished_sandwich)
print("\n")

print("Please pick-up at the front counter: ")

for finished_sandwich in finished_sandwiches:
	print(finished_sandwich.title() + " sandwich.")


print("\n") #No Pastrami: 7-9:


print("[The deli has unfortunately run out of pastrami].\n")

sandwich_orders = ['pastrami', 'italian', 'pastrami' ,'meat lovers', 'pastrami']
finished_sandwiches = []

while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')

for sandwich_order in sandwich_orders:
	print("Your " + sandwich_order.title() + " sandwich is being prepared.")
print("\n")

sandwich_orders.reverse() #Eureka!

while sandwich_orders:
	finished_sandwich = sandwich_orders.pop() 
	print("Finishing up: " + finished_sandwich.title() + " sandwich.")
	#pops but doesn't do anything with them.

	finished_sandwiches.append(finished_sandwich)
print("\n")

print("Please pick-up at the front counter: ")

for finished_sandwich in finished_sandwiches:
	print(finished_sandwich.title() + " sandwich.")


print("\n") #Dream Vacation: 7-10:


name_prompt = "\nWhat is your name? "
name_prompt += "\n\t(To terminate session at any time, hit CTRL-C)	"
place_prompt = "\n"
place_prompt += "If you could visit one place in the world, where would it be? "
active_session_prompt = "\nWould you like let another person respond? (yes/no) "

reponses = {}

session_active = True

while session_active:
	name = input(name_prompt)
	location = input(place_prompt)

	reponses[name] = location

	repeat = input(active_session_prompt)
	if repeat == "no":
		session_active = False

print("---Polling Results---")
for name, location in reponses.items():
	print(name.title() + " would like to visit " + location.title() + ".")


print ("\n") #Terminate.






























