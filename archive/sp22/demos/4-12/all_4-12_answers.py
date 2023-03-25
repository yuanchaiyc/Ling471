# variables, assignment, expressions, and statements activity

# Write an expression for the following prose:
# "Three plus two minus ten all divided by fifteen"
(3 + 2 - 10) / 15

# On a new line, store the value of that expression in a variable called "x"
x = (3 + 2 - 10) / 15

# Assign the string 'hello' to a variable called "var"
var = 'hello'

# Print the result of the following expression:
# "(3**2+4**2)**0.5" (without the quotation marks)
print((3**2+4**2)**0.5)

# list activity

# Create a list that includes the integers from 1-9
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Print the fourth element from that list
print(my_list[3])
# Print the fourth and fifth element from that list using slicing
print(my_list[3:5])
# Set the last element to 10
my_list[-1] = 10

# string activity

# Create a string of the integers from 1-9
s = '123456789'
# Print the fourth character from that string
print(s[3])
# Print the fourth and fifth character from that string
print(s[3:5])
# Set the last element to 10
s = s[:-1] + '10'

# FizzBuzz solution
# using version from slides ("Fizz" for 5, "Buzz" for 3)

x = 9

if x % 3 == 0 and x % 5 == 0:
    print('FizzBuz')
elif x % 5 == 0:
    print('Fizz')
elif x % 3 == 0:
    print('Buzz')
    
# if you want, you could have
# else:
#   pass
# but that is not necessary