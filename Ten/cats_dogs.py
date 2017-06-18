#python3 cats_dogs.py

#def read_files(filename):
#	"""Read files."""
#	try:
#		with open(filename) as file_object:
#			contents = file_object.read()
#			print(contents)
#	except FileNotFoundError:
#		message = "There is no '" + filename + "' file in your directory!"
#		print(message)

from read_files import read_files

filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
	read_files(filename)