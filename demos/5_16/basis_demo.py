#  %% Load packages and simulate data
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

HIDDEN_UNITS = 64
EPOCHS = 100

def f(x):
    return 3*(x-4)**3 + 2*x**2 + x + 4
x_in = np.linspace(0, 10, num=5000)
x = x_in.reshape(-1, 1)
y = f(x_in)
plt.plot(x_in, y)

# %% Train our network with 64 hidden units (64 sigmoids)
m = keras.Sequential()
m.add(keras.layers.Dense(HIDDEN_UNITS, activation='sigmoid', input_dim=1))
m.add(keras.layers.Dense(1, activation='linear'))
m.compile(optimizer='adam', loss='mse')
h = m.fit(x, y, epochs=EPOCHS, verbose=2)

# %% Plot loss over number of epochs of training
plt.plot(h.history['loss'])
plt.xlabel('Epoch number')
plt.ylabel('MSE training loss')

# %% Plot predicted values
plt.plot(x, y, label='Original function')
plt.plot(x, m.predict(x), label='Fitted function')
plt.xlabel('x')
plt.ylabel('yhat')
plt.legend()