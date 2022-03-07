import pandas as pd
# Import cars data
cars = pd.read_csv("../python-datacamp/data/cars.csv", index_col = 0)
print(cars)

# Iterate over rows of cars
for lab, row in cars.iterrows():
    print(lab)
    print(row)


# Adapt for loop
for lab, row in cars.iterrows() :
    print(lab + ": " + str(row['cars_per_cap']))

# Code for loop that adds COUNTRY column
for col, row in cars.iterrows():
    cars.loc[col, "COUNTRY"] = row["country"].upper()

# Print cars
print(cars)

# Use .apply(str.upper)
cars["COUNTRY"] = cars["country"].apply(str.upper)

print(cars)
