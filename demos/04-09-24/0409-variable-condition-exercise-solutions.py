if __name__ == '__main__':
# ----------------------------------------------------
    #Exercise 1
    # Write an expression for the following prose:
    # “Three plus two minus ten all divided by fifteen”
    (3+2-10)/15
    # On a new line, store the value of that expression in a variable
    # called “x”
    x = (3+2-10)/15
    
    # Assign the string 'hello' to a variable called “var”
    var = 'hello'
    
    # Print the result of the following expression:
    # “(3**2+4**2)**0.5” (without the quotation marks)
    print((3**2+4**2)**0.5)

#----------------------------------------------------
    # exercise 2
    # Create a list that includes the integers from 1-9
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # Print the fourth element from that list
    print(a[3])
    # Print the fourth and fifth element from that list using slicing
    print(a[3:5])
    # Set the last element to 10
    a[8] = 10
    # or
    a[-1] = 10

    # Create a string of the integers from 1-9
    s = '123456789'
    # Print the fourth character from that string
    print(s[3])
    # Print the fourth and fifth characters from that string using slicing
    print(s[3:5])
    # Print a string where the '9' is replaced with '10'
    print(s[:8] + '10')
    # or
    print(s[:-1] + '10')

#--------------------------------------------------
    #exercise 3
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