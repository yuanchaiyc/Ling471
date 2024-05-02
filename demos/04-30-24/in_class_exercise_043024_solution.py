import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.special import erf

def normal_pdf(x, mu, sigma):
    # mu: the mean
    # sigma: the standard deviation
    # square root: np.sqrt()
    # exponent of e: np.exp()
    # coefficient = None
    # exponent = None

    coefficient = 1 / (sigma * np.sqrt(2 * np.pi))
    exponent = -0.5 * ((x - mu) / sigma) ** 2
    return coefficient * np.exp(exponent)

def normal_cdf(x, mu, sigma):
    return 0.5 * (1 + erf((x - mu) / (sigma * np.sqrt(2))))

# Calculate the probability within 1 sd of the mean
prob_within_one_sd = normal_cdf(1, 0, 1) - normal_cdf(-1, 0, 1)

# Calculate the probability within 2 sd of the mean
prob_within_two_sd = normal_cdf(2, 0, 1) - normal_cdf(-2, 0, 1)

# Calculate the probability within 3 sd of the mean
prob_within_three_sd = normal_cdf(3, 0, 1) - normal_cdf(-3, 0, 1)

print(prob_within_one_sd)
print(prob_within_two_sd)
print(prob_within_three_sd)

x_data = np.linspace(-5, 5, 1000)

y_data_pdf = normal_pdf(x_data, 0, 1)

y_data_cdf = normal_cdf(x_data, 0, 1)

# Plot pdf
plt.plot(x_data, y_data_pdf)
# Plot cdf
plt.plot(x_data, y_data_cdf)
plt.show()