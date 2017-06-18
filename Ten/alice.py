#python3 alice.py

filename = 'alice.txt'

try:
	with open(filename) as file_object:
		contents = file_object.read()
except FileNotFoundError:
	message = "There is no '" + filename + "' file in your directory!"
	print(message)
else:
	#Count the number of words in the file.
	words = contents.split()
	num_words = len(words)
	print("The file '" + filename + "' has roughly " 
						+ str(num_words) + " words.")