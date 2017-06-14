#python3 favorite_languages.py

from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['tony'] = 'python'
favorite_languages['mike'] = 'c++'
favorite_languages['marlon'] = 'java'
favorite_languages['blatner'] = 'matlab'
favorite_languages['marcus'] = 'c'

for name, language in favorite_languages.items():
	print(name.title() + "'s favorite language is " + language.title() + ".")