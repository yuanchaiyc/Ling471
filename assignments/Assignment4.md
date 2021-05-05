# Assignment 4: Naive Bayes classifier

In this assignment, you will use a Naive Bayes classifier to classify the IMDB reviews. We will then compare its performance with the simplistic model we used in Assignment 3.

### Part 0: Clean up and refactoring
1. Address any comments you got for Assignment 3, if available, or otherwise make sure your metrics computation is working correctly.
2. Take all the code in your main() and put it in a new method/function (you can call it "runAllSimplePredictions()" or whatever you like). Comment out the call to this function in your main so all that procedure is out of the way for the moment.

### Part 1: Better clean up
1. Use the BeautifulSoup package to effortlessly get rid of HTML tags in the review texts and then furthermore lowercase all the words for more accurate counts. You can do that by calling: `BeautifulSoup(text,features="lxml").get_text().lower()`. Add this call in your CleanFileContents(), before you get rid of punctuation and extra spaces. Admire the result in the debugger!

### Part 2: Stopwords!
Counting words like `the` is usually not informative. We'll ignore them.
1. Install the NLTK module by `pip install nltk`. Import it in your assignment3.py
2. You can now access a list of English "stopwords": 
    `from nltk.corpus import stopwords`
    `stopwords_en = stopwords.words("english")`
4. Edit your tokenizer function to only count a word if it is **not** in the list of these stopwords.

### Part 2: Another vector representation

In Assignment 3, we had a class for review vectors. That can be convenient for debugging/thinking about the problem, but in actuality, people usually use simple tables to store data vectors. Such a table simply contains rows where one of the columns is the gold label. 

1. Install (via `pip`) and import (in your assignment4.py) the `pandas` module and the Beautiful Soup 4 module. The Beautiful Soup 4 module is installed by `pip install beautifulsoup4` and can be imported by `from bs4 import BeautifulSoup`.

2.  Store the data vectors as a **pandas dataframe** (see lecture). Use 1 and 0 for labels where 1 is the "positive" ("good") review label. Use "text" and "label" for column names. See lecture on how to create a pandas dataframe properly with column names! It's easy to create a dataframe with the wrong number of columns, and get confused with the column names.

3. If you print out the dataframe, you should see something like this:

```
0   Richard Farnsworth is one of my favorite actor...
0   My comments may be a bit of a spoiler for what...
0   The saucy misadventures of four au pairs who a...
0   Oh those Italians Assuming that movies about a...
0   Eight academy nominations Its beyond belief I ...
0   Not that I dislike childrens movies but this w...
```

-- these are the last negative reviews.

# Part 2:
