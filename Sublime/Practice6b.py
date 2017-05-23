print ("\n")	#Looping through key-value pairs.

user_cal = {
	'username' : 'dking',
	'first' : 'dan',
	'last' : 'king',
}

for key, value in user_cal.items():                       #.items(), new method.
	print ("\nKey: " + key)
	print ("Value: " + value)

                                           #key and value are mutable variables.

print ("\n")	#Favorite_languages.py	p.104

fav_langs = {
	'jen' : 'python',
	'sara' : 'html',
	'james' : 'java',
	'marlon' : 'r',
	}

for name, lang in fav_langs.items():
	print (name.title() + "'s favorite language is " + lang.title() + ".")

print ("\n")	#Favorite_languages.py	Part II 

friends = ['james', 'marlon']      #Has to be here due to for and if operations.
for name in fav_langs:
	print ("\n" + name.title())

	if name in friends:
		print ("Hi, " + name.title() + " I see your favorite language is "
						+ fav_langs[name].title() + ". ;)")

if 'erin' not in fav_langs:                #Had to play around with the indents.
	print ("\nErin, please take our poll. :)")

print ("\n")	#Looping through a dictionarys keys in order.

for name in sorted(fav_langs):        #Wrapped sorted() around dictinary.keys().
	print ("\n" + name.title() + ", thank you for participating in our poll.")

print ("\n")	#Looping through all values in a dictionary.

favorite_languages = {
	'mit' : 'python',
	'harvard' : 'python',
	'berkeley' : 'C',
	'other' : 'java',	
}

for name, language in favorite_languages.items():
	print (name.title())

print ("\n")                                                               #Space.

for language in set(favorite_languages.values()):
	print (language.title())

print ("\n")	#


























