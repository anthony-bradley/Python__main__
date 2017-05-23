#	*Figure out how to remove the [] in the output, ['java']

print ("\n")
#cd desktop/python/sublime
#python3 practice6c.py

alien_0 = {'color':'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for aliens in aliens:	#Allows print to list aliens off in order.
	print (aliens)



print ("\n")	#Create a fleet of aliens:
aliens = []

for aliens_number in range(30): #Tells python how many times to run the loop.
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'} 
	aliens.append(new_alien)
		#Every time the loop runs we create a new alien with append.

for alien in aliens [:5]: #Prints only 5 of the newly created elements.
	print(alien)
print("\n")

print("Total number of aliens: " + str(len(aliens))) #Proves the fleet exists.



print ("\n")	#Same as above. Except with cars:
cars = []

for cars_number in range(1000):
	new_car = {'color': 'red', 'price': 200000, 'make': 'ferrari'}
	cars.append(new_car)

#Newly added code:
for car in cars[:5]:
	if car['color'] == 'red':
		car['color'] = 'yellow'
		car['make'] = 'lamborghini'
		car['price'] = 250000

for car in cars [:10]:
	print(car)
print ("\n")

print("Total number of cars: " + str(len(cars)))



print ("\n")	#favorite_languages.py p.112:

#	*1
favorite_languages = {
	'andrew' : ['matlab', 'c++'],
	'mike' : ['python', 'java', 'c++'],
	'marcus' : ['c++', 'java'],
	'marlon' : ['java'],
	'anthony': ['python', 'd', 'hadoop'] 
}

#if len(favorite_languages) <= 1:
	#print(name.title()+ "'s favorite language is " + favorite_languages.items())

#for name, languages in favorite_languages.items():
	#print ("The favorite language(s) of " + name.title() + " are: ")
	#for language in languages:
		#print ("\t" + language.title())

for name, languages in favorite_languages.items():
	if len(languages) <= 1:
		print(name.title() + "'s favorite language is " + str(languages) + "\n")
for name, languages in favorite_languages.items():
	if len(languages) > 1:
		print ("\n")
		print (name.title() + "'s favorite languages are: ")
		for language in languages:
			print ("\t" + language.title())

print ("\n")	#pp.113-114 many_users.py:

users = {
	'aeinstein': {
		'first': 'albert',
		'last': 'einsten',
		'location': 'princeton',
	},
	'mcurie': {
		'first': 'marie',
		'last': 'curie',
		'location': 'paris',
	},
}

for username, user_info in users.items():
	print("\nUsername: " + username)
	
	full_name = user_info['first'] + " " + user_info['last']
	location = user_info['location']

	print("\tFull Name: " + full_name.title())
	print("\tLocation: " + location.title())













































































