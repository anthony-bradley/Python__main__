#python3 names.py

from name_function import get_formatted_name

print("Enter 'q' to exit the prompt.")
while True:
	first = input("\nPlease give me your first name: ")
	if first == 'q':
		break
	last = input("Please give me a last name: ")
	if last == 'q':
		break

	formatted_name = get_formatted_name(first, last)
	print("\nNeatly formatted name: " + formatted_name)
	#break