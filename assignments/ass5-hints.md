[home](../index.md)

# Assignment 5 Hints

Consult these steps if you don't know how to start the programming in Part 1 and Part 2.


### Part 1: Better clean up and lemmatization (in imdb_dataframe.py and in UWNetID_assignment5.py)

1. In the `imdb_dataframe.py` skeleton, you will notice that the CleanFileContents() function has changed. We added several additional things to it. There are some comments there explaining the new steps. Set up the debugger and step through some of the program execution (e.g. some number of words in one file) to understand what the function is doing now and what changed.

2. Merge the  `imdb_dataframe.py` skeleton with your `imdb_dataframe.py` from Assignment 4 such that you have your main() but the new CleanFileContents() as well as the new import statements. (By "merging" here I mean just manually.)

3. Change the main() function such that it works with the new CleanFileContents() and store additional return values (`cleaned_text`, `lowercased`, `no_stopwords`, and `lemmatized`) in additional columns in the dataframe, named appropriately.

4. Run `imdb_dataframe.py` on all IMDB files saving the result in a new csv file. You may call it `my_expanded_imdb.csv`. Note that **this will take some time**. This is because you are iterating over every word in each text and performing expensive language processing such as stemming. **To reassure yourself that your program is making progress**, insert a print statement in main() which will print out a message for every 100th file: "Processing dir {} out of {}, file {} out of {}" (you will need to keep a counter for this, but you know how to do this!). **Capture the standard output** in a text file. So, running the updated `imdb_dataframe.py` will result in two files: a csv file and a text file. To capture standard output (print statements) in a file, run your program in command line like this: 

    `python imdb_dataframe.py dir1 dir2 dir3 dir4 > UW_NET_ID_output.txt` 

5. Open the csv file (you can do this in VS Code) and inspect the new columns. 

6. Now that you have a new csv file, move to UWNetID_assignment5.py. Using python documentation and/or StackOverflow (or similar), **learn how to sort a python dict by value in reverse (descending order)**. (I could explain it to you, but it is important to learn to figure such things out on your own.) For example, given a dict: `{'a':1, 'b':3, g: '2'}`, you should get: `{'b':3, 'g':2, 'a':1}`. Feel free to ask on Discussion board if you don't understand the documentation/solution. **Do not implement your own sorting algorithm"; use the built-in python methods.**

7. After you've successfully sorted a toy python dict by value in descending order, use this knowledge to compare the most frequent words from the "review" (uncleaned, original text) column to the most frequent words in the newly added columns, using your word counter from Assignment 2 or any other method (you can use others' code here, but do give the source in a comment). Look at **training reviews only**. 



### Part 2: Model comparison (in UWNetID_assignment5.py)

1. Import or copy your `evaluation.py` functions computing accuracy and precision and recall into Assignment 5. 

2. Put all your Naive Bayes code from Assignment 4 into a function and import that function into Assignment 5. 

3. Modify it such that it accepts a column name and grabs the review text from that column. 

4. Modify it such that it returns a dict or a list contatining the 10 output numbers. It is up to you which order/format; just make sure it is clear to you what that is and you don't make a mistake later accessing the numbers.
 
5. Run several different models and record the 10 numbers (which you reported for Assignment 4) **for each model**:
    1. predictSimplistic (now run it not only on training but also on test data)
    2. NaiveBayes on the original review text (that's your Assignment 4)
    3. NaiveBayes with additional clean up provided in Assignment 5 skeleton **but without lowercasing, without removing stopwords, and with no lemmatization**
    4. Naive Bayes with additional clean up and with lowercasing.
    5. Naive Bayes with additional clean up, lowercasing, and with stopwords removed.
    6. Naive Bayes with additional clean up, with lowercasing, with stopwords removed, and with lemmatization.
    7. The neural model that you got with the skeleton (yes, it uses a different version of the dataset. It's not ideal but it's OK for this assignment. Don't do that (compare models' performance on different versions of data) in real life :). For the neural model, you only have the accuracy score. That's OK.
    
    **You may either program your main() to run all the functions one after another automatically and automatically populate an array with the scores, or you may output the numbers for each model in a separate file and either read them automatically from a file or manually put them into an array for plotting**. Doing everything automatically is better but we are not requiring that in this assignment. If you are putting numbers in manually, triple check that you didn't make any mistakes; that's a lot of numbers to enter!


[home](../index.md)
