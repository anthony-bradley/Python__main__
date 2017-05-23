# python TIY5a.py
# 5-1 conditional tests.

color = 'blue'
print color == 'BLUE'
#1 False - Capitalization.

color_1 = 'Red'
print color_1 == 'red'
#2 False - Capitalization.

print color == 'blue'
#3 True - Exact match.

print color_1 == 'red'
#4 False - Capitalization.

car = 'ferrari'
print car == 'ferrari'
#5 True - Exact match.

print color == 'BLUE'.lower()
#6 True.

color_1 = 'Red'.title()
#7 True.

var_1 = 'WOW'
print var_1 == 'wow'.upper()
#8 True.

age = 21
age_1 = 22
print age == 21 and age_1 == 22
#9 True.

print age < 21 or age_1 > 21
# True.

print age < 21 and age_1 > 21
#False.

print"\n"
# 5-2

berkeley_streets = ['addison', 'bonar', 'kittredge'.title(), 'vine']
print 'monterey'.title() in berkeley_streets
#False.

print 'kittredge'.title() in berkeley_streets
#True.

if 'bonar' in berkeley_streets: #Swap 'bona'
	print 'bonar'.title() + " is present."
else:
	print "There is no such street in Berkeley, Ca."

street = 'buenos isles'		#Replace with any item from berkeley_streets list.
if street not in berkeley_streets:
	print street.title() + " is not in Berkeley, Ca."
else:
	print street.title() + " is in Berkeley, Ca."

print"\n"
aarp_age_restriction = 50
age = 50 #Play around with number.

if age < aarp_age_restriction:
	print "Not eleigible for AARP membership."
elif age == aarp_age_restriction:
	print "Sign up now for AARP member services."
elif age >= aarp_age_restriction:
	print "Sign up now for AARP member services."
elif age > aarp_age_restriction:
	print "Sign up now for AARP member services."
else:
	print "See what our program has to offer."































