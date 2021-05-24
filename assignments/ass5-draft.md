[home](../index.md)

# Assignment 5

In this final assignment, you will (1) add some linguistic preprocessing to your data; and (2) compare various models with each other (including different *data* models/formats), preparing a report with a few visualizations. (You will also use standard output (print statements) as a progress indicator for slow programs.)

**You have come very far. You started perhaps with zero programming experience, and you are now going to be manipulating powerful data models! Take a moment to think back and appreciate just how far you have come!**

**Disclaimer:** This assignment may be somewhat annoying. It's long and at times tedious. Sorry! I think you won't regret going through it though, because this is the real practical stuff :).

**Disclaimer2:** To our disappointment, we will find that linguistic processing didn't give us much! It is not the case that linguistic knowledge never is important; it is more that it is hard to integrate it properly into the model. Also, sometimes the simplest model is simply... *good enough*! And that's an important lesson. 

### Submission summary, to be committed like usual, to the repo that you share with the instructors. The commit number is submitted to Canvas for time stamp.
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

3. The **csv file** that your `imdb_dataframe.py` output, with at least 7 (seven) columns: file type (train or test), gold label (1 or 0), original review text, cleaned review text, lowercased review text, review text with stopwords removed, and lemmatized review text. (These levels of processing are already implemented for you and explained in Part 1.) Additional columns (such as file name) are optional.

4. A PDF file with your report for Part 2.

5. Your UW_NET_ID_assignment5.py (Part 2)

6. If you did the bonus word embeddings part (Part III), your updated `neural_imdb.py` with the TODOs completed.

### Part 0: Get the skeleton
1. Obtain the skeleton the usual way by importing or privately copying https://github.com/olzama/Ling471-SP2021-HW5.

2. In the skeleton, there is a file `imbd_neural.py`. This is a **bonus** assignment. If you wish to complete it, install all the missing packages (particularly `tensorflow`) and make sure the program runs as expected (you can check against the original blog here:[https://thedatafrog.com/en/articles/word-embedding-sentiment-analysis/](https://thedatafrog.com/en/articles/word-embedding-sentiment-analysis/)). Ask any questions you like about the code on the discussion board, and note how the author of the code visualizes things such as accuracy in matplotlib. It's pretty **fun** but feel free to leave it till the end. There is no programming involved, everything is already implemented.

3. Start a document (in your favorite text editor but such that it can be ultimately saved as PDF). We will later ask you to include various tables and figures in the document and comment on them.


### Part 1: Preprocessing (in imdb_dataframe.py and in UWNetID_assignment5.py)

1. In the `imdb_dataframe.py` skeleton, you will notice that the **CleanFileContents()** function has changed. We added several additional things to it. There are some comments there explaining the new steps. Set up the debugger and **step through some of the program execution** (e.g. some number of words in one file) to understand what the function is doing now and what changed. **NB:** You need to pip-install the **nltk package** for this to work. Make sure you can do that **early**.

3. Merge your `imdb_dataframe.py` with this new one such that it works with the new CleanFileContents(), and store **additional return values** (`cleaned_text`, `lowercased`, `no_stopwords`, and `lemmatized`) in **additional columns** in the dataframe, named appropriately. 

4. Run `imdb_dataframe.py` on all IMDB files saving the result in a new csv file. You may call it `my_expanded_imdb.csv`. 

5. Step 4 takes some time. This is because you are iterating over every word in each text and performing expensive language processing such as stemming. To reassure yourself that your program is making progress, insert a print statement in main() which will print out a message for every 100th file: "Processing dir {} out of {}, file {} out of {}".    **Capture the standard output** in a text file. NB: This step (both the progress indicator and capturing standard output in a file) is **required** because these are both important techniques and we want to make sure you learn it! See [hints](ass5-hints.md).
    
5. Once you have the new dataframe file, move to `assignment5.py`. There, compare the **most frequent words** from the "review" (uncleaned, **original** text) column to the most frequent words in the **newly added** columns, using your word counter from Assignment 2 or any other method (you can use others' code here, but do give the source in a comment). Look at **training reviews only**. See [hints](ass5-hints.md).

6. In your document, present the most common (**top 20**) words in positive and negative reviews (separately!), for: (i) original data; (ii) data cleaned from non-letters; (iii) data without stopwords, and (iv) lemmatized data. That's **eight** groups of sorted word counts. You can use **any effective mode of presentation**, e.g. a table or a graph/plot where word counts are e.g. bars. It should be effective/readable. It can be a couple tables. **It must not be a text description but a visualization** (a table counts as visualization so long it is well-formatted). You can accompany the visualization with a comment.

7. Inspect the "lemmatized" words in the dataframe (e.g. by opening it in Excel). Did the NLTK lemmatizer do a good job? What can you say about what it did? **Add a comment in your report**, below the tables/visualizations associated with 6.


### Part 2: Model comparison (in UWNetID_assignment5.py)
 
1. Run several different models (differing mainly in data processing) and record the 10 numbers (which you reported for Assignment 4) **for each model**. The code is kind of already in place but it assumes a certain signature (input/output) of the Naive Bayes method. See comments in the skeleton! You can adapt either your naive_bayes() program or the HW5 skeleton; up to you! See also [hints](ass5-hints.md). 
 
2. **BONUS**: Add the neural model that you got with the skeleton (yes, it uses a different version of the dataset. It's not ideal but it's OK for this assignment. Don't do that (compare models' performance on different versions of data) in real life :). For the neural model, you only have the accuracy score. That's OK.

3. **BONUS**: Add the predictSimplistic model (now run it not only on training but also on test data)
    
4. **Plot** all numbers in one or several graphs, such that the X axis is the type of model (just its name) and the Y axis is a percentage score. So, you will have 5--7 (five to seven, depending on whether you did the bonus parts) discrete ticks on the X axis, but 10 scores corresponding to most of them, so, **potentially** 10 different lines/bars/charts in one plot. Use different colors to indicate training vs. test data and furthermore different colors/style (e.g. dotted) for lines tracking accuracy, precision, and recall. You may use different graphs for positive and negative reviews, or you may use different colors/styles of line/bar/whatever-you-choose-for-visualization here as well and cram *everything* in one plot. Keep in mind that the graph(s) **must be clear and readable, and effective in conveying the information.** It is **not obvious what is best** here. For example, keeping train and test data in one plot may be very effective, because it is then easier to compare them, and same goes for positive and negative reviews. But perhaps you can't cram *everything* in one graph. You will need to prioritize and make decisions. **Experiment and explore**; look at how others visualize multiple models comparison and try to learn how to do what seems effective to you. 

5. In the document, **explain what the graphs indicate**, in your own words. Then **comment on the numbers**.  We don't know why the numbers are what they are, but we can think about **several things**:
    1. English as a language, it has certain properties. E.g. English is a morphologically simple language. How does this potentially affect the value of lemmatization?
    2. Dataset size. IMDB is fairly large! How may this affect the value of preprocessing?
    3. The genre. How do people tend to write reviews, what style/grammar do they tend to employ? How might that affect the value of e.g. lowercasing?
    4. ...anything else that you might think about here! We look forward to hearing your thoughts! 

### Part 3: BONUS (optional): Fun with embeddings!

1. There are **two TODOs** in `neural_imdb.py`. They ask you to come up with an experimental "unseen" review and visualize it. Complete these TODOs. After this, you should have **6** `png` files produced by this program: `accuracy.png, words.png, Review15.png, Review17.png, my_review1.png, my_review2.png`. **Include all these figures in your report/document**. **Comment on each figure**, what it means/represents, and anything you find interesting about it. For `my_review2.png` in particular, comment about whether the spatial representation for this "review" in 2D ended up meaningful in any respect (like the representation of `my_review1`) and if not, why do you think that is.

[home](../index.md)
