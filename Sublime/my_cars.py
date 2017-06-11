#python3 my_cars.py

#from car import Car, ElectricCar

#my_beetle = Car('vw', 'beetle', 2018)
#print(my_beetle.get_description())

#my_tesla = ElectricCar('tesla', 'model s', 2018)
#print(my_tesla.get_description())


import car

my_beetle = car.Car('vw', 'beetle', 2018)
print(my_beetle.get_description())

my_tesla = car.ElectricCar('tesla', 'model s', 2018)
print(my_tesla.get_description())


