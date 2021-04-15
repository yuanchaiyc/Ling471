# Loops
import string
# Infinite loops

#x = 3

# while x in [1, 2, 3]:
#    print(x)

# while x < 4:
#     print(x)
#     #x = x + 1
#     x += 1  # this line means the same as the one above; special syntax

# For-loops
for x in [1, 2, 3]:
    print(x)

# Dicts and counting
# Count characters in a word

'''
The function below takes a word as argument and counts characters in it.
The counts are returned as a new dictionary.
'''


def countChars(word):
    # print(word)
    counts = {}
    for c in word:
        # 1. check if there is already an entry for c
        if not c in counts:
            # Initialize the entry for c,
            # only if c is not yet in the dictionary
            counts[c] = 0
        # increment the count OUTSIDE the if scope.
        # This means, the count will be incremented at every step of the loop,
        # regardless of whether the if condition is true.
        counts[c] += 1
    return counts


'''
The function below takes a word AND a dict as arguments.
It counts characters in the word and UPDATES the passed dict with those counts.
It does not need to return anything.
'''


def countCharsManyWords(word, d):
    for c in word:
        if not c in d:
            d[c] = 0
        d[c] += 1


# Calling the first function.
# #my_counts = countChars("apple")
my_counts = {}
wordlist = ["apple", "banana"]

# Calling the second function on every word in the list.
for w in wordlist:
    countCharsManyWords(w, my_counts)


# Formatting output

# What if I want to know, for each letter of the alphabet,
# how many times it was found in the text (represented by my worldlist in this case).
# string.ascii_lowercase contains the english alphabet;
# it is a constant available through the "string" module.
# I imported the module at the beginning of the file.
# Try:
print(string.ascii_lowercase)
for c in string.ascii_lowercase:
    if c in my_counts:
        # "naive" formatting of the output:
        #print("The count for " + c + " is " + str(my_counts[c]))
        # more elegant formatting of the output
        print("The count for {} is {}".format(c, my_counts[c]))

# Opening files for reading

# A given filepath; you won't have it on your machine.
filepath = "/Users/olzama/Teaching/Ling471/datasets/IMDB/aclImdb/train/pos/296_10.txt"

# On Windows, need to replace backslashes by double backslashes,
# otherwise python gets confused because for python, \ is a special character.
windows_filepath = "C:\\Users\\olzama\\Teaching\\Ling471\\filename.txt"
# with keyword makes sure file is closed automatically
with open(filepath, 'r', encoding="utf8") as f:
    text = f.read()

print(text)

# Stop the debugger here if you don't want to exit the program after the previous statement,
# e.g. to observe the previous statement's effect.
print("bye")
