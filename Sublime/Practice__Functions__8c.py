#python3 Practice__Functions__8c.py

print("\n") #formatted_name.py:

def get_formatted_name(first_name, last_name):
	"""Return a full name, neatly formatted."""
	full_name = first_name + ' ' + last_name
	return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
print("\n")


def get_formatted_name(first_name, middle_name, last_name):
	"""Return a full name, neatly formatted."""
	full_name = first_name + ' ' + middle_name + ' ' + last_name
	return full_name.title()

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)
print("\n")


def get_formatted_name(first_name, last_name, middle_name = ''):
	"""Return a full name, neatly formatted."""
	if middle_name:
		full_name = first_name + ' ' + middle_name + ' ' + last_name
	else:
		full_name = first_name + ' ' + last_name
	return full_name.title()

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

musician = get_formatted_name('jimi', 'hendrix')
print(musician)


print("\n") #person.py:

def build_person(first_name, last_name):
	"""Return a dictionary of inforation about a person."""
	person = {'first': first_name, 'last': last_name}
	return person

musician = build_person('jimi', 'hendix')
print(musician)
print("\n")


def build_person(first_name, last_name, age = ''):
	"""Return a dictionary of inforation about a person."""
	person = {'first': first_name, 'last': last_name}
	if age:
		person['age'] = age
	return person

musician = build_person('jimi', 'hendix', age = 27)
#musician = build_person('jimi', 'hendix', 27) #works.
print(musician)


print("\n") #greeter.py:

#def get_formatted_name(first_name, last_name):
#	"""Return a full name, neatly formatted."""
#	full_name = first_name + ' ' + last_name
#	return full_name.title()

##This is an infinite loop!:
#while True: 
#	print("\nLet's start with your name.")
#	f_name = input("First name: ")
#	l_name = input("Last name: ")

#	formatted_name = get_formatted_name(f_name, l_name)
#	print("\nHello, " + formatted_name)
#print("\n")


def get_formatted_name(first_name, last_name):
	"""Return a full name, neatly formatted."""
	full_name = first_name + ' ' + last_name
	return full_name.title()

#This is an infinite loop!:
while True: 
	print("\n~ Let's start with your name ~")
	print("(enter 'q' at any time to exit the program)")

	f_name = input("\nFirst name: ")
	if f_name == 'q':
		break

	l_name = input("Last name: ")
	if l_name == 'q':
		break

	formatted_name = get_formatted_name(f_name, l_name)
	print("\nHello, " + formatted_name)

#	Just learned multiline comments don't actually exist in Python, 
#	due to doctrings.