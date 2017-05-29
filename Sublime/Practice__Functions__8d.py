#python3 practice__functions__8d.py

print("\n") #greet_users.py:

def greet_users(names):
	"""Print a simple greeting to each user in the list."""
	for name in names:
		greeting = "Hello, " + name.title()
		print(greeting)

users = ['mike', 'dan', 'shoban']
greet_users(users)


print("\n")#print_vs_return.py:

def function_that_prints():
    print ("I printed")

def function_that_returns():
    return "I returned"

f1 = function_that_prints()
f2 = function_that_returns()

print("Print: ")
print(f1)

print("\nReturn: ")
print(f2)


print("\n") #printing_models.py:

#unprinted_designs = ['iphone case', 'android case', 'dodecahedron']
#completed_models = []

#while unprinted_designs:
#	current_design = unprinted_designs.pop(0)
#	print("Printing Model: " + current_design.title())
#	completed_models.append(current_design)

#print("\nThe following models have been printed: ")
#for completed_model in completed_models:
#	print (completed_model.title())

print("\n") #printing_models.py (part II with functions):

def print_models(unprinted_designs, completed_models):
	"""
	Simulate printing each design until none are left.
	Move each design to completed_models after printing.
	"""
	while unprinted_designs:
		current_design = unprinted_designs.pop()

		print("Printing Model: " + current_design)
		completed_models.append(current_design)

def show_completed_models(completed_models):
	"""Show all the models that were printed."""
	print("\nThe following models have been printed: ")
	for completed_model in completed_models:
		print (completed_model)

unprinted_designs = ['iphone case', 'android case', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
#print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)

print (unprinted_designs) #Choose to empty unprinted_designs list or not.
print("\n")