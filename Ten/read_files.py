#python3 read_files.py


def read_files(filename):
	"""Count the approximate number of words in a file."""
	try:
		with open(filename) as file_object:
			contents = file_object.read()
			print(contents)
	except FileNotFoundError:
		#message = "There is no '" + filename + "' file in your directory!"
		#print(message)
		pass


#filename = 'alice.txt'

#filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']

#for filename in filenames:
#	read_files(filename)