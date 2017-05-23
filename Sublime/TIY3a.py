friends = ['glen', 'rick', 'aryo makoui', 'david', 'dan']
	#print friends

print friends[2].title()

msg_david = "Hey " + friends[-2].title() + ", what's going on?"
print msg_david

msg_rick = "YO " + friends[1].upper() + ", where you going?"
print msg_rick

method_transportation = ['tesla', 'jet', 'bullet train']

msg_tesla = "I would like to drive a " + method_transportation[0] + " so bad!"
print msg_tesla

method_transportation[0] = 'Jeep'
print method_transportation[0]

print method_transportation 
	#Jeep replaces Tesla.

method_transportation.append('ducati')
print method_transportation

#new
composers = []

composers.append('mozart')
composers.append('bach')
composers.append('handel')
composers.append('freshly exposed')
composers.append('dft boys')
print composers

composers.insert(2, 'tchaikovsky')
print composers

del composers[1]
print composers

#new
popped_composer = composers.pop()
print composers
print popped_composer.title()

print composers

#new

composer_favorite = composers.pop(-1)
print "My favorite musician group is: " + composer_favorite.title()

composers.remove('mozart')
print composers
	# How do I make sure the list prints in .title() form?

































