# Assignment 5

In this final assignment, you will (1) add some linguistic preprocessing to your data; and (2) compare various models with each other (including different *data* models/formats), preparing a report with a few visualizations. (You will also use standard output (print statements) as a progress indicator for slow programs.)

**You have come very far. You started perhaps with zero programming experience, and you are now going to be manipulating powerful data models! Take a moment to think back and appreciate just how far you have come!**

**Disclaimer:** This assignment may be somewhat annoying. It's long and at times tedious. Sorry! I think you won't regret going through it though, because this is the real practical stuff :).

**Disclaimer2:** To our disappointment, we will find that linguistic processing didn't give us much! It is not the case that linguistic knowledge never is important; it is more that it is hard to integrate it properly into the model. Also, sometimes the simplest model is simply... *good enough*! And that's an important lesson. 

### Submission summary, to be committed like usual, to the repo that you share with the instructors. The commit number is submitted to Canvas for time stamp.
1. The updated `imdb_dataframe.py` (see Part 1).

2. Your `largest_counts.py` (with the function completed).

3. A **PDF file** `UW_NET_ID_report.pdf` with your report for Part 1 Section 6 and 7, and Part 2. **PLEASE DO NOT FORGET TO DO THIS. IT IS WORTH *A LOT* OF POINTS.**

4. Your UW_NET_ID_assignment5.py (Part 2)

### Part 0: Get the skeleton
1. Obtain the skeleton from the class GitHub repository.

2. Start a **document** (in your favorite text editor or word processor, but such that it can be ultimately **saved as PDF**). We will later ask you to include various tables and figures in the document and comment on them.

### Part 1: Preprocessing (in imdb_dataframe.py and in largest_counts.py)

1. In the `imdb_dataframe.py` skeleton, you will notice that the **CleanFileContents()** function has changed. We added several additional things to it. There are some comments there explaining the new steps. Set up the debugger and **step through some of the program execution** (e.g. some number of words in one file) to understand what the function is doing now and what changed. **NB:** You need to have installed `nltk` for this to work. Make sure you can do that **early**.

2. Merge your `imdb_dataframe.py` with this new one such that it works with the new CleanFileContents() and stores additional return values (`cleaned_text`, `lowercased`, `no_stopwords`, and `lemmatized`) in additional columns in the dataframe, named appropriately. The code is already there, you just need to harmonize it with your main(). That is, the code that creates the `cleaned_text`, `lowercased`, `no_stopwords`, and `lemmatized` verions is already written; you just need to make sure you are making use of it.

3. **Run** `imdb_dataframe.py` on **all** IMDB files **saving the result** in a **new** csv file. You may call it `my_expanded_imdb.csv`. The **saving** part is **already included**, but you need to **add iteration over directories and files**.

4. Step 3 takes some time. This is because you are iterating over every word in each text and performing expensive language processing such as stemming. To reassure yourself that your program is making progress, insert a print statement in `main()` which will print out a message for every 100th file: "Processing dir {} out of {}, file {} out of {}".    **Capture the standard output** in a text file.

    NB: These progress output lines are **required** because this is important technique and we want to make sure you know it! See [hints](Assignment5-hints.md).

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

    
5. Once you have the new dataframe file, move to `largest_counts.py`. Finish implementing the function (sort the counts), and obtain the **most frequent words** from the "review" (uncleaned, **original** text) column and also the most frequent words in the **newly added** columns, using your word counter from Assignment 2 or any other method (you can use others' code here, but do give the source in a comment). Look at **training reviews only**. See [hints](Assignment5-hints.md).

6. In your document, present the most common (**top 20**) words in positive and negative reviews (separately!), for:

    1. original data
    2. data cleaned from non-letters (cleaned_text)
    3. data without stopwords
    4. lemmatized data.
    
    That's **eight (8)** groups of sorted word counts.
    
    You can use **any effective mode of presentation**, e.g. a table or a graph/plot where word counts are e.g. bars. It should be effective/readable. It can be a couple tables. **It must not be a text description but a visualization**. A table counts as visualization so long it is well-formatted. You can accompany the visualization with a comment or caption.

7. Inspect the "lemmatized" words in the dataframe (e.g. by opening it in Excel). Did the NLTK lemmatizer do a good job? What can you say about what it did? **Add a comment in your report**, below the tables/visualizations associated with 6.

    You can read more about lemmatization, but as a brief note of the summary, a lemmatizer or stemmer should be removing any prefixes, suffixes, etc. from a word. In a lemmatized data set, you should not see words like *cats*, *dogs*, *loved*, and *reanalyze*, only base forms like *cat*, *dog*, *love*, and *analyze*.

The contents of **No. 6 and 7** go into your `UW_NET_ID_report.pdf` file.


### Part 2: Model comparison (in UWNetID_assignment5.py)
 
1. Run the several different models indicated in the code (differing mainly in data processing) and record the 10 numbers (which you reported for Assignment 4) **for each model**. The code is kind of already in place but it assumes a certain signature (input/output) of the Naive Bayes method. See comments in the skeleton! You can adapt either your naive_bayes() program or the HW5 skeleton; up to you! Just make sure your code runs. See also [hints](Assignment5-hints.md). 
    
2. **Plot** all numbers in one or several graphs. You are going to have 50 numbers in total to be plotted.

    ```
    original    train   accuracy        0.97028           clean   train   accuracy      0.97016
                        pos precision   0.98141                           pos precision 0.98046
                        pos recall      0.95872                           pos recall    0.95944
                        neg precision   0.95965                           neg precision 0.96029
                        neg recall      0.98184                           neg recall    0.98088
                test    accuracy        0.86832                   test    accuracy      0.86912
                        pos precision   0.90279                           pos precision 0.90184
                        pos recall      0.82552                           pos recall    0.8284
                        neg precision   0.83927                           neg precision 0.84132
                        neg recall      0.91112                           neg recall    0.90984
    lowercase   train   accuracy        0.97016           nonstop train   accuracy      0.98688 
                        pos precision   0.98046                           pos precision 0.98907
                        pos recall      0.95944                           pos recall    0.98464
                        neg precision   0.96029                           neg precision 0.98470
                        neg recall      0.98088                           neg recall    0.98912
                test    accuracy        0.86912                   test    accuracy      0.86412
                        pos precision   0.90184                           pos precision 0.88270
                        pos recall      0.8284                            pos recall    0.83984
                        neg precision   0.84132                           neg precision 0.84725
                        neg recall      0.90984                           neg recall    0.8884
    lemmatized  train   accuracy        0.98332                          
                        pos precision   0.98623                             
                        pos recall      0.98032                           
                        neg precision   0.98043                              
                        neg recall      0.98632                               
                test    accuracy        0.8582                    
                        pos precision   0.87434                       
                        pos recall      0.83664                       
                        neg precision   0.84339                            
                        neg recall      0.87976                            
    ```

{'train': {'accuracy': 0.97028, 'POS': {'precision': 0.9814102039145033, 'recall': 0.95872}, 'NEG': {'precision': 0.9596528266479005, 'recall': 0.98184}}, 'test': {'accuracy': 0.86832, 'POS': {'precision': 0.9027996500437445, 'recall': 0.82552}, 'NEG': {'precision': 0.8392778187177597, 'recall': 0.91112}}}
{'train': {'accuracy': 0.97016, 'POS': {'precision': 0.980461085676913, 'recall': 0.95944}, 'NEG': {'precision': 0.9602913533834586, 'recall': 0.98088}}, 'test': {'accuracy': 0.86912, 'POS': {'precision': 0.9018463682285316, 'recall': 0.8284}, 'NEG': {'precision': 0.8413226808699512, 'recall': 0.90984}}}



    There are different ways to organize the data on a plot. Codes for example plots in matplotlib can be found at the [matplotlib tutorial websites](https://matplotlib.org/stable/gallery/index.html#examples-index). Y-axis will be percentage score, On x-axis, you can group the data by the parameter. For example on x-axis, you have train accuracy, test accuracy, train pos precision, test pos precision, ..., and within each parameter, you have five stacked bars for different models, so that you can compare *original* vs *clean text* vs *lowercase* vs *no stop words* vs *lemmatized* with these five bars juxtaposed to each other. You can also group data by model, for example, on x-axis, you have *original*, *clean text*, *lowercase*, *no stop words*, *lemmatized*. And within each model, you have ten stacked bars for each parameters, so that you are comparing *train accuracy* vs *test accuracy* vs *train pos precision* vs *train neg precision* vs ... .

    Of course, plotting all 50 numbers on one plot could be very crowded, you can plot five parameters on one plot (e.g. train accuracy, train pos precision, train pos recall, train neg precision, train neg recall), and another five parameters on the other plot (e.g. test accuracy, test pos precision, test pos recall, test neg precision, test neg recall).

    Use different colors and/or styles of line (dotted, dashed...) to indicate *training* vs. *test* data, *precision* vs. *recall* etc. You may use different graphs for positive and negative reviews, or you may use different colors/styles of line/bar/whatever-you-choose-for-visualization here as well and cram *everything* in one plot. Keep in mind that the graph(s) **must be clear and readable, and effective in conveying the information.** It is **not obvious what is best** here.
    
    For example, keeping train and test data in one plot may be very effective, because it is then easier to compare them, and same goes for positive and negative reviews. Maybe you can't cram *everything* in one graph. You will need to prioritize and make decisions. **Experiment and explore**; look at how others visualize multiple models comparison and try to learn how to do what seems effective to you.
    
    If you really want to do so, you *can* draw your plots by hand, but the same readability requirements apply, and they must look reasonably accurate. Additionally, they **must** be included in your PDF; they cannot be submitted separately.

5. In the document, **explain what the graphs indicate**, in your own words. Then **comment on the numbers**. We don't know why the numbers are what they are, but we can think about **several things**:
    1. English as a language, it has certain properties. E.g. English is a morphologically simple language. How does this potentially affect the value of lemmatization?
    2. Dataset size. IMDB is fairly large! How may this affect the value of preprocessing?
    3. The genre. How do people tend to write reviews, what style/grammar do they tend to employ? How might that affect the value of e.g. lowercasing?
    4. ...anything else that you might think about here! We look forward to hearing your thoughts!

The graph(s) and proses in Part 2 go into `UW_NET_ID_report.pdf` file.