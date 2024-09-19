# -*- coding: utf-8 -*-

my_vehicle = {
    "model": "Ford",
    "make": "Explorer",
    "year": 2018,
    "mileage": 40000
}

for x,y in my_vehicle.items():
    print(x,y)
    
my_vehicle2 = my_vehicle.copy()
print(my_vehicle2)    
    
my_vehicle2["no_of_tires"] = 4
print(my_vehicle2)

my_vehicle2.pop("mileage")
print(my_vehicle2)
print(my_vehicle)
