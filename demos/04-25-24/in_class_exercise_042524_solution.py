__author__ = 'Yuan Chai'
import random
#-------------------------------------
# Programming acitivity 1

# Using the random module, flip some coins
# Assume 0 is tails and 1 is heads

# TODO: Use random.choices(),
#  Flip 1,000 coins and count how many heads or tails your get, Calculate the probability of getting heads and tails
#  Flip 1,000 more and compare your results, Calculate the probability of getting heads and tails
def flip(relevant_class, num_observation):
    n_H = sum(random.choices([0,1])[0] == relevant_class for flip in range(num_observation))
    probability = n_H/num_oberservation
    return probability

flip(1, 1000)
flip(1, 1000)


# TODO: If you have more time, for a challenge:
# create an unfair coin,
# i.e., one where heads and tails are not equally probable
# Hint: Give more options to random.choices
# and rethink what numbers correspond to heads and tails

#This is a coin that P(H) = 0.1; P(T) = 0.9
n_h = sum(x >= 1 for x in rand.choices(range(10), k=n))
print(n_h / n)

#-------------------------------------
# Programming acitivity 2
# TODO: Write a for loop to approximate the value of θ that maximizes P(D) = {HHHTT}
#  Think about how to loop over evenly-spaced numbers between 0 to 1
#  Then loop over the numbers and calculate the value of θ^3 * (1-θ)^2
#  Then compare the product with the existing highest P(D) value to update the smallest value
#  Feel free to come up with your own numerical approximation method

curr_max_p = 0
curr_max_x = 0
for x in range(0, 1000, 1):
    x /= 1000
    p = x ** 3 * (1 - x) ** 2
    if p > curr_max_p:
        curr_max_p = p
        curr_max_x = x
print(f'value of theta: {curr_max_x}, p: {curr_max_p}')

#OR

for i in range(0,10000):
    x = random.random()
    p = x ** 3 * (1 - x) ** 2
    if p > curr_max_p:
        curr_max_p = p
        curr_max_x = x
print(f'value of theta: {curr_max_x}, p: {curr_max_p}')


from scipy.optimize import minimize_scalar


import sympy as sp
# Define the symbol
x = sp.Symbol('x')
# Define the function
f = x**3 * (1 - x)**2
# Take the derivative
f_prime = sp.diff(f, x)
# Solve for critical points
critical_points = sp.solve(f_prime, x)
# Evaluate the function at critical points and endpoints
values = [f.subs(x, point) for point in critical_points + [0, 1]]
# Find the maximum value and its corresponding x
max_value = max(values)
arg_max_x = critical_points[values.index(max_value)]
print("Arg max x:", arg_max_x)
print("Maximum value:", max_value)