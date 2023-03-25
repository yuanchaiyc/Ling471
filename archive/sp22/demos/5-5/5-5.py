# Copyright 2021 Olga Zamaraeva
# Reproduced with permission
import pandas as pd

# Create a dataframe from a list
flowers_list = ['iris', 'rose', 'lilac', 'jasmine']
flowers_df = pd.DataFrame(flowers_list)

shape = flowers_df.shape
print(flowers_df)


# Create a dataframe from a dict

cars = {'Make': ['Honda', 'Toyota', 'Bugatti'], 'Year': [2000, 2020, 1999]}

cars_df = pd.DataFrame(cars)

print(cars_df)

# Create a dataframe from list of lists

# review_vec had a label and a text
# ["Positive", "good good good"]

fruit_sales = [['apples', 20], ['oranges', 30], [
    'oranges', 15], ['oranges', 5], ['apples', 25]]

column_names = ['type', 'kilos']

fruit_df = pd.DataFrame(data=fruit_sales, columns=column_names)

print(fruit_df)

# Reading from a csv file, which shoul have the following form:
'''
Make,Year
Toyota,1999
Honda,2010
Bugatti,1990
'''


cars1 = pd.read_csv("cars.csv")
print(cars1)

# Creating a csv file
fruit_df.to_csv("fruit.csv")
