
if __name__ == '__main__':
    # Using a while loop, write code that will print the integers
    # from 1 up to and including 10
    i = 1
    while i <= 10:
        print(i)
        i += 1

    # Create a list of integers from 1 up to and including 5
    # and assign it to a variable
    a = [1, 2, 3, 4, 5]
    # Check if the number 10 is in it
    print(10 in a)

    # Using a for loop, write code that will print the integers
    # from 1 up to and including 10
    for i in range(1, 11):
        print(i)

    # Using a for loop, print out every character in the string 'ling471'
    for c in 'ling471':
        print(c)

    #Challenge: using a for loop over the string 'ling471', store index as key, and the corresponding character as value.
    #Hint: enumerate()
    #Output is {1:'l', 2:'i', 3:'n', 4: 'g', 5: '4', 6: '7', 8: '1'}
    dict_471 = {}
    for index, element in enumerate('ling471'):
        dict_471[index] = element
    print(dict_471)


    # Thinking activity: What would happen if you used “while True:” for a
    # while loop? What about “while False:” and “for x in []”?

    # while True:
    #     print('I am looping')

    while False:
        print('Is this true?')

    for x in []:
        print('What is for?')

    # Create an empty dict
    d = {}
    # Add the pair 'a':1 to it
    d['a'] = 1
    print(d)
    # Add the pair 1:'b' to it
    d[1] = 'b'
    print(d)
    # Check if 2 is in the dict
    print(2 in d)
    # Check if 'a' is in the dict
    print('a' in d)
    Increase the value of 'a' to 2
    d['a'] = 2
    print(d)

    # Using a for loop, modify an empty dict to have keys that are
    # the integers 1 up to and including 4 and values that are the
    # squares of the integers 1 up to and including 4
    # (that is, 12, 22, 32, 42)
    d = {}
    for x in range(1, 5):
        d[x] = x**2
    print(d)

    # Create a txt file with all lower case text and save it somewhere you can find
    # Read that txt file in with Python
    with open('lowercasetext.txt', 'r', encoding='utf-8') as f:
        s = f.read()
        
    # Change all the text to uppercase
    s_new = s.upper()
    
    # Write the txt file back out to a new file
    with open('uppercasetxt.txt', 'w', encoding='utf-8') as w:
        w.write(s_new)
