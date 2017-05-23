#python TIY5b.py
#5-3
alien_color = 'green'

print "\n"
if 'yellow' in alien_color:
	print "The alien is yellow.".title()
if 'green' in alien_color:
	print "The alien is green. You recieve 5 points.".title()
if 'red' in alien_color:
	print "The alien is red.".title()

print"\n"
if 'yellow' in alien_color:
	print "The alien is yellow.".title()
elif 'red' in alien_color:
	print "The alien is red.".title()
elif 'green' in alien_color:
	print "The alien is green. You recieve 5 points.".title()
else:
	print "Alien's color is unknown.".title()

print "\n"

alien_color_1 = ['green', 'yellow']
if 'yellow' in alien_color_1:
	print " " #"The alien is yellow.".title()
elif 'green' in alien_color_1:
	print "The alien is green.".title()
elif 'red' in alien_color_1:
	print "The alien is red."
else:
	print "Alien's color is unknown.".title()

#5-4 Come back to this.
print "\n"
alien_color_2 = 'red'
if 'green' in alien_color_2:
	print "You just earned 5 points for shooting the alien.".title()
if 'green' not in alien_color_2:
	print "You just earned 10 points.".title()

print "\n"
if 'green' in alien_color_2:
	print "5 points!".title()
elif 'green' not in alien_color_2:
	print "10 points!".title()
else:
	print "N/A"

print "\n"

#5-5
color_alien = 'green'

if 'green' in color_alien:
	print "The player earned 5 points.".title()
elif 'yellow' in color_alien:
	print "The player earned 10 points.".title()
elif 'red' in color_alien:
	print "The player earned 15 points.".title()

#5-6
print"\n"

age = 24

if age < 2:
	print "That person is a baby."
elif age >= 2 and age < 4:
	print "That person is a toddler."
elif age >= 4 and age < 13:
	print "That person is a kid."
elif age >= 13 and age < 20:
	print "That person is a teenager."
elif age >= 20 and age < 25:
	print "That person, age: " + str(age) + ", is a young adult."
elif age >= 30 and age < 65:
	print "That person is an adult."
elif age > 65:
	print "That person is an elder."

print "\n"

#5-7
favorite_fruits = ['apples','tangerines','bananas']

if 'apples' in favorite_fruits:
	print "\nYou really like " + favorite_fruits[0] + "."
if 'oranges' in favorite_fruits:
	print "You really like oranges"
if 'tangerines' in favorite_fruits:
	print "\nYou really like " + favorite_fruits[1] + "."
if 'tomato' in favorite_fruits:
	print "You really like tomatoes."
if 'bananas' in favorite_fruits:
	print "\nYou really like " + favorite_fruits[2] + "."

print "\n"































