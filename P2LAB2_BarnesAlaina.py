#Alaina Barnes
#6/20/2024
#P2Lab2
#Using dictionaries

cars = {'Camaro':18.21, 'Prius':52.36, 'Model S':110, 'Silverdo':26}

cars_keys = cars.keys()

print(cars_keys)

print(*cars_keys, sep = ", ")

car_name = input("Enter a vehicle to see its MPG: ")

car_mpg = cars[car_name]

print(f"The {car_name} gets {car_mpg} MPG.")

miles_driven = float(input(f'How many miles will you drive the {car_name}?: '))

gallons_needed = miles_driven/car_mpg

print(f'{gallons_needed:.2f} gallon(s) of gas are needed to drive the {car_name} {miles_driven} miles.')
