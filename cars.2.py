import pandas as p
# Problem 2
cars = p.read_csv('cars.csv')

# letter a: Display the first five rows with odd numbered columns
d = cars.iloc[0:5,0::2]
print(d)
print("")

# letter b: Display the row of that contains the Model of Mazda RX4
a = cars.loc[cars['Model'] == 'Mazda RX4']
print("Mazda RX4:")
print(a)
print("")
print("")

# letter c: Determine how many cylinders and what gear type of the given car models
b = cars.loc[cars['Model'] == 'Camaro Z28',['Model','cyl']]
print("Number of Cylinders in Camaro Z28")
print("")
print(b)
print("")
print("")

# letter d:
c = cars.loc[cars['Model'].isin(['Mazda RX4 Wag','Ford Pantera L','Honda Civic']),['Model','cyl','gear']]
print("Cylinders and Gear Type of The Following:")
print("")
print(c)
