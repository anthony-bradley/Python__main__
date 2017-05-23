print ("\n")	#Try it yourself 6-1:

glen = {'first_name': 'glen', 'last_name': 'engle', 
		'age': 24, 'city': 'el cerrito'}

print (glen)

print ("\n")	#Try it yourself 6-2: Dictionary to store people's favorite #'s:

favorite_numbers = {
	'glen': 11,
	'mike': 23,
	'tony': 7,
	'alyse': 12,
}

print (favorite_numbers)

print ("\n")	#Try it yourself 6-3: 

import collections
from pprint import pprint
programming_words = {
	'list': 'Items enclosed in [] brackets.',
	'list_comprehension':'A simpler way to construct lists.',
	'tuple':'A list of immutable objects, enclosed in () brackets.',
	'pep 8':'Style guide for Python code.',
	'dict.items()':'Returns a copy of the dictionary\'s (key, value) pairs.',
	'slice':'A specific position to start, stop, increment. In lists/tuples.',

	'test': ('this', 'that', 'other'),
	'test2': ['this', 'that', 'other'],
}

pprint (programming_words)






