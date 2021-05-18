[home](../index.md)

# Assignment 5

In this final assignment, you will (1) add some linguistic preprocessing to your data; and (2) compare various models with each other (including different *data* models/formats), preparing a report with a few visualizations. (You will also use standard output (print statements) as a progress indicator for slow programs.)

### Submission summary, to be committed to the repo that you share with the instructors:
1. The updated `imdb_dataframe.py` (see Part 1).

2. A text file capturing the **standard output** of your `imdb_dataframe.py`. Name it: UW_NET_ID_dataframe.txt. The file should look something like this:
    ```
    Test NEG: Processing dir 1/4, file 100 out of 12500
    Test NEG: Processing dir 1/4, file 200 out of 12500
    Test NEG: Processing dir 1/4, file 300 out of 12500
    ...
    ...
    ...
    Train POS: Processing dir 4/4, file 12200 out of 12500
    Train POS: Processing dir 4/4, file 12300 out of 12500
    Train POS: Processing dir 4/4, file 12400 out of 12500
    ```
    **You can format this output as you like**, so long as it is clearly reporting progress. It **does not** need to look exactly like above.

3. The **csv file** that your `imdb_dataframe.py` output, with at least 4 columns: file type (train or test), gold label (1 or 0), review text, and cleaned review text. Additional columns (such as file name) are optional.

4. A PDF file with your report for Part 2.

5. Your UW_NET_ID_assignment5.py (Part 2)

### Part 0: Get the skeleton and run the neural model
1. Obtain the skeleton the usual way from FIXME.

2. In the skeleton, there is a file `imbd_neural.py`. Install all the missing packages (particularly `tensorflow`) and make sure the program runs as expected (you can check against the original blog here:[https://thedatafrog.com/en/articles/word-embedding-sentiment-analysis/](https://thedatafrog.com/en/articles/word-embedding-sentiment-analysis/)). Ask any questions you like about the code on the discussion board, and note how the author of the code visualizes things such as accuracy in matplotlib.

### Part 1: Better clean up and lemmatization (in imdb_dataframe.py)

1. In the `imdb_dataframe.py` skeleton, you will notice that the CleanFileContents() function has changed. We added several additional things to it. There are some comments there explaining the new steps. Set up the debugger and step through some of the program execution (e.g. some number of words in one file) to understand what the function is doing now and what changed.

2. Merge the  `imdb_dataframe.py` skeleton with your `imdb_dataframe.py` from Assignment 4 such that you have your main() but the new CleanFileContents() as well as the new import statements. 

3. Change the main() function such that it works with the new CleanFileContents() and store additional return values (`cleaned_text`, `no_stopwords`, and `lemmatized`) in additional columns in the dataframe, named appropriately.

4. Run the program on all files **saving** the result in a csv file. Note that **this will take some time**. This is because you are iterating over every word in each text and performing expensive language processing such as stemming. **To reassure yourself that your program is making progress**, insert a print statement in main() which will print out a message for every 100th file: "Processing dir {} out of {}, file {} out of {}" (you will need to keep a counter for this, but you know how to do this!). **Capture the standard output** in a text file. So, running the updated `imdb_dataframe.py` will result in two files: a csv file and a text file. To capture standard output (print statements) in a file, run your program in command line like this: 

    `python imdb_dataframe.py dir1 dir2 dir3 dir4 > UW_NET_ID_output.txt` 

5. Open the csv file (you can do this in VS Code) and inspect the new column. It is going to look a little weird! Take a note of a few things. We will ask you to say something about them in the report in Part 2.


### Part 2: Model comparison (in UWNetID_assignment5.py)
1. Start a document (in your favorite text editor but such that it can be saved as PDF). In this Part, we will ask you to include various tables and figures in the document and comment on them.

2. Import your Assignment 3 and Assignment 4 code into the Assignment 5 code as modules. (You may or may not need Assignment 2, depending on whether your Assignment 3 relies on it.)
 
3. Using python documentation and/or StackOverflow (or similar), **learn how to sort a python dict by value in reverse (descending order)**. (I could explain it to you, but it is important to learn to figure such things out on your own.) For example, given a dict: `{'a':1, 'b':3, g: '2'}`, you should get: `{'b':3, 'g':2, 'a':1}`. Feel free to ask on Discussion board if you don't understand the documentation/solution. **Do not implement your own sorting algorithm"; use the built-in python methods.**

4. After you successfully sort a toy python dict by value in descending order, use this knowledge to compare the most frequent words from the "review" (uncleaned, original text) column to the most frequent words in the "cleaned_review" column, using your word counter from Assignment 2 or any other method (you can use others' code here, but do give the source in a comment). Look at training reviews only. **In your document, present** the most common (top 30) words in positive and negative reviews (separately!), for: (i) original data; (ii) data cleaned from non-letters; and (iii) data without stopwords. That's **six** groups of sorted word counts. You can use any mode of presentation, e.g. a table or a graph/plot where word counts are e.g. bars. It should be effective/readable. **It must not be a text description but a visualization** (a table counts as visualization so long it is well-formatted). You can accompany the visualization with a comment.

5. Run several different models and record the 10 numbers (which you reported for Assignment 4) **for each model**:
    1. predictSimplistic (now run it not only on training but also on test data)
    2. NaiveBayes on the original review text (that's your Assignment 4)
    3. NaiveBayes with additional clean up provided in Assignment 5 skeleton **but without lowercasing, without removing stopwords, and with no lemmatization**
    4. Naive Bayes with additional clean up and with lowercasing.
    5. Naive Bayes with additional clean up, lowercasing, and with stopwords removed.
    6. Naive Bayes with additional clean up, with lowercasing, with stopwords removed, and with lemmatization.
    7. The neural model that you got with the skeleton (yes, it uses a different version of the dataset. It's not ideal but it's OK for this assignment. Don't do that (compare models' performance on different versions of data) in real life :). For the neural model, you only have the accuracy score. That's OK.
    
    **You may either program your main() to run all the functions one after another automatically and automatically populate an array with the scores, or you may output the numbers for each model in a separate file and either read them automatically from a file or manually put them into an array for plotting**. Doing everything automatically is better but we are not requiring that in this assignment. If you are putting numbers in manually, triple check that you didn't make any mistakes; that's a lot of numbers to enter!

6. Plot all numbers in one or several graphs, such that the X axis is the type of model (just its name) and the Y axis is a percentage score. So, you will have 7 (seven) discrete ticks on the X axis, but 10 scores corresponding to **six** of them, so, potentially 10 different lines/bars/charts in one plot. Use different colors to indicate training vs. test data and furthermore different colors/style for lines tracking accuracy, precision, and recall. You may use different graphs for positive and negative reviews, or you may use different colors/styles of line/bar/whatever-you-choose-for-visualization here as well and cram *everything* in one plot. Keep in mind that the graph(s) **must be clear and readable, and effective in conveying the information.** It is not obvious what is best here. For example, keeping train and test data in one plot may be very effective, because it is then easier to compare them, and same goes for positive and negative reviews. But perhaps you can't cram *everything* in one graph. You will need to prioritize and make decisions. Experiment and explore; looks at how others visualize multiple models comparison and try to learn how to do what seems effective to you. 

### Part 3: Fun with embeddings!

1. There are two TODOs in `neural_imdb.py`. They ask you to come up with an experimental "unseen" review and visualize it. Complete these TODOs. After this, you should have 7 `png` files produced by this program: `accuracy.png, words.png, Review15.png, Review17.png, my_review1.png, my_review2.png, and my_review3.png`. Include all these figures in your report/document. Comment on each figure, what it means/represents, and anything you find interesting about it. For `my_review2.png` and `my_review2.png`in particular, comment about whether the spatial representation for this "review" in 2D ended up meaningful in any respect (like the representation of `my_review1`) and if not, why do you think that is.

[home](../index.md)
