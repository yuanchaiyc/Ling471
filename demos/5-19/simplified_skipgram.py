#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tensorflow import keras
import numpy as np
import nltk
from copy import deepcopy
from scipy.spatial import distance


# In[2]:


text = 'Once upon a time, there lived two monarchs. The king sat on a throne. Also, the queen sat on a throne. Together, they both were seated on thrones.'
NGRAM_LIMIT = 10000
tokens = nltk.tokenize.word_tokenize(text)
tokens_lc = [x.lower() for x in tokens]
INDEXES = {x: i for i, x in enumerate(sorted(set(tokens_lc)))}
REV_INDEXES = {x: i for i, x in INDEXES.items()}
bigrams = list(nltk.bigrams(tokens_lc))
bigrams = bigrams[:min(len(bigrams), NGRAM_LIMIT)]


# In[3]:


x_text = [w1 for w1, w2 in bigrams]
y_text = [w2 for w1, w2 in bigrams]

x_num = [INDEXES[x] for x in x_text]
y_num = [INDEXES[y] for y in y_text]

X = keras.utils.to_categorical(x_num, num_classes=len(INDEXES))
y = keras.utils.to_categorical(y_num, num_classes=len(INDEXES))


# In[4]:


m = keras.models.Sequential()
m.add(keras.layers.Dense(64, activation='relu', input_dim=len(INDEXES)))
m.add(keras.layers.Dense(32, activation='relu'))
m.add(keras.layers.Dense(len(INDEXES), activation='softmax'))
m.compile(optimizer='adam', loss='categorical_crossentropy', metrics='acc')
m.summary()
m.fit(X, y, epochs=100)


# In[5]:


newmod = keras.models.clone_model(m)
newmod.pop() # Remove last layer


# In[6]:


def get_vector(word):
    i = INDEXES[word]
    onehot = keras.utils.to_categorical([i], num_classes=len(INDEXES))
    return newmod.predict(onehot)


# In[7]:


print(get_vector('queen'))


# In[8]:


print(get_vector('king'))

