#python3 Tiy7a.py
print("\n") #TIY 7-1. Rental Car:


prompt = input("What kind of rental car would you like? ")

print("\nLet me see if I can find you a " + prompt.title() + ".")


print("\n") #7-2. Restaurant Seating:


prompt = input("How many people are in your party? ")

if int(prompt) > 8:
	print("\nPlease wait to be seated.")
else:
	print("\nYour table is ready.")


print("\n") #7-3. Multiples of Ten:


prompt = "Let's see if your number is a multiple of 10."
prompt += ("\nPlease give me a number: ")
prompt = input(prompt)
prompt = int(prompt)

if prompt % 10 == 0:
	print("\n\tYour number " + str(prompt) + " is indeed a multiple of 10.")
else:
	print("\n\tYour number " + str(prompt) + " is not a multiple of 10.")


print ("\n") 