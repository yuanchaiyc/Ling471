if __name__ == '__main__':
    # Fill in the code to do the following
    # 1. Set x to be a non-negative integer (no decimals, no negatives)
    # 2. If x is divisible by 3, print 'Fizz'
    # 3. If x is divisible by 5, print 'Buzz'
    # 4. If x is divisible by both 3 and 5, print 'FizzBuzz'
    # 5. If x is divisible by neither 3 nor 5, do not print anything
    #
    # How to check if a number is divisble by another number?
    # Use modulus division! Modulus division tells you what the
    # remainder is after you do as many divisions as you can. It is performed
    # with the % operator.
    #
    # For example, 7 / 4 = 1 with 3 remaining. Modulus division will return
    # 3 for this example, that is, 7 % 4, will return 3. If a number is x is
    # divisible by another number y, x % y will be 0. So, 4 % 2 = 0.

    # Change assignment here
    x = 15

    # Insert conditional(s) here

    # A straightforward, readable solution
    if x % 3 == 0 and x % 5 == 0:
        print('FizzBuzz')
    elif x % 5 == 0:
        print('Fizz')
    elif x % 3 == 0:
        print('Buzz')

    # An example of something clever that you should consider not writing:
    # s = 'Fizz' * (x % 5 == 0) + 'Buzz' * (x % 3 == 0) + '\n' * (x % 5 == 0 or x % 3 == 0)
    # print(s, end='')