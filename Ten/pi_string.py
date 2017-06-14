#python3 pi_string.py

filename = 'pi_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

pi_string = ''

for line in lines:
	pi_string += line.rstrip()
	#pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))


#Birthday Pi

filename_2 = 'pi_million_digits.txt'

with open(filename_2) as file_object:
	lines = file_object.readlines()

pi_string_2 = ''

for line in lines:
	pi_string_2 += line.strip()

birthday = input("Enter birthday in the form of mmddyy: ")
if birthday in pi_string:
	print("Your birthdate is present in Pi!")
else:
	print("Your birthdate in not present in Pi...")

#print(pi_string_2[:52] + "...")
#print(len(pi_string_2))

