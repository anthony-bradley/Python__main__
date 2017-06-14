#python3 write_message.py

filename = 'programming.txt'

with open(filename, 'w') as file_object:
	file_object.write("Test")
	file_object.write("\nTest_2")

with open(filename, 'a') as file_object:
	file_object.write("\nAppend_Test")
	file_object.write("\nAppend_Test_2")

