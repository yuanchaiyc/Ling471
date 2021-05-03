import numpy as np
import matplotlib.pyplot as plt

# Set variables for mean and standard deviation. Store 0.5 as mu and 0.1 as sigma

mu, sigma = 0.5, 0.1

# Call np.random.normal() on mu, sigma, and number of datapoints equal to 1000
data = np.random.normal()  # Pass correct arguments!

# Call plt.hist() on the return value of np.random.normal(), request 30 bars ("bins", in hist()'s docs),
# and normalize the data (normed=True).
# There will be three return values; capture all of them but we will only need the second one.
# Call it e.g. "x_data". Those are the sample values we will want to plot on the x-axis.

dont_care1, x_data, dont_care2 = plt.hist()  # Pass correct arguments!

# Specify the formula for the y-axis. The value for you "y_data" (or whatever you like to call it)
# is the function of x (your "bins", or "x_data", or whatever you called it). Specifically, it is the Gaussian function.
# Carefully write it using the appropriate math operators for python and grouping things by parentheses.
# Use np.exp() for exponent (where the exponent is complex and not just an integer); use np.pi for the constnat pi,
# and use np.sqrt() for the square root (you pass the sqrt() function whatever you want the square root of).

# y_data =  # Uncomment when done

# Plot the distribution curve
# plt.plot(x_data, y_data) # Uncomment when done

# Uncomment the following line to actually see the plot!
# plt.show() # Uncomment when done
