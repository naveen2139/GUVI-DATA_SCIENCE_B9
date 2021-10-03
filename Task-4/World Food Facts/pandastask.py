import pandas as pd
import numpy as np

# Use the tsv file and assign it to a dataframe called food
food=pd.read_csv('en.openfoodfacts.org.products.tsv',delimiter='\t',low_memory=False)

# See the first 5 entries
print("See the first 5 entries:")
print(food.head())
print()
# What is the number of observations in the dataset?
print("What is the number of observations in the dataset?")
print(food.shape)
print()

# What is the number of rows in the dataset?
print("What is the number of rows in the dataset?")
print(len(food))
print()

# What is the number of columns in the dataset?
print("What is the number of columns in the dataset?")
print(len(food.columns))
print()

# Print the name of all the columns.
print("Print the name of all the columns.")
print(food.columns)
print()

# What is the name of 105th column?
print("What is the name of 105th column?")
print(food.columns[104])
print()

# What is the type of the observations of the 105th column?
print("What is the type of the observations of the 105th column?")
print(food[food.columns[104]].dtypes)
print()

# How is the dataset indexed?
print("How is the dataset indexed?")
print(food.index)
print()

# What is the product name of the 19th observation?
print("What is the product name of the 19th observation?")
print(food['product_name'].iloc[18])