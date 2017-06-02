#RECAP
#python3 TIY__Functions__8d.py

#print("\n") #Magicians: 8-9:

#magicians = [
#'harry houdini', 
#'david blaine', 
#'david copperfield', 
#'criss angel'
#]

#def show_magicians(magicians):
#	"""Print the name of each magician in the list."""
#	for magician in magicians:
#		print(magician.title())

#show_magicians(magicians)


print("\n") #Great Magicians: 8-10:

#magicians = [
#'harry houdini', 
#'david blaine', 
#'david copperfield', 
#'criss angel',
#]


magicians = [
'harry houdini',
'david blaine',
'david copperfield', 
'criss angel',
]

def show_magicians(magicians):
	"""Print the name of each magician in the list."""
	for magician in magicians:
		print(magician.title())

def make_great(magicians):
	"""Adds 'The Great' to each magician's name while modifying the list."""
	great_magicians = []

	while magicians:
		removed_magician = magicians.pop(0)
		great_magician = 'The Great ' + removed_magician
		great_magicians.append(great_magician) # Appends singular magician to 
		# great_magicians list

	for great_magician in great_magicians:
		magicians.append(great_magician)

show_magicians(magicians)

print("\n")
make_great(magicians)
show_magicians(magicians)


print("\n") #Unchanged Magicians: 8-11:

magicians = [
'harry houdini',
'david blaine',
'david copperfield', 
'criss angel',
]

def show_magicians(magicians):
	"""Print the name of each magician in the list."""
	for magician in magicians:
		print("\t" + magician.title())
	print("\n")

def make_great(magicians):
	"""Adds 'The Great' to each magician's name while modifying the list."""
	great_magicians = []

	while magicians:
		removed_magician = magicians.pop(0)
		great_magician = 'The Great ' + removed_magician
		great_magicians.append(great_magician) # Appends singular magician to 
		# great_magicians list

	for great_magician in great_magicians:
		magicians.append(great_magician)
		#print(magicians)

	return magicians

show_magicians(magicians)

#New code:
print("\nGreat Magicians: ")
great_magicians = make_great(magicians[:])
#Call function while putting copied list in a new (empty) list.
show_magicians(great_magicians)

print("\nOriginal list of Magicians: ")
show_magicians(magicians)