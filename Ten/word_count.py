#python3 word_count.py

def count_words(filename):
	"""Count the approximate number of words in a file."""
	try:
		with open(filename) as file_object:
			contents = file_object.read()
	except FileNotFoundError:
		#message = "There is no '" + filename + "' file in your directory!"
		#print(message)
		pass
	else:
		#Count the number of words in the file.
		words = contents.split()
		num_words = len(words)
		print("The file '" + filename + "' has roughly " 
							+ str(num_words) + " words.")

#filename = 'alice.txt'
filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
	count_words(filename)

