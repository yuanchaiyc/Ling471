import numpy as np
import matplotlib.pyplot as plt

# Earlier demo of numpy and matplotlib:

# print(np.sqrt(4))
# print(np.pi)
# print(np.exp(1))
# data = [1,2,3,4,5]
# x_axis = np.array(data)
# y_axis = 2*x_axis

# plt.plot(x_axis,y_axis)

#plt.show() 

# Set variables for mean and standard deviation. Store 0.5 as mu and 0.1 as sigma

mu, sigma = 0.5, 0.1

# Call np.random.normal() on mu, sigma, and number of datapoints equal to 1000
data = np.random.normal(mu, sigma, 1000)

# Call plt.hist() on the return value of np.random.normal(), request 30 bars ("bins", in hist()'s docs),
# and normalize the data (normed=True).
# There will be three return values; capture all of them but we will only need the second one.
# Call it e.g. "x_data". Those are the sample values we will want to plot on the x-axis.

dont_care1, x_data, dont_care2 = plt.hist(data, 30, denisity=True) # "density" was called "normed" in earlier versions of python

# Specify the formula for the y-axis. The value for you "y_data" (or whatever you like to call it)
# is the function of x (your "bins", or "x_data", or whatever you called it). Specifically, it is the Gaussian function.
# Carefully write it using the appropriate math operators for python and grouping things by parentheses.
# Use np.exp() for the exponent (e; for example: np.exp(2) is e to the power of 2);
# use np.pi for the constnat pi;
# and use np.sqrt() for the square root (you pass the sqrt() function whatever you want the square root of;
# for example: np.sqrt(4) will return 2).
# Work this out in pieces; write out each term carefully, then combine the terms.
# E.g. start with the square root of two pi. Can you write that? Now multiply that by sigma. Now, use that
# as the denominator and divide 1 by this entire thing. Now, go for the exponent: do the numerator and the denominator separately,
# now add a minus. Now pass this entire thing to np.exp(). Now multiply your first term by this term.
# This is not easy to do but is a great exercise.
y_data = 1/(sigma * np.sqrt(2 * np.pi)) * \
    np.exp(- (x_data - mu)**2 / (2 * sigma**2))


# Plot the distribution curve
plt.plot(x_data, y_data)

# Uncomment the following line to actually see the plot!
plt.show()

# x_data = np.array([1,2,3,4,5])
# y_data = 2*x_data

# print(np.exp(1))
# print(np.pi)
# print(np.sqrt(4))