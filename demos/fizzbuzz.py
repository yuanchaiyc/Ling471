# The following is a classic problem which is sometimes still asked in programming intervies!

'''
Specification:

Iterate over numbers from 1 to 100.
At each step: 
If the number is divisible by 3, print "fizz".
If the number is divisible by 5, print "buzz".
If the number is divisible by 3 and 5, print "fizzbuzz".
Otherwise, print out the number itself.
'''

# range means: [1,2,3,4...100] (101 is not included!)
for x in range(1, 101):
    # % is the "modulo" operator. 3/3 remainder: is 0 4/3 remainder: is 1, etc.
    # So, x % 3 == 0 means: x is divisible by 3.
    if (x % 3 == 0 and x % 5 == 0):
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)
