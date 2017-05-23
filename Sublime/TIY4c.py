# 4-10
members_un = ['bolivia', 'egypt', 'ethiopia', 'italy', 'japan', 'kazakhstan', 'senegal', 'sweden', 'ukraine']
members_un_new_1 = members_un[:]
members_un_new_2 = members_un[:]
print "\n"
print "The first three items in the list are: " 
for members_un in members_un[:3]:
	print members_un.title()
print "\n"


print "Three items from the middle of the list are: "
for members_un_new_1 in members_un_new_1[3:6]:
	print members_un_new_1.title()
print "\n"

print "The last three items in the list are: "
for members_un_new_2 in members_un_new_2[6:]:
	print members_un_new_2.title()
print "\n"

# 4-11
toppings_pizza = ['salami', 'anchovies', 'artichokes']
pizza_friend = toppings_pizza[:]

toppings_pizza.append('pepperoni')
pizza_friend.append('pepperoncini')

print "My favorite pizzas are: "
for toppings_pizza in toppings_pizza:
	print toppings_pizza
print "\n"

print "My friend's favorite pizzas are: "
for pizza_friend in pizza_friend:
	print pizza_friend
print "\n"

# 4-12		# foods.py
my_foods = ['pizza', 'falafel', 'carrot cake']
food_friend = my_foods[:]

my_foods.append('ice cream')
food_friend.append('baklava')

print "My favorite foods: ".upper()
for my_foods in my_foods:
	print my_foods.title() + "."
print"\n"

print "My friends favorite foods are: ".upper()
for food_friend in food_friend:
	print food_friend.title() + "."
print "\n"


