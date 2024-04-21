# Codes on the slides and activity skeleton
#demonstrating the mutable and immutable of string and list
a = [1, 2, 3]
a[0] = 3
b = 'hello'
#b[1] = 'a'

#demonstrating single operators
a = 10
b = 5
-b #negative operator
b += 1 # increment by 1
a>b #True
not(a > b) #False (not True)

# ----------------------------------------------
# Programming activity 1
# Write an expression for the following prose:
# “Three plus two minus ten all divided by fifteen”
# On a new line, store the value of that expression in a variable called “x”
# Assign the string 'hello' to a variable called “var”
# Print the result of the following expression:
# (3**2+4**2)**0.5 (without the quotation marks)
# ----------------------------------------------


#list
a = [1, 2, 3]
a[0] # 1
a[1] # 2
a[2] # 3

a = [0, 1, 2, 3]
# Useful:
a[0:2] # [0, 1]
a[0:3] # [0, 1, 2]
a[1:3] # [1, 2]
a[1:] # [1, 2, 3]
a[:3] # [0, 1, 2]
# Harder to understand:
a[:-1] # [0, 1, 2]
a[:-2] # [0, 1]

#----------------------------------------------
# Programming activity 2
# Create a list that includes the integers from 1-9
# Print the fourth element from that list
# Print the fourth and fifth element from that list using slicing
# Set the last element to 10
# Create a string of the integers from 1-9
# Perform the same actions as for the list
# You will have to make a new string using concatenation instead of setting the last element
#----------------------------------------------

# Conditions
a = 19
b = 11
c = 10
d = 9
if (a>b) and (c>d) :
    print('a and c are larger than b and d')

#relational operator
3 <= 2
3 != 2
3 == 3
3 == 2
3 != 2
3 != 3
3 > 2
2 > 3
3 >= 2
2 >= 3
2 <= 3
3 >= 2

#logical operator
(3 > 2) and (3 < 5)
(3 > 2) & (3 < 5)
(3 > 2) and (3 > 5)
(3 > 2) or (3 > 5)
(3 > 2) | (3 > 5)
not(3 > 2)

(2 < 3) and (5 > 2) # true
(3 < 2) and (2 > 5) # false

(3 > 2) or (3 > 4) # true
(3 < 2) or (3 > 4) # false

x = 0
if x > 0:
    print('+')
elif x < 0:
    print('-')
else:
    print('0')


# ----------------------------------------------
# Programming activity 3
# This activity is called “FizzBuzz”; see skeleton in the demo file
# Write a program that does the following:
# Set a variable “x” to be a number
# If “x” is divisible by 5, print “Fizz”
# If “x” is divisible by 3, print “Buzz”
# If “x” is divisible by 3 and 5, print “FizzBuzz”
# If “x” is not divisible by either 3 or 5, do not print anything

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


# An example of something clever and much shorter, but much less readable:
# s = 'Fizz' * (x % 5 == 0) + 'Buzz' * (x % 3 == 0) + '\n' * (x % 5 == 0 or x % 3 == 0)
# print(s, end='')