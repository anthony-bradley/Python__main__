#New format for program readability. Use this:

print"\n"	#Coffee program:

coffee = {'price': 2, 'location': 'Peets'}

coffee_cost = coffee['price']
print 	("The price of your coffee is ".title() + str(coffee_cost) 
						+ " dollars.".title())

print "\n"	#Empty 'alien_1' dictionary:										

alien_1 = {}

alien_1['color'] = 'red'
alien_1['points'] = 10

print alien_1

print "\n"	#Add key-value to 'alien_1' dictionary:

alien_1['color'] = 'green'
print alien_1

print "\n"	#Start 'alien_0' dictionary:

alien_0 = {'color': 'green', 'points': 5}

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print alien_0

print "\n"	#Moves 'alien_0' x-position based on key-value 'speed':
			#Puts the new x-position back into the dictionary:

print "\n"
alien_0['speed'] = 'fast'
print "Original x-position: " + str(alien_0['x_position'])

if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print "\nNew x-position: " + str(alien_0['x_position'])

print "\nNew 'alien_0' dictionary:"
print "\n" + str(alien_0)

print "\n"	#Removing key-value pairs:

del alien_0['points']
print alien_0

print "\n"	#Dictionary for simple poll:

favorite_languages = {
	'marlon': 'java',
	'stephen': 'sql',
	'anthony':'python',
	'marcus': 'c',
}

print favorite_languages

print "\n"	#Dictionary look-up for a specific name.

print 	("Stephen's favorite language is: " + 
			favorite_languages['stephen'].title() + ".")

print "\n"	#End of practice6a.py

