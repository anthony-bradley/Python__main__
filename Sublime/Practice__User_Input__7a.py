#python3 practice7a.py
#pp.117 ->


message = input("Tell me something, and I will repeat it back to you: ")
print(message)


print("\n") #greeter.py:


name = input("Please enter you name: ")
print("Hello, " + name + "!")

prompt = "We'll first need your name."
prompt += "\nWhat is your name: "

name = input(prompt)

print("Welcome " + name)


print("\n") #


age = input("How old are you? ")

print("Okay " + name +  ", you are " + age + " years old. Very nice!")


age = input("How old are you? ")
age = int(age)
#print (age >= 18)
age >= 18
if True:
	print("\n\tLegal")



print("\n") #sigmanu.py


prompt = "How tall are you brah?"
prompt += "\nIn inches I am: "

height = input(prompt)
height = int(height)

if height >= 72:
	print("We're good to go bro! Sig Nuuuuuu!".upper())
else:
	print("\nSocial chair says nah brah...".title())


print("\n") #p.121 even_or_odd.py:

number =  input("Enter a number, and I'll tell you whether it's even or odd: ")
number = int(number)

if number % 2 == 0:
	print("\nThe number " + str(number) + " is even.")
else:
	print("\nThe number " + str(number) + " is odd.")