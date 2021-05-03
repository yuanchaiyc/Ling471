## Exercise for May 4

### Summary

In this exercise, you will write a few lines of code to generate some data which will be be distributed normally. 
You will then visualize the data as a histogram and as the corresponding bell curve.

### Steps
1. Download (or copy and paste into a new VS Code project) the [python skeleton](May4.py).
2. Pip-install numpy package for python (in command line, type `pip install numpy`)
3. Pip-install mathplotlib package for python.
4. The numpy's `random` class has a method called `normal`. It accepts a mu, a sigma, and an integer signifying the number of data points, and returns a dataset of real numbers which follow a Gaussian distribution. Call that method on mu=0.5, sigma=0.1, and dataset size=1000. Store the return value in a varialbe. Note that the parameters of the `normal` method are not called mu and sigma; they are called `loc` and `scale` (and the dataset size is called `size`). You can pass the three arguments without names. Consult [the docs](https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html) as needed. 
5. The `mathplotlib.pyplot` package is for data visualization. It has a method named `hist` which creates a histogram of data. A histogram is a visualization which divides the data into "bins", and the bins are then displayed as bars. The `hist` method accepts an array of numbers (your dataset) and the number of bins. Pass it your dataset and ask for 20 bins (by passing 20 as the second argument). In addition, pass it a third optional argument called "normed", set to True. 
 
