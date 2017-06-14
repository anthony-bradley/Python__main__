#python3 TIY__Classes__9e.py

#S = Solutions


#OrderedDict Rewrite: 9-13:

from collections import OrderedDict

programming_words = OrderedDict()

programming_words['list'] = 'Items enclosed in [] brackets.'
programming_words['list comprehension'] = 'A simpler way to construct lists.'
programming_words['tuple'] = 'List of immutable objects.'
programming_words['pep 8'] = 'Style guide for Python code.'
programming_words['slice'] = 'A specific position to start, stop, increment.'
programming_words['slice'] += ' In lists/tuples.'
programming_words['key'] = 'First part of an item in a dictionary.'
programming_words['key'] += ' Coupled with value.'
programming_words['value'] = 'Second part of an item in a dictionary.'
programming_words['value'] += ' Coupled with key.'
programming_words['pprint'] = '"Pretty print". Nicely formats a list.'

for word, definition in programming_words.items():
	print (word.title() + " = " + definition)


#Dice: 9-14:

from random import randint

class Die():
	""" """
	def __init__(self, sides=6):
		""" """ 
		self.sides = sides

	def roll_die(self):
		""" """
		return randint(1, self.sides) # S (and below)

d6 = Die() #Makes a 6-sided dice object.

results = [] #Creates an empty dictionary.

for roll_num in range(10):
	result = d6.roll_die()
	results.append(result)

print("\n10 rolls of a 6-sided dice: ")
print(results)

# ^S

d10 = Die()

results = []

for roll_num in range(10):
	result = d10.roll_die()
	results.append(result)

print("\n10 rolls of a 10-sided die: ")
print(results)


d20 = Die()

results = []

for roll_num in range(10):
	result = d20.roll_die()
	results.append(result)

print("\n10 rolls of a 20-sided dice: ")
print(results)