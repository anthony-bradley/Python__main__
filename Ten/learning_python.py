#python3 learning_python.py

with open('learning_python.txt') as file_object:
	contents = file_object.read()
	print(contents)

print("\n")

filename = 'learning_python.txt'

with open(filename) as file_object:
	for line in file_object:
		print(line.rstrip())


print("\n")


with open(filename) as file_object:
	lines = file_object.readlines()

lp_lines = ''

for line in lines:
	lp_lines += line
	#print(line.strip())

print(lp_lines)


print("\n")


with open(filename) as file_object:
	lines = file_object.readlines()

for line in lines:
	line = line.rstrip()
	print(line.replace('Python', 'C'))