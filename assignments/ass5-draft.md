# Assignment 5

In this final assignment, you will (1) add some linguistic preprocessing to your data; and (2) compare various models with each other, ending up preparing a report with a few visualizations. (You will also use standard output (print statements) as a progress indicator for slow programs.)

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

3. The **csv file** that your `imdb_dataframe.py` output, with at least 4 columns: file type (train or test), gold label (1 or 0), review text, and cleaned review text. Additional columns (such as file name) are optional.

4. A PDF file with your report for Part 2.

5. Your UW_NET_ID_assignment5.py (Part 2)

### Part 0: Get the skeleton

### Part 1: Better clean up and lemmatization (in imdb_dataframe.py)

1. In the `imdb_dataframe.py` skeleton, you will notice that the CleanFileContents() function has changed. We added several additional things to it. There are some comments there explaining the new steps. Set up the debugger and step through some of the program execution (e.g. some number of words in one file) to understand what the function is doing now and what changed.

2. Merge the  `imdb_dataframe.py` skeleton with your `imdb_dataframe.py` from Assignment 4 such that you have your main() but the new CleanFileContents() as well as the new import statements. 

3. Change the main() function such that it works with the new CleanFileContents() and store the additional return value (`cleaned_text`) in an additional column in the dataframe, called "cleaned_review" or something else sensible.

4. Run the program on all files **saving** the result in a csv file. Note that **this will take some time**. This is because you are iterating over every word in each text and performing expensive language processing such as stemming. **To reassure yourself that your program is making progress**, insert a print statement in main() which will print out a message for every 100th file: "Processing dir {} out of {}, file {} out of {}" (you will need to keep a counter for this, but you know how to do this!). **Capture the standard output** in a text file. So, running the updated `imdb_dataframe.py` will result in two files: a csv file and a text file. To capture standard output (print statements) in a file, run your program in command line like this: 

    `python imdb_dataframe.py dir1 dir2 dir3 dir4 > UW_NET_ID_output.txt` 

5. Open the csv file (you can do this in VS Code) and inspect the new column. It is going to look a little weird! Take a note of a few things. We will ask you to say something about them in the report in Part 2.


### Part 2: Model comparison (in UWNetID_assignment5.py)
1. Compare the most frequent words from the "review" (uncleaned, original text) column to the most frequent words in the "cleaned_review" column. Look at training reviews only. To do this, use the TF-IDF vectorizer object. This object has a method `get_features()`.
