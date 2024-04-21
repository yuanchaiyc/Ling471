
if __name__ == '__main__':
    #for loop
    for pancake in range(0, 10):  # Starts from 1 and goes up to but not including 11
        print("I'm cooking pancake No. ", pancake)

    #while loop
    pancake = 1
    hungry_guests = True
    while hungry_guests:
        print("I'm cooking pancake No. ", pancake)
        pancake += 1
        #soliciting input from the user
        response = input("Are there still hungry guests? (yes/no): ").lower()
        if response == "yes":
            hungry_guests = True
        elif response == "no":
            hungry_guests = False
        else:
            break


    a = 1
    while a <= 10:
        print(a)
        a += 1

    a = [1,2,3,4]
    for x in a:
        print(x)

    for x in range(1,5):
        print(x)

    for x in range(len(a)):
        a[x] = a[x]*2

    a = ["a", "b", "c"]
    i = 0
    while i < len(a):
        print(a[i])
        i += 1

    a = ["a", "b", "c"]
    for i in a:
        print(i)


    #while loop
    def square(num):
        return num * num
    while True:
        user_num = float(input("Give me a number: "))
        number = square(user_num)
        print(square(user_num))

    #iterator
    a = [1, 2, 3, 4]
    iterator = iter(a)
    next(iterator)
    next(iterator)
    next(iterator)
    next(iterator)
    next(iterator)

    #range
    range(5)
    range(1, 5)
    range(1, 5, 2)

    #list vs range
    my_list = [1, 2, 3, 4, 5]
    for index, item in enumerate(my_list):
        print(index,item)

    for item in range(1, 6):
        print(item)

#-------------------------
#Programming activity 1
    # Using a for loop, write code that will print the integers
    # from 1 up to and including 10

    # Create a list of integers from 1 up to and including 5
    # and assign it to a variable
    # Check if the number 10 is in it

    # Using a for loop, write code that will print the integers
    # from 1 up to and including 10

    # Using a for loop, print out every character in the string 'ling471'

    # Thinking activity: What would happen if you used “while True:” for a
    # while loop? What about “while False:” and “for x in []”?
#---------------------------------

    #dictionary
    food_type = {'pinto':'bean', 'banana':'fruit', 'rice':'grain'}
    word_counts = {'the': 10, 'brown': 4, 'dog':2}
    bad_dogs = {}
    word_counts['the']
    word_counts['brown']
    word_counts[10]

    #modify the value of a key; add new key to dictionary
    word_counts['the'] = 11
    word_counts['hello'] = 1

    #check membership in a dict
    word_counts = {'the': 10, 'brown': 4, 'dog': 2}
    'dog' in word_counts  # True
    'pig' in word_counts  # False

#----------------------------------------
#Programming activity 2
    # Create an empty dict
    # Add the pair 'a':1 into it
    # Add the pair 1:'b' to it
    # Check if 2 is in the dict
    # Check if 'a' is in the dict
    # increase the value of 'a' to 2

    # Using a for loop, modify an empty dict to have keys
    # that are the integers 1 up to and including 4
    # and values that are the squares of the integers 1 up to and including 4
    # The output should be: {1:1,2:4,3:9,4:16}

    #Challenge: using a for loop over the string 'ling471', store index as key, and the corresponding character as value.
    #Hint: enumerate()
    #Output is {1:'l', 2:'i', 3:'n', 4: 'g', 5: '4', 6: '7', 8: '1'}
#----------------------------------------

    #string methods]
    s = 'abcdefg'
    #convert to uppercase
    s.upper()
    #split sentence into words
    s = 'here are some words'
    s.split()  # ['here', 'are', 'some', 'words’]
    #remove extra spaces
    s = '  there is extra space here '
    s.strip()  # 'there is extra space here'
    #join list of word into a string by comma
    ', '.join(['Smith', 'Janet', 'student'])  # 'Smith, Janet, student'

    #list methods
    a = [1, 2, 3, 5]
    #append item to list
    a.append(4)  # a == [1, 2, 3, 5, 4]
    #remove item by index
    a.pop(0)  # a == [2, 3, 5]
    #remove item by value (if multiple, remove the first occurance)
    a.remove(5)  # a == [2, 3]

    a = [3, 1, 2]
    #sort in ascending order
    a.sort()  # a == [1, 2, 3# ]
    #sort in descending order
    a.sort(reverse=True)  # a == [3, 2, 1]
    a = [1, 2, 4]
    #insert an element
    a.insert(2, 3)  # a == [1, 2, 3, 4]
    a = [1, 1, 1, 2, 1, 3, 1]
    #count how many 1s are there in the list
    a.count(1)  # 5

#-----------------------------------------------
#Programming activity 3
    # Read the txt file lowercase.txt, which is written in lower case text. Save it somewhere you can find
    # Change all characters into upper case
    # Write the txt file into a new file called uppercase.txt
