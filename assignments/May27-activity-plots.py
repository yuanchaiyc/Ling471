import matplotlib.pyplot as plt

# Example plot

X = range(-5, 5)  # Note the missing +5!
Y = [pow(x, 2) for x in X]

plt.plot(X, Y) plt.show()
plt.xlabel('X', color='fuchsia', fontweight='bold')
plt.ylabel('f(x)')
plt.plot(X, Y, 'o-', label='squared')
plt.legend(loc="upper left")

plt.savefig('figures/parabola.png')

