members_un = ['bolivia', 'egypt', 'ethiopia', 'italy', 'japan', 'kazakhstan', 'senegal', 'sweden', 'ukraine']
for members_un in members_un:
	print members_un.title() + ", you are all cordially invited to the next summit."
	print " Your attendance is mandatory. \n"

print "- UN Council 4-14 \n"

for value in range(0,4): # Prints 0 - 3.
	print value

numbers = list(range(1,6)) # Puts 1 - 5 in a list.
print numbers

odd_numbers = list(range(1,21,2))
print odd_numbers

squares = []
for value in range(1,11): # 1 - 10
		square = value**2
		squares.append(square)

print squares
print "\n"
print "OR \n"

squares = []
for value in range(1,11):
	squares.append(value**2)

print squares

print min(squares)
print max(squares)
print sum(squares)
print "\n"
print min(odd_numbers)
print max(odd_numbers)
print sum(odd_numbers)
print "\n"





































