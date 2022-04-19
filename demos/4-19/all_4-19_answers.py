import math, statistics

##########################
# MODULES
##########################
print('----------modules----------')

a = -1 * math.pi

print(math.sin(a))
print(math.cos(a))
# this next one throws an error, so it is commented out
# print(math.sqrt(a))
print(math.sqrt(16))
print(math.pow(a, 2))
# this next one throws an error, so it is commented out
# print(math.log(a))
print(math.log(math.e)) # log is ln from math
print(math.floor(a))

nums = list(range(1, 11))
print(statistics.mean(nums))
print(statistics.median(nums))
print(statistics.stdev(nums))
print(sum(nums) / len(nums))

##########################
# REGEXES
##########################
import re

print('----------regexes----------')

s = 'The passcode is 8675309. Please remember it.'

# Extract just the passcode
print(re.findall(r'\d+', s))

# Change the passcode to 555-5555
print(re.sub(r'\d+', '555-5555', s))

# Extract all words that begin with "p"
print(re.findall(r'p\w+', s))

# Extract the first word of each sentence
print(re.findall(r'[A-Z]\w*', s))

# Delete the word "Please" and capitalize "remember" afterward
print(re.sub('Please r', 'R', s))

# Change each "." to "!"
# Here is what happens if you forget to escape the character:
print(re.sub('.', '!', s))

# Here is the correct version
print(re.sub(r'\.', '!', s))

##########################
# TOKENIZATION
##########################
print('----------tokenization----------')
import nltk
s = "Here's a sentence that involves contractions, punctuation, and an abbreviation such as \"Ph.D.\"."
print(nltk.tokenize.word_tokenize(s))
# This sentence seemed to be tokenized okay
s = 'This is a sentence that involves foreign words like jalapeño, a colloquialism like finna\', and a less common abbreviation like et al., etc.'
print(nltk.tokenize.word_tokenize(s))
# It mostly seemed to work here, but it separated the period from "etc.",
# when it probably should have duplicated it to indicate that there was
# "etc." and a period.

print('----------regex version----------')

# Regex based tokenization
s = "Here's a sentence that involves contractions, punctuation, and an abbreviation such as \"Ph.D.\"."
print(nltk.tokenize.regexp.wordpunct_tokenize(s))
# Didn't handle "Ph.D." very well, and "Here's" got broken up strangely
s = 'This is a sentence that involves foreign words like jalapeño, a colloquialism like finna\', and a less common abbreviation like et al., etc.'
print(nltk.tokenize.regexp.wordpunct_tokenize(s))
# The abbreviations also did not get tokenized very well here
# Of course, abbreviations are notorious for being one of the more
# difficult parts of tokenization