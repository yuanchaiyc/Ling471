import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression


# Linear regression demo

X = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

# Want: y = 2x + 0 (m = 2, b = 0)
Y = [2*x for x in X]  # list comprehension
Y_2 = [x*x for x in X]
Y_3 = [x*x*x for x in X]
# for x in X:
#    Y.append(2*x)

# plt.plot(X,Y,color="red")
# plt.plot(X,Y_2,color="blue")
# plt.plot(X,Y_3,color="green")
# plt.show()
# The data: Distance needed for cars at different speeds to stop
data_url = 'https://raw.githubusercontent.com/cmdlinetips/data/master/cars.tsv'
cars = pd.read_csv(data_url, sep="\t")

print(cars.head())

print(cars.shape)

# cars['dist']
X = cars.dist.values
Y = cars.speed.values

plt.scatter(X, Y)
plt.xlabel('Distance to stop (ft)')
plt.ylabel('Speed (mph)')
# plt.show()

lr = LinearRegression()
X_matrix = [[x] for x in X]

lm = lr.fit(X_matrix, Y)

predictions = lm.predict(X_matrix)

plt.plot(X, predictions)
# plt.show()

# By the way, that's how you could do it without any package:

# Create a matrix where first column is all 1s and second column is our X data
# To use the linear algebra package, need to use the numpy,
# because the linear algebra backage expects a proper matrix.
# Could use pandas objects as well.

#X_matrix = np.vstack((np.ones(len(X)), X)).T

# Find our A matrix (the vector of parameters) by solving a matrix equation:
#best_parameters_for_regression = np.linalg.inv(X_matrix.T.dot(X_matrix)).dot(X_matrix.T).dot(Y)

# Prediction line: Multiply X by A, now that we know A:
#predictions = X_matrix.dot(best_parameters_for_regression)

#plt.plot(X, predictions)
# plt.show()
