#python3 my_car.py

from car import Car

my_new_car = Car('audi', 'r8', 2018)
print(my_new_car.get_description())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()
