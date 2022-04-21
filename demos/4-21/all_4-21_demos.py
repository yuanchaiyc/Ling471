import math

###########################
# LIST COMPREHENSIONS
###########################

# Create a list from 0 up to and including 10000
a = [x for x in range(10001)]
print(a[:5])

# Create a list that squares all the numbers from the previous list
b = [x**2 for x in a]
## OR ##
b = [math.pow(x, 2) for x in a]
## OR ##
b = [pow(x, 2) for x in a]
print(b[:5])

# Create a list that only includes odd numbers from 0 up to and including 9877
c = [x for x in range(9878) if x % 2 != 0]
print(c[:5])
print(c[:-6:-1]) # print the last 5 elements

#  Create a list that has converted each word in the following string to lowercase: "tHIs iS A sENtENce thaT hAS miXeD cASe"
d = [x.lower() for x in 'tHIs iS A sENtENce thaT hAS miXeD cASe'.split()]
print(d[:5])

# Create a list that has called ord on the characters in the example string on the slide "Text data: Is Unicode enough?"
e = [ord(c) for c in 'The quick brown fox jumped over the lazy dog']
print(e[:5])
# Invert if you want
f = [chr(c) for c in e]
print(f[:5])

###########################
# GENERATOR COMPREHENSIONS
###########################

# Create a dict that maps all integers from 0 up to and including 10000 to their square roots
roots = {x : math.sqrt(x) for x in range(10001)}
print(roots[2], roots[16], roots[100])
# Can also use **, pow, or math.pow to raise to the power of 1/2 or 0.5

#  Sum the value of all even numbers from 0 up to and including 4578
print(sum(x for x in range(4579) if x % 2 == 0))
