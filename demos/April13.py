# This is a comment. This line won't be executed.
# Demo for April 8.

# Python does not require that you declare any functions or classes.
# You can just enter statements and the interpreter will execute them.

# This import statement is needed to be able to pass arguments to the main() function.
import sys

# Let's declare/define a function. It will add two integers and return the sum.


def computeSum(x, y):
    # z = x + y
    # return z
    return x+y

# We will also define a so-called main function.
# The main function is conventionally the point of entry for execution.
# This is true in most programming languages/conventions.


def main(argv):  # argv is the name of the list of arguments passed from the system
    print(argv[0])  # argv[0] is the program file name (including path)
    print(argv[1])
    res = computeSum(argv[1], argv[2])
    print(res)
    res = computeSum(int(argv[1]), int(argv[2]))
    print(res)


# The below code is needed so that this file can be used as a module.
# If we want to call our program from outside this window, in other words.

if __name__ == "__main__":
    main(sys.argv)
