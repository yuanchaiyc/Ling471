__author__ = 'Yuan Chai'
# TODO: Corpus terminologies
# "The cat chases the cat that was chasing the mouse."
# Type:
# Token:
# Hapax legomenon:
# Wordform:
# Lemma:

# TODO: explore the corpus
#  Go to https://www.english-corpora.org and choose a corpus that seems interesting
#  Think about some phrases you are interested in (very new phrases may not appear)
#  Find five concordances of the words/phrases

import matplotlib.pyplot as plt
from collections import Counter
import numpy as np
import string
import re

# Load the text data
with open('janeeyre.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Preprocess the text
text = text.lower()
text = re.sub(f'[{re.escape(string.punctuation)}]', '', text)  # Remove punctuation
words = text.split()
word_counts = Counter(words)

# TODO: To draw a Zipf's law illustration graph,
#  The x-axis is the rank of the words (1, 2, 3, 4, 5, ...) --> This should be easy
#  The y-axis is the frequency count of each word, from largest to smallest
#  How to get these?

ranks = list(range(1, len(frequency) + 1))
#print(ranks)
# Plotting Zipf's Law
plt.figure(figsize=(7, 4))
plt.plot(ranks, frequency_sort, marker='o', linestyle='none')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Rank')
plt.ylabel('Frequency')
plt.title("Zipf's Law")
plt.grid(True)
plt.show()

# nltk

import nltk
# Download specific resources
nltk.download('webtext')
nltk.download('book')
nltk.download('gutenberg')
nltk.download('nps_chat')
nltk.download('inaugural')
nltk.download('reuters')
nltk.download('udhr')
nltk.download('genesis')

# import all books
from nltk.book import *

# get concordance
# see the context of the word
text1.concordance('whale')
text1.concordance('ship')

# see what words are used in a similar context to a target word
# similar() method identifies words in similar contexts (e.g. syntactic position)
text1.similar('whale')

# the common contexts between two words, num indicates how many contexts to output
text1.common_contexts(['ship', 'whale'], num=50)

# number of tokens in text
len(text1)

# unordered sequence of unique tokens from the text (types)
set(text1)

# number of unique types in a text
len(set(text1))

# count a specific token
text1.count('whale')

# normalized frequency
# the precentage of P(whale)
100 * text1.count('whale')/len(text1)

# list-like operations on nltk objects

# access by index
text1[100]

# slice
text1[100:200]

# get the count of 'whale'
text1.index('whale')

# counting frequency
freq_distr = FreqDist(text1)

# get all the vocabs
vocab = freq_distr.keys()

# get the frequency of specific word
freq_distr['whale']

# get hapaxes
freq_distr.hapaxes()

# get the token with the maximum frequency
freq_distr.max()

# TODO: In text2, find all words that occur more than 10 times;
#  organize the frequency dictionary from largest number to smallest number
#  Get rid of short functions words -- words that have a frequency larger than 10, and the length of word smaller than 4
#  Create a list of words that start with 'sh'
