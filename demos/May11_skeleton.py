import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

# Matrix multiplication:
# Data

matrix1 = [(1, 1, 2),

           (0, 2, 1),

           (2, 0, 1)]

 

matrix2 = [(2, 0, 2),

           (1, 1, 1),

           (2, 2, 2)]


# Data structure options for creating dataframes: 1) list of lists (each list is a ROW)
# 2) dicts (each key is a column name, each value, which must be a list, is a row)
# Can also create a list of row/column names and pass it to the constructor.
# The index= parameter is for row names; the columns= parameter is for column names.

# Fruit pie sales exercise:

# TODO: Store the pie prices in a variable as a 1x3 matrix (vector):

matrix1 = 

# TODO: Store the sales records in a variable as a 3x4 matrix:

matrix2 = 

# TODO: convert to pandas dataframes. 
# Note: ideally, the indices of the first matrix should be the same 
# as the columns of the second. Then it will be easier to multiply :).

df1 = 
df2 = 

# Print out to check dimensions and indices/column names:

print("Matrix1:")

print(df1.to_string(index=True))

print("Dimension:")

print(df1.shape)


print("Matrix2:")

print(df2.to_string(index=True))

print("Dimension:")

print(df2.shape)

# Multiply the matrices. It is the dot() function:
result = df.dot(dataFrame2)

print("Matrix multiplication – resultant matrix:")

print(result.to_string(index=False))

print("Dimension of the resultant matrix:")

print(result.shape)

# The data: Distance needed for cars at different speeds to stop
data_url = 'https://raw.githubusercontent.com/cmdlinetips/data/master/cars.tsv'
