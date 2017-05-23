#5-8
#5-9
#cd desktop/python/sublime
print "\n"

names_users = ['admin', 'jake', 'jill', 'sam', 'charlie']
#names_users = []

if names_users:
	for names_users in names_users:		#Runs a loop.
		if names_users == 'admin'.title() or names_users == 'admin':
			print "Hello admin, would you like to see a status report?"
		elif names_users != 'admin'.title() or names_users != 'admin':
			print ("Hello " + names_users.title() 
							+ ", thank you for logging in again.")
else:
	print "We need more users!".title()

print "\n"

#5-10
#Added a line comprehension for capitalization and line spacing.
current_users = ['Bennet', 'jake', 'jill', 'sam', 'charlie'] 
#Play with 'bennet' capitalization and line spacing.
new_users = ['arty', 'paulie', 'christopher', 'patricia', 'cody', 'beNNet']

#current_users_lower = [user.lower() for user in current_users]
current_users_title = [user.title().strip() for user in current_users]

for new_users in new_users:
	if new_users.title().strip() in current_users_title:
		print ("The user name '" + new_users 
			+ "' is taken, you'll need to enter a new user name.")
	else: 
		print "Great! The user name '" + new_users + "' is available."

print "\n"

#5-10
#Once more for readability.

current_users = ['Bennet', 'jake', 'jill', 'sam', 'charlie']

new_users = ['arty', 'paulie', 'christopher', 'patricia', 'cody', 'beNNet']

current_users_title = [user.title().strip() for user in current_users]

for new_users in new_users:
	if new_users.title().strip() in current_users_title:
		print ("The user name '" + new_users 
			+ "' is taken, you'll need to enter a new user name.")
	else: 
		print "Great! The user name '" + new_users + "' is available."

#5-11
print "\n"

#numbers = list(range(1,10))
#for numbers in numbers:
	#print numbers

print "\n"

for value in range(1,10):
	if value == 1:
		print str(value) + "st"
	elif value == 2:
		print str(value) + "nd"
	elif value == 3:
		print str(value) + "rd"
	else:
		print str(value) + "th"

print "Done!"

print "\n"






























