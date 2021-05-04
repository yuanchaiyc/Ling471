# Assignment 4: Naive Bayes classifier

In this assignment, you will use a Naive Bayes classifier to classify the IMDB reviews.

# Part 1: Another vector representation

In Assignment 3, we had a class for review vectors. That can be convenient for debugging/thinking about the problem, but in actuality, people usually use simple tables to store data vectors. Such a table simply contains rows where one of the columns is the gold label. 

1. Install (via `pip`) and import (in your assignment4.py) the `pandas` module
2.  Store the data vectors as a pandas dataframe (see lecture). Use 1 and 0 for labels where 1 is the "positive" ("good") review label. You still have the code which creates review vectors for predictSimplistic; you can create two lists, one containing all the review texts and one containing all the labels, in those two for loops which you used to create review_vec instances. Then pass the two lists to pandas.DataFrame() and store the result in a variable.
3. If you print out the dataframe, you should see something like this:

```
0   Towards the end of the movie I felt it was too...
0   This is the kind of movie that my enemies cont...
0   I saw Descent last night at the Stockholm Film...
0   Some films that you pick up for a pound turn o...
0   This is one of the dumbest films Ive ever seen...
```

-- these are the last negative reviews.

# Part 2:
