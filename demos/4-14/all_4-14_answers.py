# Using a while loop, write code that will print the integers from 1 up to and including 10
a = 1
while a <= 10:
    print(a)
    a = a + 1

# Create a list of integers from 1 up to and including 5 and assign it to a variable
a = [1, 2, 3, 4, 5]
# Check if the number 10 is in it
10 in a

# Using a for loop, write code that will print the integers from 1 up to and including 10
for i in range(1, 11):
    print(i)
    
# Using a for loop, print out every character in the string 'ling471'
for c in 'ling471':
    print(c)
    
# Remove the next lines out to try a while True: loop
#while True:
    #print('hi')
    
# Trying out a while False: loop
while False:
    print('hi')
    
# Trying out a for loop on an empty list
for x in []:
    print('hi')
    
# Create an empty dict
d = {}

# Add the pair 'a':1 to it
d['a'] = 1

# Add the pair 1:'b' to it
d[1] = 'b'

# Check if 2 is in the dict
2 in d

# Check if 'a' is in the dict
'a' in d

# Increase the value of 'a' to 2
d['a'] = 2

# Using a for loop, modify an empty dict to have keys that are the integers 1 up to and including 4 and values that are the squares of the integers 1 up to and including 4 (that is, 1^2, 2^2, 3^2, 4^2)
d = {}
for i in range(1, 5):
    d[i] = i**2

# Create a txt file with all lower case text and save it somewhere you can find
#   See 'samplefile.txt'

s = ''

# Read that txt file in with Python
with open('samplefile.txt', 'r') as f:
    s = f.read()

# Change all the text to uppercase
s = s.upper()    

# Write the txt file back out to a new file
with open('sampleout.txt', 'w') as f:
    f.write(s)