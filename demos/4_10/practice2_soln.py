if __name__ == '__main__':
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

    
