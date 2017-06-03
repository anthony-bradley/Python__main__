#python3 making_pizzas.py

#import pizza #Import an entire module.

#pizza.make_pizza(16, 'pepperoni')
#pizza.make_pizza(12, 'mushrooms', 'green peppers', 'olives')


#from pizza import make_pizza #Importing specific functions.

#make_pizza(16, 'pepperoni')
#make_pizza(12, 'mushrooms', 'green peppers', 'olives')


#from pizza import make_pizza as mp #Give funtion an alias.

#mp(16, 'pepperoni')
#mp(12, 'mushrooms', 'green peppers', 'olives')


#import pizza as p #Give module an alias.

#p.make_pizza(16, 'pepperoni')
#p.make_pizza(12, 'mushrooms', 'green peppers', 'olives')


from pizza import * #Import all funtions in a module.

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'olives')