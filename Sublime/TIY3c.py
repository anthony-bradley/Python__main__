# 3-8 
# 3-9
locations = ['rio', 'barcelona', 'berlin', 'new york', 'iceland']

print "A"
print locations
print sorted(locations) # Temporary
print locations

print "\nB"
print sorted(locations, reverse = True) # Temporary
print locations

print "\nC"
locations.reverse() # Permanent 
print locations

print "\nD"
locations.reverse() # Permanent 
print locations

print "\nE"
locations.sort() # Permanent
print locations

print "\nF"
locations.sort(reverse = True) # Permanent
print locations
print "_________________________________________________________"
print "\n"

# 3-10
members_un = ['bolivia', 'egypt', 'ethiopia', 'italy', '    japan    ', 'kazakhstan', 'senegal', 'sweden', 'ukraine']
members_un[0].title()
members_un[1].upper()
members_un[2].lower()
members_un[4].st
members_un.append('uruguay')
# members_un[0] = 'bolivia'		Replaces egypt.

print members_un
print len(members_un)

members_un.insert(0, 'united states')
print members_un
print len(members_un)

del members_un[0]
print members_un

violator_un_1 = members_un.pop(-1)
print violator_un_1.title()
print members_un
print len(members_un)

violator_un_2 = members_un.remove('italy')
#print violator_un_2	Can't use it. It's gone.
print members_un

# Use functions from practice3a.py and TIY3b.py
members_un.sort(reverse = True) # Permanent
print members_un

members_un.reverse() # Permanent
print members_un














































