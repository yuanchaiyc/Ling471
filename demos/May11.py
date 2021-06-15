import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

# Dataframes: access
#cars = pd.read_csv("cars.txt")

# print(cars)

#more_cars = pd.read_csv("more_cars.txt")

# print(more_cars)
# Matrix multiplication:
# Data

#all_cars = pd.concat([cars,more_cars],ignore_index=True)

# print(all_cars['Year'])

# print(min(all_cars['Year'].to_string(index=False)))
# print(all_cars)


matrix1 = [(1, 1, 2),

           (0, 2, 1),

           (2, 0, 1)]


matrix2 = [(2, 0, 2),

           (1, 1, 1),

           (2, 2, 2)]

column_names = ['a', 'b', 'c']
row_names = ['d', 'e', 'f']

#df1 = pd.DataFrame(matrix1,columns=column_names,index=row_names)
df1 = pd.DataFrame(matrix1)

print('Matrix 1')
print(df1.to_string(index=True))
print()
df2 = pd.DataFrame(matrix2)
print('Matrix 2')
print(df2.to_string(index=False))

# "dot" = multiplication of matrices
result = df1.dot(df2)

print()
print('Result')
print(result.to_string(index=False))

# Data structure options for creating dataframes: 1) list of lists (each list is a ROW)
# 2) dicts (each key is a column name, each value, which must be a list, is a row)
# Can also create a list of row/column names and pass it to the constructor.
# The index= parameter is for row names; the columns= parameter is for column names.
# Example:
# d = {'A': [1,2,3], 'B': [10,20,30]}
# row_names = ['single', 'double']
# digits = pd.DataFrame(data=d,index=row_names)

# The exercise:

prices = [[3, 4, 2]]

fruit_types = ['apple', 'cherry', 'blueberry']
sales = {'Mon': [13, 8, 6], 'Tue': [9, 7, 4],
         'Wed': [7, 4, 0], 'Thu': [15, 6, 3]}


# Data loaded into pandas DataFrames

dataFrame1 = pd.DataFrame(data=prices, index=['price'], columns=fruit_types)

dataFrame2 = pd.DataFrame(data=sales, index=fruit_types)

print(dataFrame2.at['apple', 'Mon'])

print("Matrix1:")

print(dataFrame1.to_string(index=True))

print("Dimension:")

print(dataFrame1.shape)


print("Matrix2:")

print(dataFrame2.to_string(index=True))

print("Dimension:")

print(dataFrame2.shape)


# Multiply the matrices: Matrix1 and Matrix2

# If stored the prices vector incorrectly (vertically), need to transpose:

# X_t = dataFrame1.T

# print(X_t.shape)

# print(X_t.to_string(index=False))

# Otherwise just use the dataframe as is:

X_t = dataFrame1

result = X_t.dot(dataFrame2)


# Print the result of matrix multiplication

print("Matrix multiplication – resultant matrix:")

print(result.to_string(index=False))

print("Dimension of the resultant matrix:")

print(result.shape)
