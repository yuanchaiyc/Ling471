# This code is mostly from here: https://thedatafrog.com/en/articles/word-embedding-sentiment-analysis/
# Adapted for Ling471 by Olga Zamaraeva
# May 2021

import matplotlib.pyplot as plt
import os
import math
# you must install tensorflow version 2.5.0 or later if you have not already done so
import tensorflow as tf
from tensorflow import keras
import numpy as np
from numpy.random import seed
# DEADBEEF is a famous hexadecimal number :). See here: https://en.wikipedia.org/wiki/Deadbeef
seed(0xdeadbeef)
# In order to minimize randomness where we can, we will tell numpy and tensorflow to always start in the same place.
tf.random.set_seed(0xdeadbeef)


def plot_review(idx):
    # plot the distribution of points
    enc_words = test_data[idx]
    emb_words = get_embed_out([enc_words])[0]
    plt.figure(figsize=(8, 8))
    plt.scatter(emb_words[:, 0], emb_words[:, 1])
    # use the label as title: 1 is positive,
    # 0 is negative
    plt.title(test_labels[idx])
    # for words that are far enough from (0,0),
    # print the word
    for i, (enc_word, emb_word) in enumerate(zip(enc_words, emb_words)):
        word = index[enc_word]
        x, y = emb_word
        if math.sqrt(x**2 + y**2) > 0.2:
            plt.annotate(word, (x, y))
    # fix the range in x and y to be able to compare
    # the distributions of different reviews
    axes = plt.gca()
    axes.set_xlim([-0.5, 0.5])
    axes.set_ylim([-0.5, 0.5])
    axes.set_aspect('equal', adjustable='box')
    plt.savefig('Review{}.png'.format(idx))


def decode_review(text):
    '''converts encoded text to human readable form.
    each integer in the text is looked up in the index, and 
    replaced by the corresponding word.
    '''
    return ' '.join([index.get(i, '?') for i in text])


def plot_accuracy(history, miny=None):
    acc = history.history['accuracy']
    test_acc = history.history['val_accuracy']
    epochs = range(len(acc))
    plt.plot(epochs, acc)
    plt.plot(epochs, test_acc)
    if miny:
        plt.ylim(miny, 1.0)
    plt.title('accuracy')
    plt.xlabel('epoch')
    plt.savefig('accuracy.png')


# Another version of the familiar dataset. It is not a pandas object but a keras object.
imdb = keras.datasets.imdb
num_words = 20000
(train_data, train_labels), (test_data, test_labels) = imdb.load_data(
    seed=1, num_words=num_words)

# print(train_data[0])
# print('label:', train_labels[0])

# A dictionary mapping words to an integer index
vocabulary = imdb.get_word_index()
# The first indices are reserved
vocabulary = {k: (v+3) for k, v in vocabulary.items()}
# Smoothing and n-gram support.
vocabulary["<PAD>"] = 0
vocabulary["<START>"] = 1
vocabulary["<UNK>"] = 2  # unknown
vocabulary["<UNUSED>"] = 3

# reversing the vocabulary.
# in the index, the key is an integer,
# and the value is the corresponding word.
index = dict([(value, key) for (key, value) in vocabulary.items()])

# print(decode_review(train_data[0]))


train_data = keras.preprocessing.sequence.pad_sequences(train_data,
                                                        value=vocabulary["<PAD>"],
                                                        padding='post',
                                                        maxlen=256)

test_data = keras.preprocessing.sequence.pad_sequences(test_data,
                                                       value=vocabulary["<PAD>"],
                                                       padding='post',
                                                       maxlen=256)


# print(train_data[1])

model = keras.Sequential()

# the first layer is the embedding layer.
# we indicate the number of possible words,
# the dimension of the embedding space,
# and the maximum size of the text.
model.add(keras.layers.Embedding(len(vocabulary), 2, input_length=256))

# the output of the embedding is multidimensional,
# with shape (256, 2)
# for each word, we obtain two values,
# the x and y coordinates
# we flatten this output to be able to
# use it in a dense layer
model.add(keras.layers.Flatten())

# dropout regularization
model.add(keras.layers.Dropout(rate=0.5))

# small dense layer. It's role is to analyze
# the distribution of points from embedding
model.add(keras.layers.Dense(5))

# final neuron, with sigmoid (similar to logistic function) activation
# for binary classification
model.add(keras.layers.Dense(1, activation='sigmoid'))

# print(model.summary())

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

history = model.fit(train_data,
                    train_labels,
                    epochs=5,
                    batch_size=100,
                    validation_data=(test_data, test_labels),
                    verbose=1)

plot_accuracy(history)

# This code will return a resulting embedding given X and Y coordinates of a word.
# We mapped words to 2D!
get_embed_out = keras.backend.function(
    [model.layers[0].input],
    [model.layers[1].output])

layer_output = get_embed_out(test_data[0])

#print(type(layer_output), len(layer_output), layer_output[0].shape)

words = layer_output[0]
plt.cla()
# [:,0] is so called "slicing" notation in python.
# It means the first column in a matrix, so, all rows in column 0.
plt.scatter(words[:, 0], words[:, 1])
plt.savefig('words.png')

# Plot reviews number 15 and 17:
plot_review(15)
plot_review(17)


# A fake/dummy "test" review. We assume we've seen most of these words in training!
review = ['great', 'brilliant', 'crap', 'bad',
          'fantastic', 'movie', 'seagal']

# Use our pretrained encodings to get an encoding for this unseen review:
enc_review = tf.constant([vocabulary[word] for word in review])
# print(enc_review)
words = get_embed_out([enc_review])[0]
plt.cla()  # clear the previous plot "canvas"
plt.scatter(words[:, 0], words[:, 1])

# The loop will annotate each point in the 2D plot.
# Note the enumerate() function; it is very convenient.
# It returnes a tuple: an object from the list as well as its index in the list.
# So, at the first iteration txt will be "great" and i will be 0,
# because "great" is the first word in our review.
for i, txt in enumerate(review):
    plt.annotate(txt, (words[i, 0], words[i, 1]), ha='center')
plt.savefig('my_review1.png')

# TODO: Write your own "review" similar to above, with some words which interest you,
# how they will map out in the vector space that you trained on IMDB.
# Then uncomment the remaining code and observe what happens.
my_review = []
# enc_review = tf.constant([vocabulary[word] for word in my_review])
# # print(enc_review)
# words = get_embed_out([enc_review])[0]
# plt.cla()  # clear the previous plot "canvas"
# plt.scatter(words[:, 0], words[:, 1])
# for i, txt in enumerate(review):
#     plt.annotate(txt, (words[i, 0], words[i, 1]), ha='center')
# plt.savefig('my_review2.png')
