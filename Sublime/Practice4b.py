members_un = ['bolivia', 'egypt', 'ethiopia', 'italy', 'japan', 'kazakhstan', 'senegal', 'sweden', 'ukraine']
print members_un[1:4] # Starts at e 'egypt', ends before j 'japan. #slice
print members_un[:6] # 0 to 6.
print members_un[2:] # From 2 over.
print members_un[-3:] # Last three.
print "\n"

destinations_desired = ['costa rica', 'bolivia', 'buenos aires', 'spain', 'germany']

print "These are the countries of which I would like to visit: "
for destinations_desired in destinations_desired:
	print destinations_desired.title()
print "\n"

destinations_desired = ['costa rica', 'bolivia', 'buenos aires', 'spain', 'germany']
#destinations_desired.append('cuba')	# Play with the placement.
sites_location_scouted = destinations_desired[:] # Not the same as 'sites_location_scouted = destinations_desired'

sites_location_scouted.append('cuba')
destinations_desired.append('iceland')

print sites_location_scouted
print destinations_desired
print "\n"














































