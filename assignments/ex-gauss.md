## Exercise for May 4

### Summary

In this exercise, you will write a few lines of code to generate some data which will be be distributed normally. 
You will then visualize the data as a histogram and as the corresponding bell curve.

### Steps
1. Download (or copy and paste into a new VS Code project) the [python skeleton](../demos/May4-skeleton.py).
2. Pip-install numpy package for python (in command line, type `pip install numpy`)
3. Pip-install mathplotlib package for python.

4. The numpy's `random` class has a method called `normal`. It accepts a mu, a sigma, and an integer signifying the number of data points, and returns a dataset of real numbers which follow a Gaussian distribution. Call that method on mu=0.5, sigma=0.1, and dataset size=1000. Store the return value in a varialbe. Note that the parameters of the `normal` method are not called mu and sigma; they are called `loc` and `scale` (and the dataset size is called `size`). You can pass the three arguments without names. Consult [the docs](https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html) as needed. 

5. The `mathplotlib.pyplot` package is for data visualization. It has a method named `hist` which creates a histogram of data. A histogram is a visualization which divides the data into "bins", and the bins are then displayed as bars. The `hist` method accepts an array of numbers (your dataset) and the number of bins. Pass it your dataset and ask for 20 bins (by passing 20 as the second argument). In addition, pass it a third optional argument called "normed", set to True. This means your number values will be "normalized", which is to say they will be "scaled" so that the sum of all bars equals to one. (This is needed so that we can treat the results as a probability distribution.) The `hist` method has three return values. We don't care about the first and the third, we only need the second one, however we need to store all three in order to get the second one. Call the second one "bins", or something else meaningful. These values indicate how the data is divided into "bins" (specifically, what the bins' edges are on the x-axis).

6. Now we will draw the bell curve which best fits our histogram! `Mathplot.pyplot`'s `plot` method accepts two arguments: the data for the x-axis and the data for the y-axis. The y-axis, crucially, can be a function of the values to be plotted on the x-axis. You saw this in the demo where we drew a straight line. We will use your "bins" as your x-axis data. As for y-axis: look at the formula for the normal distribution and carefully write that formula using python arithmetic operators and parentheses. You will need the `-` (minus), the `*` (multiplication), `**` (for exponent), and the `/` (float division). Use parentheses correctly to group operands. Use `np.sqrt` for the square root and `np.pi` for pi. Use the same mu and sigma as you used to create the dataset. Pass whichever variables you used to store x and y to `plt.plot()`. There is no return value, but you need to additionally call `plt.show()` to display the plot.

    <img width="234" alt="Screen Shot 2021-05-03 at 3 38 21 PM" src="https://user-images.githubusercontent.com/10963114/116942234-153d3680-ac26-11eb-82fb-65a2414068d5.png">

Work this out in pieces; write out each term carefully, then combine the terms.
E.g. start with the square root of two pi. Can you write that? Now multiply that by sigma. Now, use that
as the denominator and divide 1 by this entire thing. Now, go for the exponent: do the numerator and the denominator separately,
now add a minus. Now pass this entire thing to np.exp(). Now multiply your first term by this term.
This is not easy to do but is a great exercise.


7. Admire the bell curve which fits the histogram!
 
