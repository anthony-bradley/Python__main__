print ("\n")	#6-3	p.102: 

from pprint import pprint                                        #Stackoverflow.

programming_words = {
	'list': 'Items enclosed in [] brackets.',
	'list_comprehension':'A simpler way to construct lists.',
	'tuple':'A list of immutable objects, enclosed in () brackets.',
	'pep 8':'Style guide for Python code.',
	'slice':'A specific position to start, stop, increment. In lists/tuples.',
	'key': 'First part of an item in a dictionary. Coupled with value.',
	'value': 'Second part of an item in a dictionary. Coupled with key.',
	'pprint': '"Pretty print". Nicely formats a list for output.',
}

pprint (programming_words)

#print "\nIndividual keys below:".title()
#print programming_words['list']
#print programming_words['list_comprehension']
#print programming_words['tuple']
#print programming_words['pep 8']
#print programming_words['slice']

print ("\n")	#6-4	Glossary 2:
for key, value in programming_words.items():
	print ("\nKey: " + key)
	print ("Value: " + value)
print ("\n")

print ("\n")	#6-5. Rivers:

major_rivers__countries = {
	'nile': 'egypt',
	'yangtze': 'china',
	'amazon': 'south america',                          #brazil, peru, columbia.
}

pprint (major_rivers__countries)

for river, country in major_rivers__countries.items():
	print (("The " + river + " flows through " + country + ".").title())

#for rivers in major_rivers__countries.items():
	#print (river)

for river in major_rivers__countries.keys():
	print (river.title())

#for countries in major_rivers__countries.items():
	#print (country)

for country in major_rivers__countries.keys():
	print (country.title())

print ("\n")	#6-6. Polling:

favorite_languages = {
	'marlon': 'java',
	'stephen': 'sql',
	'anthony':'python',
	'marcus': 'c',
}

print (favorite_languages)

pollers = {'marlon', 'fernando', 'marcus', 'andrew', 'mike'}

for name in sorted(pollers):
	if name in favorite_languages:
		print ("Thank you for participating in our survey, " 
										+ name.title() + ".")
	else: 
		print ("Please take our survey, " + name.title() + ".")

"""for name in pollers:
	if name in pollers:
		print (name + "Please take our survey.")
"""

"""for name, language in favorite_languages:
	if name in favorite_languages:
		print ("Thank you " + name + " for participating in our survey.")
	if name not in favorite_languages:
			print ("Please take our survey.")
"""