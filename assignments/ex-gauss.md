## Exercise for May 4

### Summary

In this exercise, you will write a few lines of code to generate some data which will be be distributed normally. 
You will then visualize the data as a histogram and as the corresponding bell curve.

Pick one person to share their screen and work together. You can change who shares the screen as you go.

### Steps
1. Download (or copy and paste into a new VS Code project) the [python skeleton](../demos/May4-skeleton.py).
2. Pip-install the `numpy` package for python (in command line, type `pip install numpy`)
3. Pip-install the `mathplotlib` package for python.
4. If one of these won't install or you can't import it, engage with others on a consulting level; all people don't have to be coding at the same time.
5. Follow the comments in the skeleton. The formula for the Gaussian distribution is:

    <img width="234" alt="Screen Shot 2021-05-03 at 3 38 21 PM" src="https://user-images.githubusercontent.com/10963114/116942234-153d3680-ac26-11eb-82fb-65a2414068d5.png">

    Work this out in pieces; write out each term carefully, then combine the terms. E.g. start with the square root of two pi. Can you write that? Now multiply that by sigma. Now, use that as the denominator and divide 1 by this entire thing. Now, go for the exponent: do the numerator and the denominator separately, now add a minus. Now pass this entire thing to np.exp(). Now multiply your first term by this term. This is not easy to do but is a great exercise.


8. Admire the bell curve which fits the histogram!
 
