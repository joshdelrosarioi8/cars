import pandas as p
cars = p.read_csv('cars.csv')

# Get the first 5 rows of the Dataframe and store it to A
A = cars.head()
# Get the last 5 rows of the Dataframe and store it to B
B = cars.tail()

# Append the rows of B to the rows of A and store it to Cars
Cars = p.concat([A,B])

# Displays the Dataframe of Cars
print(Cars)