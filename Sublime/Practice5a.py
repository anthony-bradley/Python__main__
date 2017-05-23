#python practice5a.py

print "\n"
cars = ['bmw', 'gmc', 'audi', 'tesla', 'acura', 'maserati']

for car in cars:	#cars in cars also works.
	if car == 'bmw' or car == 'gmc':
		print car.upper() + "."
	#elif car == 'gmc': 		#short for else if.
		#print car.upper() + "."
	else:
		print car.title() + "."
print "\n"
#cars works everywhere. But each item in 'cars' list is a car. so we use 'car'.

age = 18
print age == 18

car = 'Audi'
print car.lower() == 'audi'


sandwich_requested = 'Meatless'

if sandwich_requested != 'Chicken':
	print "Hold the Pollo!"

print age != 18 #False
print age != 20 #True
print "\n"

age = 20 #Equal To
print age < 21 #Less Than
print age <= 21 #Less or Equal To
print age > 21 #More Than
print age >= 21 #More or Equal To

guest_1 = 20
guest_2 = 21
if guest_1 <= 21 or guest_2 <= 21:		#May use () for readability.
	print "Please, see yourself out."
else:
	print "Enjoy! Have a drink!"

print "\n"
cars_two = cars[:]
print cars_two

print 'maserati' in cars_two #True
print 'ferrari' in cars_two #False

banned_users = ['dan', 'marcy', 'charles']
user = 'jake'
if banned_users not in banned_users:
	print user.title() + ", you can post now post on the forum."

user_2 = 'marcy'
if banned_users not in banned_users:
	print user_2.title() + ", you may not post on the forum at this time."

print "\n"
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
	print "Add Mushrooms!"
if 'extra cheese' in requested_toppings:
	print "Add Extra Cheese!"
if 'genoa salami' in requested_toppings:
	print "Add Salami!"

print "Your pizza should be ready in 25 minutes.".title()

































