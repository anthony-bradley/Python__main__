# 4-3
print "\n"
for value in range(1,21):
	print value
print "\n"

# 4-4
for value in range(1, 100000000): # Works, but memory error.
	print value
print "\n"

numbers_up_to_1000 = [value for value in range(0,100)]
print numbers_up_to_1000
print"\n"

print min(numbers_up_to_1000)
print max(numbers_up_to_1000)
print sum(numbers_up_to_1000)
print"\n"

odd_numbers = list(range(1,21,2))
print odd_numbers
print "\n"

for odd_numbers in odd_numbers:
	print odd_numbers
print "\n"

multiples_of_3 = list(range(3,31,3))
print multiples_of_3
print "\n"

for multiples_of_3 in multiples_of_3:
	print multiples_of_3
print "\n"

print "cubes:"
cubes = []
for value in range(1,11):
		cube = value ** 3 # Extra temporary value. 
		cubes.append(cube)

print cubes
print "\n"

for cubes in cubes:
	print cubes
print"\n"

print "cubes two [2]:"
cubes2 = []
for value in range(1,11):
	cubes2.append(value ** 3) # Minus the temporary value.
print cubes2
print "\n"

for cubes2 in cubes2:
	print cubes2
print "\n"

print "cubes_first_10:"
cubes_first_10 = [value ** 3 for value in range(1,11)] # List Comprehension.
print cubes_first_10
print "\n"

for cubes_first_10 in cubes_first_10:
	print cubes_first_10 
print "\n"































