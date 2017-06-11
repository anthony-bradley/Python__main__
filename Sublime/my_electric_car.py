#python3 my_electric_car.py

from car import ElectricCar

my_tesla = ElectricCar('tesla', 'model s', 2018)

print(my_tesla.get_description())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

